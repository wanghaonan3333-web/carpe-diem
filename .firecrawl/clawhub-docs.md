[![](https://docs.openclaw.ai/assets/openclaw.svg)OpenClawDocs](https://docs.openclaw.ai/)

Search...K

🇺🇸English🇺🇸 English🇨🇳 简体中文🇨🇳 繁體中文🇯🇵 日本語🇪🇸 Español🇧🇷 Português (BR)🇰🇷 한국어🇩🇪 Deutsch🇫🇷 Français🇮🇳 हिन्दी🇸🇦 العربية🇮🇹 Italiano🇻🇳 Tiếng Việt🇳🇱 Nederlands🇹🇷 Türkçe🇺🇦 Українська🇮🇩 Bahasa Indonesia🇵🇱 Polski🇷🇺 Русский🇮🇷 فارسی🇹🇭 ไทย

[🇺🇸English✓](https://docs.openclaw.ai/clawhub) [🇨🇳简体中文✓](https://docs.openclaw.ai/zh-CN/clawhub) [🇨🇳繁體中文✓](https://docs.openclaw.ai/zh-TW/clawhub) [🇯🇵日本語✓](https://docs.openclaw.ai/ja-JP/clawhub) [🇪🇸Español✓](https://docs.openclaw.ai/es/clawhub) [🇧🇷Português (BR)✓](https://docs.openclaw.ai/pt-BR/) [🇰🇷한국어✓](https://docs.openclaw.ai/ko/) [🇩🇪Deutsch✓](https://docs.openclaw.ai/de/clawhub) [🇫🇷Français✓](https://docs.openclaw.ai/fr/) [🇮🇳हिन्दी✓](https://docs.openclaw.ai/hi/clawhub) [🇸🇦العربية✓](https://docs.openclaw.ai/ar/) [🇮🇹Italiano✓](https://docs.openclaw.ai/it/) [🇻🇳Tiếng Việt✓](https://docs.openclaw.ai/vi/clawhub) [🇳🇱Nederlands✓](https://docs.openclaw.ai/nl/clawhub) [🇹🇷Türkçe✓](https://docs.openclaw.ai/tr/clawhub) [🇺🇦Українська✓](https://docs.openclaw.ai/uk/) [🇮🇩Bahasa Indonesia✓](https://docs.openclaw.ai/id/clawhub) [🇵🇱Polski✓](https://docs.openclaw.ai/pl/) [🇷🇺Русский✓](https://docs.openclaw.ai/ru/) [🇮🇷فارسی✓](https://docs.openclaw.ai/fa/clawhub) [🇹🇭ไทย✓](https://docs.openclaw.ai/th/clawhub)

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

[ClawHub](https://docs.openclaw.ai/clawhub)/Overview/ClawHub

Copy page

**Copy page** Copy page as Markdown for LLMs [**View as Markdown** View this page as plain text↗](https://docs.openclaw.ai/clawhub.md) [**Open in ChatGPT** Ask questions about this page↗](https://chatgpt.com/?hints=search&q=Read%20from%20https%3A%2F%2Fdocs.openclaw.ai%2Fclawhub.md%20so%20I%20can%20ask%20questions%20about%20it.) [**Open in Claude** Ask questions about this page↗](https://claude.ai/new?q=Read%20from%20https%3A%2F%2Fdocs.openclaw.ai%2Fclawhub.md%20so%20I%20can%20ask%20questions%20about%20it.)

Overview

# ClawHub

ClawHubOverview

# ClawHub

ClawHub is the public registry for OpenClaw skills and plugins.

- Use native `openclaw` commands to search, install, and update skills and to install plugins from ClawHub.
- Use the separate `clawhub` CLI for registry auth, publishing, and delete/undelete workflows.

Site: [clawhub.ai](https://clawhub.ai/)

## Quick start

Search and install skills with OpenClaw:

bashCopy code

```bash
openclaw skills search "calendar"openclaw skills install @openclaw/demoopenclaw skills update --all
```

Search and install plugins with OpenClaw:

bashCopy code

```bash
openclaw plugins search "calendar"openclaw plugins install clawhub:<package>openclaw plugins update --all
```

Install the ClawHub CLI when you want registry-authenticated workflows such as
publish or delete/undelete:

bashCopy code

```bash
npm i -g clawhub# orpnpm add -g clawhub
```

## What ClawHub hosts

| Surface | What it stores | Typical command |
| --- | --- | --- |
| Skills | Versioned text bundles with `SKILL.md` plus supporting files | `openclaw skills install @openclaw/demo` |
| Code plugins | OpenClaw plugin packages with compatibility metadata | `openclaw plugins install clawhub:<package>` |
| Bundle plugins | Packaged plugin bundles for OpenClaw distribution | `clawhub package publish <source>` |

ClawHub tracks semver versions, tags such as `latest`, changelogs, files,
downloads, stars, and security scan summaries. Public pages show current registry
state so users can inspect a skill or plugin before installing it.

## Native OpenClaw flows

Native OpenClaw commands install into the active OpenClaw workspace and persist
source metadata so later update commands can stay on ClawHub.

Use `clawhub:<package>` when a plugin install should resolve through ClawHub.
Bare npm-safe plugin specs may resolve through npm during launch cutovers, and
`npm:<package>` stays npm-only when a source must be explicit.

Plugin installs validate advertised `pluginApi` and `minGatewayVersion`
compatibility before archive install runs. When a package version publishes a
ClawPack artifact, OpenClaw prefers the exact uploaded npm-pack `.tgz`, verifies
the ClawHub digest header and downloaded bytes, and records artifact metadata for
later updates.

## ClawHub CLI

The ClawHub CLI is for registry-authenticated work:

bashCopy code

```bash
clawhub loginclawhub whoamiclawhub search "postgres backups"clawhub skill publish ./my-skill --slug my-skill --name "My Skill" --version 1.0.0clawhub package explore --family code-pluginclawhub package inspect episodic-clawclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
```

The CLI also has skill install/update commands for direct registry workflows:

bashCopy code

```bash
clawhub install @openclaw/democlawhub update @openclaw/democlawhub update --allclawhub list
```

Those commands install skills into `./skills` under the current working directory
and record installed versions in `.clawhub/lock.json`.

## Publishing

Publish skills from a local folder containing `SKILL.md`:

bashCopy code

```bash
clawhub skill publish <path>
```

Common publish options:

- `--slug <slug>`: published skill URL name.
- `--name <name>`: display name.
- `--version <version>`: semver version.
- `--changelog <text>`: changelog text.
- `--tags <tags>`: comma-separated tags, defaulting to `latest`.

Publish plugins from a local folder, `owner/repo`, `owner/repo@ref`, or a GitHub
URL:

bashCopy code

```bash
clawhub package publish <source>
```

Use `--dry-run` to build the exact publish plan without uploading, and `--json`
for CI-friendly output.

Code plugins must include the required OpenClaw compatibility metadata in
`package.json`, including `openclaw.compat.pluginApi` and
`openclaw.build.openclawVersion`. See [CLI](https://docs.openclaw.ai/clawhub/cli) for the full command
reference and [Skill format](https://docs.openclaw.ai/clawhub/skill-format) for skill metadata.

## Security and moderation

ClawHub is open by default: anyone can upload, but publishing requires a GitHub
account old enough to pass the upload gate. Public detail pages summarize the
latest scan state before install or download.

ClawHub runs automated checks on published skills and plugin releases. Scan-held
or blocked releases may disappear from public catalog and install surfaces while
remaining visible to their owner in `/dashboard`.

Signed-in users can report skills and packages. Moderators can review reports,
hide or restore content, and ban abusive accounts. See
[Security](https://docs.openclaw.ai/clawhub/security),
[Security Audits](https://docs.openclaw.ai/clawhub/security-audits),
[Moderation and Account Safety](https://docs.openclaw.ai/clawhub/moderation), and
[Acceptable usage](https://docs.openclaw.ai/clawhub/acceptable-usage) for policy and enforcement details.

## Telemetry and environment

When you run `clawhub install` while logged in, the CLI may send a best-effort
install event so ClawHub can compute aggregate install counts. Disable this with:

bashCopy code

```bash
export CLAWHUB_DISABLE_TELEMETRY=1
```

Useful environment overrides:

| Variable | Effect |
| --- | --- |
| `CLAWHUB_SITE` | Override the site URL used for browser login. |
| `CLAWHUB_REGISTRY` | Override the registry API URL. |
| `CLAWHUB_CONFIG_PATH` | Override where the CLI stores token/config state. |
| `CLAWHUB_WORKDIR` | Override the default working directory. |
| `CLAWHUB_DISABLE_TELEMETRY=1` | Disable install telemetry. |

See [Telemetry](https://docs.openclaw.ai/clawhub/telemetry), [HTTP API](https://docs.openclaw.ai/clawhub/http-api), and
[Troubleshooting](https://docs.openclaw.ai/clawhub/troubleshooting) for deeper reference material.

Was this useful?YesNo

[Edit source](https://github.com/openclaw/clawhub/edit/main/docs/clawhub.md) [Raise issue](https://github.com/openclaw/openclaw/issues/new?title=Issue%20on%20docs&body=Path%3A%20%2Fclawhub)

[Open issue](https://github.com/openclaw/openclaw/issues/new?title=Docs+feedback%3A+%2Fclawhub&body=Page%3A+%2Fclawhub%0AURL%3A+https%3A%2F%2Fdocs.openclaw.ai%2Fclawhub%0A)

[PreviousMulti-agent sandbox and tools](https://docs.openclaw.ai/tools/multi-agent-sandbox-tools) [NextQuickstart](https://docs.openclaw.ai/clawhub/quickstart)On this page

## On this page

[Quick start](https://docs.openclaw.ai/clawhub#quick-start) [What ClawHub hosts](https://docs.openclaw.ai/clawhub#what-clawhub-hosts) [Native OpenClaw flows](https://docs.openclaw.ai/clawhub#native-openclaw-flows) [ClawHub CLI](https://docs.openclaw.ai/clawhub#clawhub-cli) [Publishing](https://docs.openclaw.ai/clawhub#publishing) [Security and moderation](https://docs.openclaw.ai/clawhub#security-and-moderation) [Telemetry and environment](https://docs.openclaw.ai/clawhub#telemetry-and-environment)

© 2026 OpenClaw — an [OpenClaw Foundation](https://openclaw.org/) project

[openclaw.ai](https://openclaw.ai/) [openclaw.org](https://openclaw.org/) [Releases](https://github.com/openclaw/openclaw/releases) [GitHub](https://github.com/openclaw/openclaw) [Discord](https://discord.com/invite/clawd)

Install OpenClawSet up TelegramFix GatewayBuild a plugin

![](https://docs.openclaw.ai/assets/molty-avatar.png)Ask Molty

![](https://docs.openclaw.ai/assets/molty-avatar.png)Ask Molty

![](https://docs.openclaw.ai/assets/molty-avatar.png)

## Molty

Responses are generated using AI and may contain mistakes.