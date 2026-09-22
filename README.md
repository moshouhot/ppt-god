# PPT GOD

A high-visual and brand-aware presentation design Skill for ChatGPT/Codex.

This project is intentionally **not** a generic “make me a PowerPoint” skill. It focuses on two cases where a dedicated workflow adds real value:

- **High-visual presentations** — pitch decks, launches, executive/sales decks, product narratives, conference talks.
- **Brand-aware corporate presentations** — decks that preserve a company’s recognizable logo, background, typography, colors, header/footer and brand shell while allowing the main content canvas to be redesigned.

## Workflow

`source material → story → storyboard IR → design system / Brand Pack → HTML/OpenDesign → PPTX → render QA → repair`

Key ideas:

- Storyboard first: separate content reasoning from visual design.
- OpenDesign-style HTML/CSS authoring for strong visual quality.
- Reusable **Brand Packs** compiled from a company PPT template for later decks.
- Default **E2 Hybrid** editability: editable text/key data, with SVG/raster fallback for complex decoration.
- Render-based QA: a deck is not done until the generated PPTX is rendered, inspected, and repaired.
- Strict Slide Master/Layout preservation is deliberately out of scope and should be handled by a dedicated strict-template skill.

## Structure

```text
ppt-god/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── scripts/
└── assets/deck-starter/
```

## Install / use

Use the repository folder as a Skill bundle, or package `ppt-god/` as a ZIP and install it in your Skill environment.

The control plane is `SKILL.md`. Python dependencies used by helper scripts are listed in `scripts/requirements.txt`.

## Corporate template reuse

On first use, supply a corporate PPT template. PPT GOD extracts a reusable Brand Pack containing the recognizable brand shell and rules. Later decks can use the Brand Pack directly without the original template.

## Prior art

PPT GOD intentionally reuses proven ideas instead of reinventing presentation workflows in isolation. See [`references/prior-art.md`](references/prior-art.md).

Notable influences include Superpowers, OpenDesign, guizang-ppt-skill, html-ppt-skill, and render-based slide QA patterns.

## Scope

**In scope:** high-visual PPT/PPTX creation, brand-aware corporate decks, story/storyboard generation, Brand Pack extraction and reuse, HTML/OpenDesign slide authoring, PPTX export, render → inspect → repair QA.

**Out of scope:** generic low-design slide generation, exact Slide Master/Layout/Placeholder preservation, complex animation/VBA/SmartArt fidelity, standalone SaaS/desktop GUI/presentation editor.

## Status

V1 Skill bundle.
