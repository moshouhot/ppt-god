#!/usr/bin/env python3
"""Create a simple contact-sheet montage from PNG/JPG slide renders."""
from __future__ import annotations

import argparse
import math
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input_dir", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--columns", type=int, default=4)
    ap.add_argument("--thumb-width", type=int, default=320)
    ns = ap.parse_args()

    files = sorted(
        [p for p in ns.input_dir.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
    )
    if not files:
        raise SystemExit("No images found")

    cols = max(1, ns.columns)
    first = Image.open(files[0]).convert("RGB")
    ratio = first.height / first.width
    tw = ns.thumb_width
    th = max(1, round(tw * ratio))
    label_h = 26
    gap = 14
    rows = math.ceil(len(files) / cols)
    sheet = Image.new("RGB", (cols * (tw + gap) + gap, rows * (th + label_h + gap) + gap), "white")
    draw = ImageDraw.Draw(sheet)

    for i, p in enumerate(files):
        img = Image.open(p).convert("RGB")
        fitted = ImageOps.fit(img, (tw, th), method=Image.Resampling.LANCZOS)
        col = i % cols
        row = i // cols
        x = gap + col * (tw + gap)
        y = gap + row * (th + label_h + gap)
        sheet.paste(fitted, (x, y))
        draw.text((x + 4, y + th + 5), f"{i+1:02d}  {p.name}", fill="black")

    ns.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(ns.output, quality=90)
    print(ns.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
