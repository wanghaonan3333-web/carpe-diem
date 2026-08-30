[![](https://docs.openclaw.ai/assets/openclaw.svg)OpenClawDocs](https://docs.openclaw.ai/)

Search...K

🇺🇸English🇺🇸 English🇨🇳 简体中文🇨🇳 繁體中文🇯🇵 日本語🇪🇸 Español🇧🇷 Português (BR)🇰🇷 한국어🇩🇪 Deutsch🇫🇷 Français🇮🇳 हिन्दी🇸🇦 العربية🇮🇹 Italiano🇻🇳 Tiếng Việt🇳🇱 Nederlands🇹🇷 Türkçe🇺🇦 Українська🇮🇩 Bahasa Indonesia🇵🇱 Polski🇷🇺 Русский🇮🇷 فارسی🇹🇭 ไทย

[🇺🇸English✓](https://docs.openclaw.ai/clawhub/skill-format) [🇨🇳简体中文✓](https://docs.openclaw.ai/zh-CN/clawhub/skill-format) [🇨🇳繁體中文✓](https://docs.openclaw.ai/zh-TW/clawhub/skill-format) [🇯🇵日本語✓](https://docs.openclaw.ai/ja-JP/clawhub/skill-format) [🇪🇸Español✓](https://docs.openclaw.ai/es/clawhub/skill-format) [🇧🇷Português (BR)✓](https://docs.openclaw.ai/pt-BR/) [🇰🇷한국어✓](https://docs.openclaw.ai/ko/) [🇩🇪Deutsch✓](https://docs.openclaw.ai/de/clawhub/skill-format) [🇫🇷Français✓](https://docs.openclaw.ai/fr/) [🇮🇳हिन्दी✓](https://docs.openclaw.ai/hi/clawhub/skill-format) [🇸🇦العربية✓](https://docs.openclaw.ai/ar/) [🇮🇹Italiano✓](https://docs.openclaw.ai/it/) [🇻🇳Tiếng Việt✓](https://docs.openclaw.ai/vi/clawhub/skill-format) [🇳🇱Nederlands✓](https://docs.openclaw.ai/nl/clawhub/skill-format) [🇹🇷Türkçe✓](https://docs.openclaw.ai/tr/clawhub/skill-format) [🇺🇦Українська✓](https://docs.openclaw.ai/uk/) [🇮🇩Bahasa Indonesia✓](https://docs.openclaw.ai/id/clawhub/skill-format) [🇵🇱Polski✓](https://docs.openclaw.ai/pl/) [🇷🇺Русский✓](https://docs.openclaw.ai/ru/) [🇮🇷فارسی✓](https://docs.openclaw.ai/fa/clawhub/skill-format) [🇹🇭ไทย✓](https://docs.openclaw.ai/th/clawhub/skill-format)

[GitHub](https://github.com/openclaw/openclaw "GitHub") [Discord](https://discord.com/invite/clawd "Discord")

[Get started](https://docs.openclaw.ai/) [Install](https://docs.openclaw.ai/install) [Channels](https://docs.openclaw.ai/channels) [Agents](https://docs.openclaw.ai/concepts/architecture) [Capabilities](https://docs.openclaw.ai/tools) [ClawHub](https://docs.openclaw.ai/clawhub) [Models](https://docs.openclaw.ai/providers) [Platforms](https://docs.openclaw.ai/platforms) [Gateway & Ops](https://docs.openclaw.ai/gateway) [Reference](https://docs.openclaw.ai/cli) [Release & CI](https://docs.openclaw.ai/releases) [Help](https://docs.openclaw.ai/help)

**Browse docs**

Section **ClawHub**[Get started](https://docs.openclaw.ai/) [Install](https://docs.openclaw.ai/install) [Channels](https://docs.openclaw.ai/channels) [Agents](https://docs.openclaw.ai/concepts/architecture) [Capabilities](https://docs.openclaw.ai/tools) [ClawHub](https://docs.openclaw.ai/clawhub) [Models](https://docs.openclaw.ai/providers) [Platforms](https://docs.openclaw.ai/platforms) [Gateway & Ops](https://docs.openclaw.ai/gateway) [Reference](https://docs.openclaw.ai/cli) [Release & CI](https://docs.openclaw.ai/releases) [Help](https://docs.openclaw.ai/help)

In this section

## Overview

[ClawHub](https://docs.openclaw.ai/clawhub) [Quickstart](https://docs.openclaw.ai/clawhub/quickstart) [How ClawHub Works](https://docs.openclaw.ai/clawhub/how-it-works)

## Using ClawHub

[CLI](https://docs.openclaw.ai/clawhub/cli) [Publishing](https://docs.openclaw.ai/clawhub/publishing) [Skill format](https://docs.openclaw.ai/clawhub/skill-format) [Auth](https://docs.openclaw.ai/clawhub/auth) [Telemetry](https://docs.openclaw.ai/clawhub/telemetry) [Troubleshooting](https://docs.openclaw.ai/clawhub/troubleshooting)

## API and trust

[API v1](https://docs.openclaw.ai/clawhub/api) [HTTP API](https://docs.openclaw.ai/clawhub/http-api) [Acceptable Usage](https://docs.openclaw.ai/clawhub/acceptable-usage) [Moderation and Account Safety](https://docs.openclaw.ai/clawhub/moderation) [Security Audits](https://docs.openclaw.ai/clawhub/security-audits)

[ClawHub](https://docs.openclaw.ai/clawhub)/Using ClawHub/Skill format

Copy page

**Copy page** Copy page as Markdown for LLMs [**View as Markdown** View this page as plain text↗](https://docs.openclaw.ai/clawhub/skill-format.md) [**Open in ChatGPT** Ask questions about this page↗](https://chatgpt.com/?hints=search&q=Read%20from%20https%3A%2F%2Fdocs.openclaw.ai%2Fclawhub%2Fskill-format.md%20so%20I%20can%20ask%20questions%20about%20it.) [**Open in Claude** Ask questions about this page↗](https://claude.ai/new?q=Read%20from%20https%3A%2F%2Fdocs.openclaw.ai%2Fclawhub%2Fskill-format.md%20so%20I%20can%20ask%20questions%20about%20it.)

Using ClawHub

# Skill format

ClawHubUsing ClawHub

# Skill format

## On disk

A skill is a folder.

Required:

- `SKILL.md` (or `skill.md`; legacy `skills.md` is also accepted)

Optional:

- any supporting regular files (see “Skill files”)
- `.clawhubignore` (ignore patterns for publishing, legacy `.clawdhubignore`)
- `.gitignore` (also honored)

## GitHub import

The web GitHub importer is stricter than local publish/sync. It only discovers
`SKILL.md` or legacy `skills.md` files in public, non-fork repositories owned by
the signed-in GitHub account. It does not import private repos, forks,
archived/disabled repos, or third-party public repos.

Local install metadata (written by the CLI):

- `<skill>/.clawhub/origin.json` (legacy `.clawdhub`)

Workdir install state (written by the CLI):

- `<workdir>/.clawhub/lock.json` (legacy `.clawdhub`)

## `SKILL.md`

- Markdown with optional YAML frontmatter.
- The server extracts metadata from frontmatter during publish.
- `description` is used as the skill summary in the UI/search.

For portable Agent Skills, `name` should match the parent directory and use
1–64 lowercase letters, numbers, or hyphens. ClawHub keeps the routable slug and
catalog display name separate, so existing names from other clients remain
publishable and are not silently rewritten. Catalog lists may shorten long names
visually without changing the stored name.

## Frontmatter metadata

Skill metadata is declared in the YAML frontmatter at the top of your `SKILL.md`. This tells the registry (and security analysis) what your skill needs to run.

### Basic frontmatter

yamlCopy code

```yaml
---name: my-skilldescription: Short summary of what this skill does.version: 1.0.0---
```

### Runtime metadata (`metadata.openclaw`)

Declare your skill's runtime requirements under `metadata.openclaw` (aliases: `metadata.clawdbot`, `metadata.clawdis`).

yamlCopy code

```yaml
---name: my-skilldescription: Manage tasks via the Todoist API.metadata:  openclaw:    requires:      env:        - TODOIST_API_KEY      bins:        - curl    primaryEnv: TODOIST_API_KEY---
```

Use `requires.env` for environment variables that must be present before the skill can run. Use `envVars` when you need per-variable metadata, including optional variables with `required: false`.

### Full field reference

| Field | Type | Description |
| --- | --- | --- |
| `requires.env` | `string[]` | Required environment variables your skill expects. |
| `requires.bins` | `string[]` | CLI binaries that must all be installed. |
| `requires.anyBins` | `string[]` | CLI binaries where at least one must exist. |
| `requires.config` | `string[]` | Config file paths your skill reads. |
| `primaryEnv` | `string` | The main credential env var for your skill. |
| `envVars` | `array` | Environment variable declarations with `name`, optional `required`, and optional `description`. Set `required: false` for optional env vars. |
| `always` | `boolean` | If `true`, skill is always active (no explicit install needed). |
| `skillKey` | `string` | Override the skill's invocation key. |
| `emoji` | `string` | Display emoji for the skill. |
| `homepage` | `string` | URL to the skill's homepage or docs. |
| `os` | `string[]` | OS restrictions (e.g. `["macos"]`, `["linux"]`). |
| `install` | `array` | Install specs for dependencies (see below). |
| `nix` | `object` | Nix plugin spec (see README). |
| `config` | `object` | Clawdbot config spec (see README). |

### Install specs

If your skill needs dependencies installed, declare them in the `install` array:

yamlCopy code

```yaml
metadata:  openclaw:    install:      - kind: brew        formula: jq        bins: [jq]      - kind: node        package: typescript        bins: [tsc]
```

Supported install kinds: `brew`, `node`, `go`, `uv`.

### Optional environment variables

Declare optional environment variables under `metadata.openclaw.envVars` and set `required: false`. Do not add optional entries to `requires.env`, because `requires.env` means the skill cannot run without them.

yamlCopy code

```yaml
metadata:  openclaw:    primaryEnv: TODOIST_API_KEY    envVars:      - name: TODOIST_API_KEY        required: true        description: Todoist API token used for authenticated requests.      - name: TODOIST_PROJECT_ID        required: false        description: Optional default project ID when the user does not specify one.
```

### Why this matters

ClawHub's security analysis checks that what your skill declares matches what it actually does. If your code references `TODOIST_API_KEY` but your frontmatter doesn't declare it under `requires.env`, `primaryEnv`, or `envVars`, the analysis will flag a metadata mismatch. Keeping declarations accurate helps your skill pass review and helps users understand what they're installing.

### Example: complete frontmatter

yamlCopy code

```yaml
---name: todoist-clidescription: Manage Todoist tasks, projects, and labels from the command line.version: 1.2.0metadata:  openclaw:    requires:      env:        - TODOIST_API_KEY      bins:        - curl    primaryEnv: TODOIST_API_KEY    envVars:      - name: TODOIST_API_KEY        required: true        description: Todoist API token.      - name: TODOIST_PROJECT_ID        required: false        description: Optional default project ID.    emoji: "\u2705"    homepage: https://github.com/example/todoist-cli---
```

## Skill files

Publish accepts all regular files in the skill folder, regardless of extension. Ignore files,
hidden paths, symlinks, macOS metadata, and server-side size limits still apply.

- Bounded files that contain valid UTF-8 can be previewed as escaped plain text and are included
in bounded text analysis.
- Other files keep their exact bytes and are available to download.
- Security scanners receive the complete stored artifact; text detection is a rendering and
analysis concern, not an upload allowlist.

Limits (server-side):

- Total bundle size: 50MB.
- Embedding text includes `SKILL.md` \+ up to ~40 bounded UTF-8 files (best-effort cap).

## Slugs

- Derived from folder name by default.
- Package scopes must match the ClawHub publisher handle exactly. Publisher handles can use lowercase letters, numbers, hyphens, dots, and underscores; they must start and end with a lowercase letter or number.
- Package slugs must be lowercase and npm-safe, for example `@example.tools/demo-plugin` or `demo-plugin`.

## Versioning + tags

- Each publish creates a new version (semver).
- Tags are string pointers to a version; `latest` is commonly used.

## License

- All skills published on ClawHub are licensed under `MIT-0`.
- Anyone may use, modify, and redistribute published skills, including commercially.
- Attribution is not required.
- Do not add conflicting license terms in `SKILL.md`; ClawHub does not support per-skill license overrides.

## Paid skills

- ClawHub does not support paid skills, per-skill pricing, paywalls, or revenue sharing.
- Do not add pricing metadata to `SKILL.md`; it is not part of the skill format and will not make a published skill paid.
- If your skill integrates with a paid third-party service, document the external cost and required account clearly in the skill instructions and env declarations (`requires.env` for required variables, or `envVars` with `required: false` for optional variables).

Was this useful?YesNo

[Edit source](https://github.com/openclaw/clawhub/edit/main/docs/skill-format.md) [Raise issue](https://github.com/openclaw/openclaw/issues/new?title=Issue%20on%20docs&body=Path%3A%20%2Fclawhub%2Fskill-format)

[Open issue](https://github.com/openclaw/openclaw/issues/new?title=Docs+feedback%3A+%2Fclawhub%2Fskill-format&body=Page%3A+%2Fclawhub%2Fskill-format%0AURL%3A+https%3A%2F%2Fdocs.openclaw.ai%2Fclawhub%2Fskill-format%0A)

[PreviousPublishing](https://docs.openclaw.ai/clawhub/publishing) [NextAuth](https://docs.openclaw.ai/clawhub/auth)On this page

## On this page

[On disk](https://docs.openclaw.ai/clawhub/skill-format#on-disk) [GitHub import](https://docs.openclaw.ai/clawhub/skill-format#github-import) [SKILL.md](https://docs.openclaw.ai/clawhub/skill-format#skill.md) [Frontmatter metadata](https://docs.openclaw.ai/clawhub/skill-format#frontmatter-metadata) [Basic frontmatter](https://docs.openclaw.ai/clawhub/skill-format#basic-frontmatter) [Runtime metadata (metadata.openclaw)](https://docs.openclaw.ai/clawhub/skill-format#runtime-metadata-(metadata.openclaw)) [Full field reference](https://docs.openclaw.ai/clawhub/skill-format#full-field-reference) [Install specs](https://docs.openclaw.ai/clawhub/skill-format#install-specs) [Optional environment variables](https://docs.openclaw.ai/clawhub/skill-format#optional-environment-variables) [Why this matters](https://docs.openclaw.ai/clawhub/skill-format#why-this-matters) [Example: complete frontmatter](https://docs.openclaw.ai/clawhub/skill-format#example%3A-complete-frontmatter) [Skill files](https://docs.openclaw.ai/clawhub/skill-format#skill-files) [Slugs](https://docs.openclaw.ai/clawhub/skill-format#slugs) [Versioning + tags](https://docs.openclaw.ai/clawhub/skill-format#versioning-%2B-tags) [License](https://docs.openclaw.ai/clawhub/skill-format#license) [Paid skills](https://docs.openclaw.ai/clawhub/skill-format#paid-skills)

© 2026 OpenClaw — an [OpenClaw Foundation](https://openclaw.org/) project

[openclaw.ai](https://openclaw.ai/) [openclaw.org](https://openclaw.org/) [Releases](https://github.com/openclaw/openclaw/releases) [GitHub](https://github.com/openclaw/openclaw) [Discord](https://discord.com/invite/clawd)

Install OpenClawSet up TelegramFix GatewayBuild a plugin

![](https://docs.openclaw.ai/assets/molty-avatar.png)Ask Molty

![](https://docs.openclaw.ai/assets/molty-avatar.png)Ask Molty

![](https://docs.openclaw.ai/assets/molty-avatar.png)

## Molty

Responses are generated using AI and may contain mistakes.