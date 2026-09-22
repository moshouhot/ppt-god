#!/usr/bin/env python3
"""Render a static HTML slide deck to PNG pages using WeasyPrint.

The deck should expose each slide as `.slide` and use a fixed canvas. This renderer
injects print CSS so each `.slide` becomes exactly one page. JavaScript/canvas effects
must be flattened before this step.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from weasyprint import HTML, CSS


def find_cmd(name: str) -> str:
    p = shutil.which(name)
    if not p:
        raise SystemExit(f"Required command not found: {name}")
    return p


def print_css(width: int, height: int, hide_text: bool = False) -> CSS:
    hide = "* { color: transparent !important; text-shadow: none !important; }" if hide_text else ""
    return CSS(string=f"""
@page {{ size: {width}px {height}px; margin: 0; }}
html, body, .deck {{ margin: 0 !important; padding: 0 !important; background: transparent !important; }}
.slide {{
  width: {width}px !important;
  height: {height}px !important;
  min-width: {width}px !important;
  min-height: {height}px !important;
  max-width: {width}px !important;
  max-height: {height}px !important;
  margin: 0 !important;
  overflow: hidden !important;
  break-after: page !important;
  page-break-after: always !important;
}}
.slide:last-child {{ break-after: auto !important; page-break-after: auto !important; }}
{hide}
""")


def render_pdf(html_path: Path, pdf_path: Path, width: int, height: int, hide_text: bool = False):
    HTML(filename=str(html_path), base_url=str(html_path.parent)).write_pdf(
        str(pdf_path), stylesheets=[print_css(width, height, hide_text=hide_text)]
    )


def pdf_to_pngs(pdf_path: Path, output_dir: Path, dpi: int = 96) -> list[Path]:
    pdftoppm = find_cmd("pdftoppm")
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = output_dir / "slide"
    proc = subprocess.run(
        [pdftoppm, "-png", "-r", str(dpi), str(pdf_path), str(prefix)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(f"pdftoppm failed:\n{proc.stdout}")
    images = sorted(output_dir.glob("slide-*.png"))
    for idx, src in enumerate(images, 1):
        dst = output_dir / f"slide-{idx:02d}.png"
        if src != dst:
            if dst.exists():
                dst.unlink()
            src.rename(dst)
    return sorted(output_dir.glob("slide-*.png"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output_dir", type=Path)
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=720)
    ap.add_argument("--dpi", type=int, default=96)
    ns = ap.parse_args()

    source = ns.input.resolve()
    out = ns.output_dir.resolve()
    if not source.exists():
        raise SystemExit(f"Input not found: {source}")
    out.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="ppt-god-html-") as td:
        pdf = Path(td) / "deck.pdf"
        render_pdf(source, pdf, ns.width, ns.height)
        images = pdf_to_pngs(pdf, out, ns.dpi)
    print(f"Rendered {len(images)} slide(s) to {out}")
    return 0 if images else 2


if __name__ == "__main__":
    raise SystemExit(main())
