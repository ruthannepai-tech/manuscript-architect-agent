# Manuscript Architect — Claude Science specialist agent

A portable definition of the **Manuscript Architect** specialist profile for
[Claude Science](https://www.anthropic.com). It turns a completed drug-program
dossier and its artifacts into a bioRxiv-style preprint, runs it through two
rounds of synthetic peer review with editor support, and produces four bundled
deliverables.

## What it does

Ingests the artifacts an upstream drug-program (or research) effort has already
produced — dossiers, figures, ranked tables, computational results, briefs —
and:

1. Reconstructs the scientific narrative from the artifact store.
2. Drafts a manuscript (Abstract, Intro, Results, Methods, Discussion) with
   figures and supplements.
3. Progresses it through **two rounds** of synthetic peer review, incorporating
   editor and reviewer feedback and tracking every revision.
4. Verifies claims against real sources and never fabricates citations, data,
   or statistics — in-silico / unvalidated results stay flagged as such.

### Four bundled deliverables

1. One-page executive summary of the paper and its impact
2. The manuscript plus supplemental files
3. A peer-review report (editor/reviewer comments across both rounds + revisions)
4. A plain-language lay abstract for non-specialists

It does **not** run the upstream pipeline, nominate targets, or design molecules
— it communicates work already done.

## Contents

| File | Purpose |
|---|---|
| `profile.json` | Portable profile definition (identity, metadata, access, recommended skills + env) |
| `system_prompt.md` | Human-readable system prompt / identity |
| `recreate.py` | Helper to recreate the profile in a Claude Science workspace |

## Recreating the agent

In a Claude Science session, from the `repl` tool:

```python
exec(open("recreate.py").read())
recreate(host)
```

This creates the profile with **full access** (live skill catalog + all
connectors). Then build its environment from
`profile.json["recommended_env"]` and switch to it with
`host.agents.switch("MANUSCRIPT_ARCHITECT")`.

### Recommended skills

`synthetic-peer-review`, `paper-narrative`, `figure-composer`, `figure-style`,
`literature-review`, `pdf-explore`.

### Recommended environment

Python 3.13 with: matplotlib, seaborn, numpy, pandas, pillow, python-docx,
reportlab, pypdf, requests, pandoc, texlive-core (conda-forge).

## License

MIT
