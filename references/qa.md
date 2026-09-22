# QA rubric

Quality assurance is mandatory. The exported PPTX, not only the HTML source, is the final truth.

## Content QA

Check:
- story arc is coherent
- no major source claim is dropped accidentally
- numbers/units are consistent
- each slide title/message agrees with its evidence
- charts communicate the intended relationship
- sources/attribution are retained where required

## Page QA

Check every slide for:
- clipped or overflowing text
- text smaller than intended
- overlap and unintended collisions
- poor crop/focal point
- weak contrast
- unbalanced whitespace
- off-grid alignment
- excessive information density

## Deck QA

Inspect a montage and check:
- coherent visual language
- enough compositional variation
- no unexplained one-off styles
- hero slides stand out
- section rhythm is visible
- repeated pages do not feel templated to death
- brand chrome stays consistent in Brand mode

## Conversion QA

Compare HTML render to PPTX render for:
- line-wrap drift
- font substitution
- missing SVG/canvas effects
- altered backgrounds
- shifted editable text overlays
- unexpected page margins

## Severity

- **P0**: corrupted/unopenable deck, missing page, major off-canvas content, unreadable slide
- **P1**: obvious overlap, clipped headline, broken brand shell, wrong key number, missing visual
- **P2**: polish issue such as weak spacing, minor visual inconsistency, non-ideal crop

Never ship with P0/P1 findings. Repair P2 when it materially affects perceived quality.
