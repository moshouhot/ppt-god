---
name: ppt-god
description: Create high-visual or brand-aware presentations rather than ordinary generic slides. Use when the user asks for a polished pitch deck, launch deck, executive or sales presentation, visually distinctive PPT/PPTX, or a deck that should follow a company PPT template, logo, background, brand guide, or reusable Brand Pack. The skill turns source material into a story and storyboard, applies an OpenDesign-style design system, authors HTML slides, exports PPTX, and runs render-based QA and repair. Do not use it merely because a simple low-design presentation is requested; strict master/layout preservation belongs to a dedicated strict-template skill.
---

# PPT GOD

Build design-led decks with two specialties: **high-visual presentations** and **brand-aware corporate presentations**. Keep this as one portable Skill: use references for judgment, scripts for deterministic conversion/QA, and OpenDesign when it is available as the preferred visual-design engine.

## Operating principles

- Infer before asking. If audience, purpose, length, and visual direction can be reasonably inferred from the user's material, proceed without a questionnaire.
- Do not paginate source documents mechanically. Rebuild the material into a persuasive story.
- Separate **content reasoning** from **visual design**. Create a storyboard before designing slides.
- Reuse proven design systems, layouts, and prior art before inventing new primitives.
- Treat enterprise PPT templates as **brand shells** by default: preserve the recognizable logo/background/header/footer/brand language, but allow the content canvas to be redesigned.
- Default to **E2 Hybrid** editability: editable text and key data; complex decoration may remain SVG/raster.
- Prefer a visually correct deck with local raster fallback over a broken "fully editable" deck.
- A deck is not complete until the rendered PPTX has been inspected and repaired.

## Scope gate

1. If the user only needs a basic, low-design deck and provides no brand constraints, use the platform's ordinary slide capability instead of this skill.
2. If the user explicitly requires exact preservation of Slide Master, layouts, placeholders, animations, SmartArt, or unsupported native objects, classify it as **Strict Template**. Do not pretend this skill guarantees that. Hand off to a dedicated strict-template skill when available.
3. Otherwise continue with one of the two normal modes:
   - **Visual mode**: no mandatory corporate brand; create a design system.
   - **Brand mode**: use an existing Brand Pack, or compile one from the supplied corporate PPTX/brand materials.

## Runtime preflight

Read `references/runtime.md` before running bundled scripts. Do not silently skip render-based QA when a dependency is missing.

## Workflow

### 1. Understand the material

Read all supplied source material that is relevant. Determine internally:
- audience and decision context
- purpose and desired outcome
- one-sentence thesis
- key claims, evidence, numbers, and caveats
- likely slide count and presentation duration
- whether the user values E1, E2, or E3 editability

Ask a question only when missing information would materially change the deck and cannot be inferred.

### 2. Build the story

Create a short narrative arc before designing pages. Favor structures such as:
- context → problem → insight → solution → evidence → plan → ask
- why now → opportunity → product → proof → economics → roadmap
- current state → gap → design basis → proposal → impact → implementation

Do not preserve source chapter order unless it is already the strongest presentation order.

### 3. Build Storyboard IR

Create an internal `storyboard.json` using `references/storyboard.md` and `references/storyboard.schema.json`.

Every slide must have:
- `role`
- `title`
- `message`
- `content`
- `visual_intent`
- `importance`
- `editability`
- `asset_requirements`

OpenDesign or any visual authoring step receives the storyboard, not raw source material.

### 4. Establish the presentation design system

#### Visual mode

Create a compact `DESIGN.md` using `references/design-system.md`.

#### Brand mode

If a Brand Pack already exists, validate and use it.

If the user supplies a corporate PPTX for the first time:
1. Run `python scripts/brand_extract.py <template.pptx> <brand-pack-dir>`.
2. Inspect generated representative renders and manifest.
3. Refine `BRAND_SYSTEM.md`, `brand.css`, and the HTML shells.
4. Run `python scripts/validate_brand_pack.py <brand-pack-dir>`.
5. Keep the Brand Pack as a reusable deliverable.

Read `references/brand-pack.md` before doing this.

### 5. Plan assets before layout

For each slide, resolve `asset_requirements` before final layout. Prefer user-provided assets, existing brand assets, authoritative charts/diagrams, appropriate imagery, then icons/illustrations. Do not add generic decorative images merely to fill space.

### 6. Author HTML slides

Use OpenDesign when it is available. Read `references/open-design.md` first.

Preferred prior art inside OpenDesign:
- `guizang-ppt` for editorial/magazine/high-impact decks
- `html-ppt-*` for reusable theme/layout systems
- `critique` for design self-review
- brand `DESIGN.md` for persistent visual constraints

If OpenDesign is unavailable, author a static HTML deck directly using the same contract. Start from `assets/deck-starter/`.

Rules:
- default canvas: 16:9, 1280×720 CSS pixels
- one dominant message per slide
- use design tokens, not ad-hoc literal styling everywhere
- preserve brand-shell locked areas in Brand mode
- prefer a small vocabulary of layout families reused consistently
- vary rhythm across the deck
- avoid excessive rounded cards, gratuitous gradients, tiny text, repeated 3-card grids, random icons, and decorative noise

### 7. HTML visual QA

Render:
`python scripts/render_html_deck.py <deck.html> <render-dir>`

Build montage:
`python scripts/make_montage.py <render-dir> <montage.png>`

Inspect representative pages and montage. Repair overflow/cropping, weak hierarchy, bad crops, excessive density, inconsistent margins/grid, repetitive composition, off-brand elements, and unreadable charts.

### 8. Export PPTX

Choose the least-complex path that meets requested editability:
- use reliable OpenDesign PPTX export when available
- otherwise use `python scripts/html_to_pptx.py <deck.html> <output.pptx> --mode E2`
- use `--mode E3` when visual fidelity is more important than editability
- rebuild specific E1 elements natively rather than forcing the whole deck through one renderer

The bundled E2 exporter rasterizes the visual layer but recreates visible text as editable PowerPoint text.

### 9. PPTX QA and repair

Run:
`python scripts/validate_pptx.py <output.pptx>`

`python scripts/render_pptx.py <output.pptx> <ppt-render-dir>`

`python scripts/make_montage.py <ppt-render-dir> <ppt-montage.png>`

Inspect the PPT render, not merely the HTML preview. Repair conversion drift and repeat until no severe defect remains.

### 10. Deliver

Deliver final `.pptx`. For a company's first Brand-mode run, also deliver the reusable Brand Pack directory/ZIP.

## Editability levels

Read `references/editability.md` when the trade-off matters.

- **E1 Native-first**: maximize editable native objects.
- **E2 Hybrid (default)**: editable text/key data, raster/SVG for complex visual treatment.
- **E3 Visual-first**: preserve rendered appearance; rasterization is acceptable.

## Quality gate

Before declaring success:
- the deck has a coherent story
- every slide has a clear message
- high-importance slides receive stronger visual treatment
- the visual system is consistent
- Brand mode visibly preserves company identity
- the final PPTX opens and renders
- deterministic validator has no severe errors
- rendered PPTX has been visually inspected after export
- defects found during QA have actually been repaired

## References

Load only what is needed:
- `references/storyboard.md`
- `references/storyboard.schema.json`
- `references/design-system.md`
- `references/brand-pack.md`
- `references/editability.md`
- `references/open-design.md`
- `references/qa.md`
- `references/runtime.md`
- `references/prior-art.md`
