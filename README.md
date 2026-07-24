# Manuscript Architect

A specialist agent profile and its companion skill for **Claude Science**, built
to turn a completed drug-program dossier and its artifacts into a bioRxiv-style
preprint, run it through two rounds of synthetic peer review with editor support,
and produce four bundled deliverables.

## What it does

Ingests the artifacts an upstream drug-program (or research) effort has already
produced — dossiers, figures, ranked tables, computational results, briefs — and:

1. Reconstructs the scientific narrative from the artifact store.
2. Drafts a manuscript (Abstract, Intro, Results, Methods, Discussion) with
   figures and supplements.
3. Progresses it through **two rounds** of synthetic peer review, incorporating
   editor and reviewer feedback and tracking every revision.
4. Verifies claims against real sources and never fabricates citations, data, or
   statistics — in-silico / unvalidated results stay flagged as such.

### Four bundled deliverables

1. One-page executive summary of the paper and its impact
2. The manuscript plus supplemental files
3. A peer-review report (editor/reviewer comments across both rounds + revisions)
4. A plain-language lay abstract for non-specialists

It does **not** run the upstream pipeline, nominate targets, or design molecules
— it communicates work already done.

## What's in this repository

```
agent/
  profile.json        # picker metadata + settings (name, description, access)
  system_prompt.md    # the agent's identity / opening system prompt
skills/
  synthetic-peer-review/   # the mock peer-review panel (editor + reviewers,
                           #   multi-round, revision tracking)
export_manifest.json  # index of exported files
install.py            # one-shot installer (run in the Claude Science repl tool)
LICENSE               # MIT
```

The agent is **unrestricted** — it sees the full live Claude Science skill
catalog and all connectors. This repository bundles only the one **personal**
skill it depends on (`synthetic-peer-review`). Its other recommended skills —
`paper-narrative`, `figure-composer`, `figure-style`, `literature-review`,
`pdf-explore` — ship with Claude Science and are loaded from the live catalog at
run time, so they are intentionally not bundled here.

## Install

From a Claude Science conversation, in the **`repl`** tool, from the root of a
clone of this repository:

```python
exec(open("install.py").read())
```

The installer is idempotent (safe to re-run; it updates in place). It publishes
the bundled skill and creates/updates the `MANUSCRIPT_ARCHITECT` agent. It then
prints the one tool call to create the analysis environment — Python 3.13 with
matplotlib, seaborn, numpy, pandas, pillow, python-docx, reportlab, pypdf,
requests — which you run separately since environment creation is a tool, not
part of the SDK.

## Integrity & safety

- Every quantitative claim traces to an upstream artifact or a retrieved source;
  no fabricated citations, data, or statistics.
- In-silico / unvalidated results stay flagged as such; a paper's framing matches
  the strength of its evidence.
- If upstream artifacts are missing or ambiguous, the agent says so rather than
  inventing content.

## License

MIT — see [LICENSE](LICENSE).
