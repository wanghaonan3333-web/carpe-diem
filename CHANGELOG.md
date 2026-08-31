# Changelog

All notable changes to Carpe Diem are documented here.

## v0.3.0 — 2026-08-31

### Added

- 22 evidence-backed behavior cards across validation, collaboration, product, engineering, and anti-pattern topics.
- A research-layer evidence register with source type, provenance, uncertainty, and verification status.
- Routing acceptance cases, overlap checks, and single-writer integration guidance for future distillation.

### Changed

- Runtime routing now uses the current stage as a candidate filter and loads at most one primary card plus one supporting card from concrete user signals.
- Pricing, Go/No-Go, API, security, code review, observability, technical debt, and async communication cards now avoid unsupported universal thresholds and high-risk wording.
- Documentation now separates research provenance from the runtime voice shown to users.

### Security

- The installer no longer downloads and executes remote code through a pipe-to-shell path.
- Installation guidance is local-first and keeps the reviewable plan and explicit approval step visible.

## v0.2.0 — 2026-08-30

- Added the first 33-card wisdom distillation library across Discover, Validate, Plan, Track, and cross-stage guidance.
- Added the research → plan → implement → integrate distillation workflow.
- Added stage-aware loading and manifest coverage for the wisdom cards.

## v0.1.1 — 2026-08-31

- Hardened installer path validation.
- Completed lifecycle recovery rules and scoped session authorization reuse.
- Improved bilingual discovery and responses.

## v0.1.0 — 2026-08-27

- Initial public release of the local-first Carpe Diem Agent Skill.
