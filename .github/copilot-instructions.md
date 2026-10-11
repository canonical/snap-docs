<!-- Copilot / AI instructions for contributors working on this repository -->
# AI assistant guidance for `snap-docs`

This file contains short, concrete guidance for AI coding agents working in this repository. Keep instructions specific to the repository and reference real files/commands.

## Quick context
- Project: documentation built with Sphinx (MyST/Markdown + some reST).
- Key directories: `docs/` (content), `docs/_dev/` (style/config helpers), `.github/workflows/` (CI).
- Primary build: virtualenv at `docs/.venv` created by `make install` from the repo root.

## Most useful commands (examples)
- Create venv & install deps: `make install` (from repo root).
- Live preview while editing: `make run` — serves at `127.0.0.1:8000` using `sphinx-autobuild`.
- Single build for review: `make html`.
- Run link checker: `make linkcheck`.
- Run Vale inclusive-language/style checks: `make vale` or `make woke` (see `docs/Makefile`).
- Accessibility checks (pa11y): `make pa11y` (requires `make pa11y-install` first or let the Makefile install it).
- To reproduce CI dependency build: `make install PIPOPTS="--no-binary :all:"` (used in `.github/workflows/sphinx-python-dependency-build-checks.yml`).

## CI behavior to keep in mind
- CI runs defined in `.github/workflows/` — notable files:
  - `automatic-doc-checks.yml` (uses `canonical/documentation-workflows` for docs checks),
  - `markdown-style-checks.yml` (markdownlint),
  - `sphinx-python-dependency-build-checks.yml` (verifies building venv from source).
- Workflows are triggered on changes under `docs/**` (and on pushes to `main`). Keep PRs focused to docs paths to avoid unnecessary CI runs.

## Codebase patterns & conventions (concrete)
- Content is mostly MyST Markdown with some reST snippets. Files and section roots commonly use `index.md` per directory (e.g. `docs/how-to-guides/*/index.md`).
- Cross-references use relative paths and in-repo links such as `/reference/operations/data-locations` and heading anchors.
- `docs/conf.py` enables `canonical_sphinx` — treat it as authoritative for template/theme behavior and site variables like `html_context`.
- Reusable content may be included via `rst_epilog` and `reuse/substitutions.yaml` (if present). Check `docs/conf.py` before making global substitutions.

## Files to check/read when changing behavior or styling
- `docs/conf.py` — Sphinx configuration and extensions (canonical_sphinx, myst, intersphinx).
- `docs/Makefile` — canonical make targets and environment expectations (venv location, PIPOPTS usage).
- `docs/_dev/.pymarkdown.json` — Markdown lint configuration.
- `docs/_dev/pa11y.json` — accessibility checker configuration.
- `.github/workflows/*` — CI entrypoints and special flags (e.g. docs-only triggers).

## How to propose edits (recommended checklist)
1. Run `make run` locally and visually confirm layout and link changes.
2. Run `make linkcheck` and `make vale` to catch link/style issues early.
3. Check `docs/_dev/*` for project-specific lint/spell rules and adhere to them.
4. Push a branch and open a PR; CI will validate markdown style and Sphinx build on `docs/**` changes.

## Examples from this repo (quick references)
- Sample doc page: `docs/how-to-guides/manage-snaps/create-data-snapshots.md` — shows MyST usage, code blocks, admonitions, and internal links.
- Sphinx build settings: see `docs/conf.py` (uses `canonical_sphinx` and sets `repo_default_branch = 'main'`).

If anything in these instructions is unclear or you want more detail about a specific workflow (for example, building PDFs or running the dependency-heavy CI path), tell me which area to expand. 
