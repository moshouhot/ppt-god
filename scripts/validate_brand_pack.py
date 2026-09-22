#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = [
    "manifest.json",
    "BRAND_SYSTEM.md",
    "brand.css",
    "layouts/cover.html",
    "layouts/contents.html",
    "layouts/section.html",
    "layouts/content.html",
    "layouts/ending.html",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("brand_pack", type=Path)
    ns = ap.parse_args()
    root = ns.brand_pack.resolve()
    errors = []
    warnings = []
    for rel in REQUIRED:
        if not (root / rel).exists():
            errors.append(f"missing:{rel}")
    manifest_path = root / "manifest.json"
    if manifest_path.exists():
        try:
            m = json.loads(manifest_path.read_text(encoding="utf-8"))
            for key in ["name", "version", "canvas", "safe_area", "locked_elements", "representative_slides"]:
                if key not in m:
                    warnings.append(f"manifest_missing:{key}")
        except Exception as e:
            errors.append(f"manifest_invalid:{e}")
    result = {"root": str(root), "errors": errors, "warnings": warnings, "valid": not errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
