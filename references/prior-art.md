# Prior art deliberately reused

This skill is intentionally a synthesis of proven patterns rather than a new presentation framework invented in isolation.

## Superpowers brainstorming

Source: https://github.com/obra/superpowers

Adopted ideas:
- establish intent, constraints, and success criteria before implementation
- scale process to task complexity
- YAGNI: remove unnecessary machinery

Adaptation here:
- presentation work should infer obvious context instead of forcing approval gates and long software-design interviews
- the storyboard is the presentation-specific spec

## OpenDesign

Source: https://github.com/attentiondotnet/open-design

Adopted ideas:
- `DESIGN.md` as a reusable brand contract
- artifact-first HTML/CSS design loop
- deck mode and reusable skills/templates
- critique before handoff
- agent-native/headless use rather than GUI-only dependence

## guizang-ppt-skill

Source: https://github.com/op7418/guizang-ppt-skill

Adopted ideas:
- editorial/magazine presentation mindset
- strict visual presets are often more reliable than arbitrary color/style freedom
- strong validation/checklists for deck quality

## html-ppt-skill

Source: https://github.com/lewislulu/html-ppt-skill

Adopted ideas:
- token-driven themes
- reuse existing page layouts before inventing new ones
- static HTML/CSS as a transparent presentation surface
- headless browser rendering for verification
- consistent chrome slots and scoped templates

## OpenAI/Anthropic-style slide tooling

Adopted ideas:
- render the PPTX after generation
- use montage review for deck-level coherence
- keep native PowerPoint objects when editability materially matters
- programmatic overflow/out-of-bounds checks are necessary but not sufficient

## Design-skill registries

References:
- https://github.com/bergside/awesome-design-skills
- https://github.com/VoltAgent/awesome-design-md

Adopted idea:
- separate agent instructions (`SKILL.md`) from reusable design intent (`DESIGN.md`) and brand assets.
