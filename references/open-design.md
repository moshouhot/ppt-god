# OpenDesign integration

OpenDesign is the preferred visual-design engine when it is available, but this skill must remain usable without its desktop GUI.

## What to reuse from OpenDesign

OpenDesign's public project currently provides:
- deck mode
- brand `DESIGN.md` systems
- `guizang-ppt` for magazine/editorial decks
- the `html-ppt-*` family for theme/layout-driven decks
- a critique utility
- HTML/PDF/PPTX handoff paths
- headless/agent integrations in addition to its desktop UI

Prefer these existing patterns instead of inventing a new HTML presentation framework from zero.

## Recommended usage

1. Feed OpenDesign a resolved brief, storyboard, design system, and assets.
2. Select a coherent deck family; do not mix unrelated theme systems page-by-page.
3. Keep the output as real HTML/CSS so it can be inspected and repaired before PPTX export.
4. Run visual critique before export.
5. Treat current PPTX export behavior as an implementation detail that can change between OpenDesign versions. Verify the produced PPTX instead of assuming editability/fidelity.

## When OpenDesign is unavailable

Use `assets/deck-starter/` as the base HTML contract and follow the same design-system rules. The bundled render/export/QA scripts do not require the OpenDesign GUI.

## Current public prior art

- OpenDesign: https://github.com/attentiondotnet/open-design
- guizang-ppt-skill: https://github.com/op7418/guizang-ppt-skill
- html-ppt-skill: https://github.com/lewislulu/html-ppt-skill
