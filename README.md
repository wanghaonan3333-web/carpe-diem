# Carpe Diem

English | [简体中文](README.zh-CN.md)

> You have a Coding Agent. Now, what is actually worth building?

An open-source Agent Skill for developers and creators, Carpe Diem is designed for people who have access to powerful Coding Agents but do not yet know what project is worth starting. Inside Codex, Claude Code, Cursor, or OpenClaw, it acts as a project ignition mentor and, once a direction is chosen, a thoughtful co-founder.

It does not ship its own model, and it is not a random idea generator. It uses the reasoning and research capabilities of your current Agent, stores only the context you approve in local files, and helps turn uncertainty into a validated direction and a complete implementation plan. Once that plan is approved, Carpe Diem stops being a builder: future sessions only track progress through read-only evidence.

Carpe Diem is an early public release, and real-world feedback is still valuable: tell us what helped, what felt confusing, and where the guidance lost the thread.

Current release: `v0.3.0`. The wisdom library now includes 55 behavior cards. Runtime routing treats a stage as a candidate filter and loads at most one primary plus one supporting card from concrete user signals; the contributor workflow now separates runtime voice from research provenance and requires evidence, deduplication, scenario testing, and a single-writer integration step.

## What's new in v0.3.0

- Added 22 evidence-backed behavior cards across validation, collaboration, product, engineering, and anti-pattern topics.
- Replaced stage-wide card loading with bounded one-primary/one-support routing driven by concrete user signals.
- Added an evidence register, overlap checks, scenario acceptance cases, and single-writer integration guidance for future distillation.
- Hardened local installation guidance and removed remote pipe-to-shell execution from the installer.

See the full history in [CHANGELOG.md](CHANGELOG.md).

## What it does

Carpe Diem turns “I do not know what to build” into four stages:

1. **Discover** — Find opportunities in recurring friction, existing skills, genuine interests, and unfinished assets instead of producing a list of generic ideas.
2. **Validate** — Investigate competitors, substitutes, demand signals, and reasons the idea may fail. It never claims an idea is original without evidence.
3. **Plan** — Work through a complete implementation plan and a concise handoff package, one section at a time.
4. **Track** — After development begins, inspect Git and existing test or CI evidence in read-only mode, record progress and deviations, and recommend the next step.

## A typical first conversation

```text
You: I have a Coding Agent, but I have no idea what to build.

Carpe Diem: You do not need to force yourself to invent a “great idea.” Projects worth
building are usually hidden in recurring friction, abilities you have not yet turned into
a product, unfinished assets, or needs that only recently became possible to address.
I will first build an opportunity map from this conversation. If the evidence is too thin,
you can then decide whether to grant read-only access to a specific local folder or GitHub
scope. I will not inspect anything else without your permission.
```

Carpe Diem gives its judgment and reasoning first. It asks for one decision only when guessing incorrectly would create real rework.

## Installation

Carpe Diem requires Python 3.10+ and uses only the standard library. Clone or download the repository, then run from its root:

```bash
python3 scripts/carpe_diem.py install detect
python3 scripts/carpe_diem.py install plan --platform codex --json > /tmp/carpe-diem-install.json
```

Review the target, version, file list, and fingerprint in the generated plan. Approve it once you are satisfied:

```bash
python3 scripts/carpe_diem.py install apply --plan /tmp/carpe-diem-install.json --yes
python3 scripts/carpe_diem.py install verify --target ~/.codex/skills/carpe-diem
```

For another host, replace `codex` with `claude-code`, `cursor`, or `openclaw`. Platform-specific notes are available for:

- [Codex](adapters/codex/INSTALL.md)
- [Claude Code](adapters/claude-code/INSTALL.md)
- [Cursor](adapters/cursor/INSTALL.md)
- [OpenClaw](adapters/openclaw/INSTALL.md)

The installer never overwrites an existing directory. Safe uninstall only removes a receipt-backed snapshot that has not been modified since installation.

## Usage

Start a new Agent conversation and speak naturally:

- “I want to build an open-source project, but I have no direction.”
- “I have three ideas. Help me decide which one is worth validating.”
- “Continue refining the project plan from last time.”
- “Compare the current project progress with the approved plan.”

You can interrupt, disagree, or ask for evidence at any time. Carpe Diem answers the interruption and then returns to the saved thread of work.

## Local memory and privacy

Carpe Diem uses two separate layers of local memory:

- Personal profile: `~/.carpe-diem/profiles/me.json`
- Project state: `.carpe-diem/` inside the project directory

The long-term profile stores only concise facts you explicitly approve. Agent inferences are presented as candidates before they can affect future recommendations. Before reading a local directory, GitHub scope, note, issue, or CI result, the Skill must explain the purpose, exact target, and read-only scope and obtain permission. Portable exports remove absolute local paths.

Project-level `.carpe-diem/` state is intended to stay local. Carpe Diem will not silently modify your `.gitignore`.

## Explicit boundaries

Carpe Diem can research, challenge assumptions, plan, prepare a development handoff, and track evidence. It does not:

- write or modify project business code;
- fix bugs or execute the implementation plan;
- automatically commit, push, or modify issues;
- inspect additional context without permission;
- bundle a model, background service, or model API key.

## Compatibility status

All four hosts use the same Skill methodology and local state protocol. In `v0.3.0`, the 55-card wisdom library, deterministic helpers, routing cases, and all four installation targets are covered by automated tests. User-level discovery and three isolated behavior scenarios have been verified with Codex CLI `0.150.0-alpha.8`.

For Claude Code, Cursor, and OpenClaw, the documented Skill locations and installation snapshots are verified, but real host invocation still needs testing. The [internal testing record](docs/internal-testing.md) deliberately separates confirmed behavior from inferred compatibility.

## Local verification

```bash
python3 -m compileall -q scripts tests
python3 -m unittest discover -s tests -v
python3 scripts/carpe_diem.py doctor --source . --json
git diff --check
```

## Changelog

### v0.3.0 — 2026-08-31

- Added 22 candidate behavior cards across validation, collaboration, product, engineering, and anti-pattern topics.
- Replaced stage-wide auto-loading with a two-card context budget and explicit trigger routing.
- Added a research-layer evidence register, overlap gates, scenario acceptance tests, and single-writer integration guidance.
- Corrected unsupported universal thresholds and high-risk guidance in pricing, Go/No-Go, API, security, code review, observability, technical debt, and async communication cards.

### v0.2.0 — 2026-08-30

**Wisdom Distillation System — 33 behavior cards across all stages**

This major update completes the wisdom distillation work, embedding 24 thought leaders' and 16 engineering case studies' actionable insights into Carpe Diem's four-stage flow.

**New for users:**
- Carpe Diem now dynamically loads behavior cards based on which stage you're in and what you say — when you mention "a lot of people say this is a good idea", it will load the Mom Test card and guide you to distinguish genuine signals from polite praise, without you needing to know the card exists
- The same applies across all four stages: Discover (5 cards), Validate (4), Plan (9), Track (9), plus 6 cross-stage cards that apply regardless of stage
- Each card provides 5-6 concrete, actionable steps you can execute in 3-5 conversation turns

**New for contributors:**
- A complete distillation pipeline (research → plan → implement → integrate) documented in `docs/wisdom-distillation-guide.md`
- Clear three-iron-rules: no source names exposed, no abstract concepts, actionable steps only
- The `manifest.json` now includes all wisdom cards, so `bash install.sh` deploys them correctly

### v0.1.1 — 2026-08-31

Hardens installer path validation, completes lifecycle recovery rules, scopes session authorization reuse, and improves bilingual discovery and responses.

## Feedback and contributions

Feedback is especially valuable. Please open an issue with:

- the moment Carpe Diem genuinely helped you make progress;
- a conversation where its guidance became generic, repetitive, or confusing;
- an unsupported host or installation problem;
- a case where memory, authorization, planning, or read-only tracking behaved unexpectedly.

Reproducible guidance failures and real cross-Agent compatibility evidence are particularly welcome. Before contributing code, read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

[Apache License 2.0](LICENSE)
