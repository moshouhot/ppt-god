# Brand Pack

A Brand Pack is the reusable result of analyzing a company's presentation template. It is not a full copy of every PowerPoint layout. It captures the minimum information needed to generate new decks that still look unmistakably like that company.

## Directory contract

```text
brand-pack/
├── manifest.json
├── BRAND_SYSTEM.md
├── brand.css
├── layouts/
│   ├── cover.html
│   ├── contents.html
│   ├── section.html
│   ├── content.html
│   └── ending.html
├── assets/
└── references/
```

## Manifest responsibilities

Record at least:
- pack name/version
- source template fingerprint
- canvas size/aspect ratio
- dominant colors
- font families
- safe content area
- locked elements
- representative slide indexes
- extracted asset inventory

## Extraction approach

1. Analyze the original PPTX structure and repeated edge elements.
2. Render representative slides when supported.
3. Extract reusable images and likely logo assets.
4. Detect dominant fonts/colors and estimate the safe content canvas.
5. Generate initial HTML shells and `brand.css`.
6. Visually inspect and refine the generated shell.
7. Validate the pack before using it.

## Brand-shell philosophy

By default, lock logo, background/chrome, company header/footer, page-number zone, and critical brand decoration. Allow redesign inside the safe content area.

Do not treat normal corporate templates as strict master-preservation tasks unless the user explicitly requires that.
