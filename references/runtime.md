# Runtime preflight

The skill itself is file-based and portable. Deterministic helper scripts expect:

- Python 3.10+
- `python-pptx`
- `Pillow`
- `weasyprint`
- `pdftoppm` (Poppler) for PNG rendering
- LibreOffice/`soffice` for rendering final PPTX

Install Python dependencies from `scripts/requirements.txt` if needed.

OpenDesign is optional but preferred as the design engine. Its desktop GUI is not required; use any available agent/CLI/skill integration.

## Static-export constraint

The bundled HTML renderer/exporter is intentionally static. Before export, flatten JavaScript/canvas/WebGL-only visuals to static SVG/PNG/CSS. This is appropriate for PPTX because animations and interactive runtime effects do not survive ordinary PowerPoint export reliably.

## Failure behavior

- If HTML rendering dependencies are unavailable, use OpenDesign's own render/export path when available.
- If PPTX rendering dependencies are unavailable, do not claim final QA passed. Report that the final PowerPoint render could not be verified.
- Do not silently skip render-based QA.
