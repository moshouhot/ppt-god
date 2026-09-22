#!/usr/bin/env python3
"""Render a PPTX to PNG slides using LibreOffice + pdftoppm.

Usage:
  python render_pptx.py input.pptx output_dir [--dpi 144]
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path


def find_cmd(*names: str) -> str:
    for name in names:
        p = shutil.which(name)
        if p:
            return p
    raise SystemExit(f"Required command not found: one of {', '.join(names)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output_dir", type=Path)
    ap.add_argument("--dpi", type=int, default=144)
    ns = ap.parse_args()

    inp = ns.input.resolve()
    out = ns.output_dir.resolve()
    if not inp.exists():
        raise SystemExit(f"Input not found: {inp}")
    out.mkdir(parents=True, exist_ok=True)

    soffice = find_cmd("libreoffice", "soffice")
    pdftoppm = find_cmd("pdftoppm")

    with tempfile.TemporaryDirectory(prefix="ppt-god-render-") as td:
        td_path = Path(td)
        proc = subprocess.run(
            [soffice, "--headless", "--convert-to", "pdf", "--outdir", str(td_path), str(inp)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            raise SystemExit(f"LibreOffice conversion failed:\n{proc.stdout}")
        pdf = td_path / f"{inp.stem}.pdf"
        if not pdf.exists():
            pdfs = list(td_path.glob("*.pdf"))
            if len(pdfs) == 1:
                pdf = pdfs[0]
            else:
                raise SystemExit(f"PDF was not produced. LibreOffice output:\n{proc.stdout}")

        prefix = out / "slide"
        proc2 = subprocess.run(
            [pdftoppm, "-png", "-r", str(ns.dpi), str(pdf), str(prefix)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
        if proc2.returncode != 0:
            raise SystemExit(f"pdftoppm failed:\n{proc2.stdout}")

    images = sorted(out.glob("slide-*.png"))
    for idx, src in enumerate(images, 1):
        dst = out / f"slide-{idx:02d}.png"
        if src != dst:
            if dst.exists():
                dst.unlink()
            src.rename(dst)
    images = sorted(out.glob("slide-*.png"))
    print(f"Rendered {len(images)} slide(s) to {out}")
    return 0 if images else 2


if __name__ == "__main__":
    raise SystemExit(main())
