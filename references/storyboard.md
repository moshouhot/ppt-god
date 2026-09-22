# Storyboard IR

Use the storyboard as the contract between content reasoning and visual design.

## Required fields

Each slide object must include:

- `slide`: 1-based order
- `role`: cover | toc | section | thesis | evidence | comparison | process | timeline | data | quote | demo | case-study | roadmap | ask | appendix | sources | thanks
- `title`: presentation title for the slide; make it conclusion-led when possible
- `message`: one-sentence takeaway the audience should remember
- `content`: concise semantic content, not final layout instructions
- `visual_intent`: hero-number | editorial | full-bleed-image | comparison | timeline | process | matrix | diagram | chart | table | quote | gallery | split | minimal
- `importance`: low | normal | high | hero
- `editability`: E1 | E2 | E3
- `asset_requirements`: list of objects describing needed visual assets

Optional fields:
- `source_refs`
- `speaker_note`
- `data`
- `brand_constraints`
- `layout_hint`

## Rules

1. One slide = one dominant message.
2. Titles should say the point, not merely the topic, unless the slide is a cover/section divider.
3. A slide with more than 3 independent messages probably needs to split.
4. Use `hero` importance sparingly; normally 10-25% of a deck.
5. Do not select a chart type until the data relationship is understood.
6. Asset requirements must be explicit enough to search or generate intentionally.
7. Avoid repeating the same `visual_intent` more than 2-3 slides in a row unless the deck is intentionally systematic.
