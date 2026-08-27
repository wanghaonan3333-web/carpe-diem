# Carpe Diem

English | [简体中文](README.zh-CN.md)

> You have a Coding Agent. Now, what is actually worth building?

An open-source Agent Skill for developers and creators, Carpe Diem is designed for people who have access to powerful Coding Agents but do not yet know what project is worth starting. Inside Codex, Claude Code, Cursor, or OpenClaw, it acts as a project ignition mentor and, once a direction is chosen, a thoughtful co-founder.

It does not ship its own model, and it is not a random idea generator. It uses the reasoning and research capabilities of your current Agent, stores only the context you approve in local files, and helps turn uncertainty into a validated direction and a complete implementation plan. Once that plan is approved, Carpe Diem stops being a builder: future sessions only track progress through read-only evidence.

This is the first `v0.1` release. We are still testing the central hypothesis: can Carpe Diem genuinely help someone move from “I have an Agent” to “I have started a project worth pursuing”? We would love thoughtful, constructive, and candid feedback—what actually helped, what felt confusing, and where the guidance lost the thread. Every real-world story will help shape the next version.

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

All four hosts use the same Skill methodology and local state protocol. In `v0.1`, structure, deterministic helpers, and all four installation targets are covered by automated tests. User-level discovery and three isolated behavior scenarios have been verified with Codex CLI `0.150.0-alpha.8`.

For Claude Code, Cursor, and OpenClaw, the documented Skill locations and installation snapshots are verified, but real host invocation still needs testing. The [internal testing record](docs/internal-testing.md) deliberately separates confirmed behavior from inferred compatibility.

## Local verification

```bash
python3 -m compileall -q scripts tests
python3 -m unittest discover -s tests -v
python3 scripts/carpe_diem.py doctor --source . --json
git diff --check
```

## Feedback and contributions

Because this is the first release, feedback is especially valuable. Please open an issue with:

- the moment Carpe Diem genuinely helped you make progress;
- a conversation where its guidance became generic, repetitive, or confusing;
- an unsupported host or installation problem;
- a case where memory, authorization, planning, or read-only tracking behaved unexpectedly.

Reproducible guidance failures and real cross-Agent compatibility evidence are particularly welcome. Before contributing code, read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

[Apache License 2.0](LICENSE)
