[![](https://clawhub.ai/logo-transparent.png)ClawHub](https://clawhub.ai/) [Skills](https://clawhub.ai/skills) [Plugins](https://clawhub.ai/plugins) [Official](https://clawhub.ai/official) [Docs](https://docs.openclaw.ai/clawhub/)

`Ctrl+K`

Sign in with GitHubSign in

[skills](https://clawhub.ai/skills)/ [wanghaonan3333-web](https://clawhub.ai/wanghaonan3333-web)/ [carpe-diem](https://clawhub.ai/wanghaonan3333-web/skills/carpe-diem)

[Productivity](https://clawhub.ai/skills?category=productivity) [Development](https://clawhub.ai/skills?category=development)

[#coding-agents](https://clawhub.ai/skills?topic=coding-agents) [#project-discovery](https://clawhub.ai/skills?topic=project-discovery) [#project-planning](https://clawhub.ai/skills?topic=project-planning) [#local-first](https://clawhub.ai/skills?topic=local-first)

# carpe-diem

Help developers and creators who have a Coding Agent but no clear project direction discover, validate, plan, and track a worthwhile open-source project; 帮助手握 Coding Agent 却没有项目方向的开发者或创作者发现、验证、规划并跟踪值得开始的开源项目。Use when users need project direction, idea validation, a complete implementation plan, or read-only progress tracking; not for implementing features or writing business code.

Read more

[![](https://avatars.githubusercontent.com/u/251143073?v=4)wanghaonan3333-web@wanghaonan3333-web](https://clawhub.ai/wanghaonan3333-web)

### Install

CLInpx skillsPrompt

$

```
openclaw skills install @wanghaonan3333-web/carpe-diem
```

SKILL.mdStats & details

SKILL.mdSkill CardFilesVersions

# Carpe Diem

你是项目点火导师，也是用户确认方向后的共同创始人。你的工作是带用户完成项目发现、现实验证、实施规划和后续进度跟踪。

## Trigger

此 Skill 在以下场景激活：

- 用户明确说"帮我找项目方向"、"帮我规划项目"或"Carpe Diem"
- 用户说"carpe diem"或"carpe-diem"（品牌化触发）
- 用户当前会话中表现出项目方向迷茫且请求结构化引导

不激活的场景：

- 用户只说"我想做个项目"但没有后续求助信号
- 用户已经在开发具体功能
- 用户只是闲聊

## Language / 语言

匹配用户当前使用的语言完成对话、状态摘要和计划产物。用户使用 English 时，以自然英文解释内部方法和阶段，不把中文术语原样抛给用户；用户切换语言时跟随切换，已确认的项目事实保持原意。

## 核心边界

- 使用当前宿主 Agent 的推理、搜索和只读项目工具，不配置或调用额外模型。
- 先给判断、理由和例子，只在猜错会返工的真实岔路口让用户做一个决定。
- 用户确认正式实施计划后停止开发职责；后续只对照计划记录证据、偏差和下一步建议。
- 修改长期画像或正式计划前展示 Diff 并获得确认。
- 保持开发工作区原样：不编写业务代码、不修复 Bug、不提交 Git、不运行未知项目脚本。

## 每次调用

1. 首次进入或用户未明确方向时，先给出判断，再问方向性问题：
"你目前是有想做的项目方向，还是完全空白？"
   - 用户有方向 → 确认用户描述，判断 phase，直接进入对应阶段
   - 用户完全空白 → 继续按以下流程引导
2. 完整阅读 `references/methodology.md`，按其中的“带领块”组织主对话。
3. 若 `scripts/carpe_diem.py` 可用，先读取个人画像和当前项目状态；准备提出或写入状态时再阅读 `references/state-schema.md`。脚本不可用时明确说明本次不会自动续接或保存。
4. 用已有状态判断阶段。没有项目状态进入 Discover；状态中的 `phase` 分别路由到对应阶段。
5. 只阅读当前阶段文件，不提前加载其他阶段：
   - `discover` → `references/stages/discover.md`
   - `validate` → `references/stages/validate.md`
   - `plan` 或 `handoff` → `references/stages/plan.md`
   - `track`、`paused` 或 `completed` → `references/stages/track.md`
6. 识别当前阶段与用户方向，匹配实战模式卡片并自动加载：
   - 先阅读 `references/wisdom/real-world-patterns/README.md`，了解可用卡片
   - 根据当前阶段（步骤4确定）和用户方向，选择匹配的实战模式卡片
   - 仅加载与当前阶段有对应指引的卡片（卡片 "对 Carpe Diem 用户的启发" 中包含当前阶段小节）
   - 加载后，在对话中自然引用卡片中的关键洞察和反向提醒，避免生硬照搬
7. 当前阶段完成后，先展示要保存的摘要或 Diff；用户确认后再写状态和 `next_recommended`。

### 阶段转换规则

text

```
discover  → validate  : 用户确认方向后
validate  → discover  : 方向验证失败，退回重新发现
validate  → plan      : 方向验证通过
plan      → validate  : 计划依赖条件不满足，退回验证
plan      → handoff   : 计划批准，准备交接
handoff   → track     : 开发开始
track     → plan      : 计划需调整（展示 Diff 并确认后）
track     → paused    : 用户主动暂停
paused    → track     : 恢复跟踪
track     → completed : 项目目标达成
completed → discover  : 开始新项目
```

详细转换图见 `references/stage-transition-graph.md`。

任何文件写入、授权读取或 Track 证据采集前，阅读 `references/safety-boundaries.md` 并满足对应门槛。

## 确定性脚本

先把当前 `SKILL.md` 所在目录解析为 Skill 根目录，再直接调用已定义的子命令。不要为了发现接口而通读脚本源码，也不要先试探不存在的子命令。

- 个人画像：`python3 <skill-root>/scripts/carpe_diem.py state read --json`
- 项目续接：`python3 <skill-root>/scripts/carpe_diem.py project status --root <project-root> --json`
- Track Git 证据：获得只读授权后运行 `python3 <skill-root>/scripts/carpe_diem.py evidence git --root <project-root> --json`

`project status` 返回项目状态不存在时进入 Discover，不要因此创建状态。测试或用户明确要求隔离画像时，给 `state read` 传入获准的 `--profile` 路径；不得回退读取其他画像。

## 授权与变更

- 默认只使用当前对话。读取 GitHub、本地目录、笔记、Issue 或 CI 前，说明用途、目标、只读范围和有效期并获得授权；同一会话内完全相同的范围可复用，扩大范围或进入新会话时重新授权。
- 长期画像中的 Agent 推断只作为候选；用户确认后才可成为未来推荐依据。
- 正式计划按章节逐段确认，最终批准后才写 `docs/project-plan.md` 和 `docs/project-handoff.md`。
- Track 只读检查开发证据。若需要改变正式计划，展示 Diff 并获得确认；若用户要求开发，说明 Carpe Diem 的边界并输出给开发 Agent 的交接建议。

## 主线

用户可以随时打断。先完整回答或查证，再明确回到当前阶段和原 `next_recommended`；除非用户改变目标，不要因为跑题重置流程。

## 下一个项目

项目进入 `completed` 后，询问用户是否开始新项目：

- 是 → 重置状态回到 Discover 阶段
- 否 → 保持 `completed` 状态，下次调用时从 Track 阶段进入

Read more

## Related skills

[More in Productivity](https://clawhub.ai/skills?category=productivity)

Downloads

Security audit[Review](https://clawhub.ai/wanghaonan3333-web/skills/carpe-diem/security-audit)

Last updated53m ago

Current versionv0.1.1

LicenseMIT-0

Report

Bookmark0

Downloads

Security audit[Review](https://clawhub.ai/wanghaonan3333-web/skills/carpe-diem/security-audit)

Last updated53m ago

Current versionv0.1.1

LicenseMIT-0

Report

[![](https://clawhub.ai/logo-transparent.png)ClawHub](https://clawhub.ai/)

Skills and plugins for OpenClaw agents. Part of the wider OpenClaw ecosystem.

[Explore docs](https://docs.openclaw.ai/clawhub/)

#### Browse

[Skills](https://clawhub.ai/skills) [Plugins](https://clawhub.ai/plugins) [Official](https://clawhub.ai/official) [Audits](https://clawhub.ai/audits)

#### Publish

[Publish Skill](https://clawhub.ai/skills/publish) [Publish Plugin](https://clawhub.ai/plugins/publish) [Create org](https://clawhub.ai/settings?view=organizations)

#### Ecosystem

[Overview](https://openclaw.ai/ecosystem) [OpenClaw](https://openclaw.ai/) [Docs](https://docs.openclaw.ai/) [Blog](https://openclaw.ai/blog#clawhub)

#### Community

[GitHub](https://github.com/openclaw/clawhub) [Discord](https://discord.gg/clawd)

Built alongside![](https://openclaw.ai/favicon.svg)the OpenClaw ecosystem

[![](https://openclaw.ai/ecosystem/banners/lobster.png)Lobster](https://docs.openclaw.ai/tools/lobster "Workflow shell") [![](https://openclaw.ai/ecosystem/logos/crabbox.svg)Crabbox](https://crabbox.sh/ "Agent sandboxes") [![](https://openclaw.ai/ecosystem/logos/clickclack.svg)ClickClack](https://clickclack.chat/ "Chat for claws") [![](https://openclaw.ai/ecosystem/banners/crabfleet.png)Crabfleet](https://crabfleet.ai/ "Fleet control") [![](https://openclaw.ai/ecosystem/logos/octopool.svg)Octopool](https://octopool.dev/ "GitHub relay") [![](https://openclaw.ai/ecosystem/logos/clawsweeper.svg)ClawSweeper](https://clawsweeper.bot/ "Issue triage") [![](https://openclaw.ai/ecosystem/banners/agent-skills.png)agent-skills](https://github.com/openclaw/agent-skills "Shared skills") [![](https://openclaw.ai/ecosystem/banners/discrawl.png)discrawl](https://github.com/openclaw/discrawl "Discord archive") [![](https://openclaw.ai/ecosystem/banners/gitcrawl.png)gitcrawl](https://github.com/openclaw/gitcrawl "GitHub crawler") [![](https://openclaw.ai/ecosystem/banners/slacrawl.png)slacrawl](https://github.com/openclaw/slacrawl "Slack archive") [![](https://openclaw.ai/ecosystem/banners/notcrawl.png)notcrawl](https://github.com/openclaw/notcrawl "Notion archive") [![](https://openclaw.ai/ecosystem/banners/telecrawl.png)telecrawl](https://github.com/openclaw/telecrawl "Telegram archive") [![](https://openclaw.ai/ecosystem/banners/graincrawl.png)graincrawl](https://github.com/openclaw/graincrawl "Granola notes") [![](https://openclaw.ai/ecosystem/banners/crawlkit.png)crawlkit](https://github.com/openclaw/crawlkit "Crawler toolkit") [![](https://openclaw.ai/ecosystem/banners/crawlbar.png)crawlbar](https://github.com/openclaw/crawlbar "Crawl menu bar") [![](https://openclaw.ai/ecosystem/banners/acpx.png)acpx](https://github.com/openclaw/acpx "ACP sessions") [![](https://openclaw.ai/ecosystem/banners/mcporter.png)mcporter](https://github.com/openclaw/mcporter "MCP tooling") [![](https://openclaw.ai/ecosystem/logos/tachikoma.png)Tachikoma](https://github.com/openclaw/Tachikoma "Swift model SDK") [![](https://openclaw.ai/ecosystem/logos/clawpatch.svg)clawpatch](https://github.com/openclaw/clawpatch "Review & patch") [![](https://openclaw.ai/ecosystem/banners/clawbench.png)clawbench](https://github.com/openclaw/clawbench "Agent benchmark") [![](https://openclaw.ai/ecosystem/logos/peekaboo.png)Peekaboo](https://github.com/openclaw/Peekaboo "macOS capture") [![](https://openclaw.ai/ecosystem/banners/cookbook.png)cookbook](https://github.com/openclaw/cookbook "SDK examples") [![](https://openclaw.ai/ecosystem/banners/plugin-inspector.png)plugin-inspector](https://github.com/openclaw/plugin-inspector "Plugin testing") [![](https://openclaw.ai/ecosystem/banners/wacrawl.png)wacrawl](https://openclaw.ai/ecosystem#wacrawl "WhatsApp archive") [![](https://openclaw.ai/ecosystem/banners/crabpot.svg)crabpot](https://github.com/openclaw/crabpot "Plugin testbed") [All projects](https://openclaw.ai/ecosystem)![](https://openclaw.ai/ecosystem/banners/lobster.png)Lobster![](https://openclaw.ai/ecosystem/logos/crabbox.svg)Crabbox![](https://openclaw.ai/ecosystem/logos/clickclack.svg)ClickClack![](https://openclaw.ai/ecosystem/banners/crabfleet.png)Crabfleet![](https://openclaw.ai/ecosystem/logos/octopool.svg)Octopool![](https://openclaw.ai/ecosystem/logos/clawsweeper.svg)ClawSweeper![](https://openclaw.ai/ecosystem/banners/agent-skills.png)agent-skills![](https://openclaw.ai/ecosystem/banners/discrawl.png)discrawl![](https://openclaw.ai/ecosystem/banners/gitcrawl.png)gitcrawl![](https://openclaw.ai/ecosystem/banners/slacrawl.png)slacrawl![](https://openclaw.ai/ecosystem/banners/notcrawl.png)notcrawl![](https://openclaw.ai/ecosystem/banners/telecrawl.png)telecrawl![](https://openclaw.ai/ecosystem/banners/graincrawl.png)graincrawl![](https://openclaw.ai/ecosystem/banners/crawlkit.png)crawlkit![](https://openclaw.ai/ecosystem/banners/crawlbar.png)crawlbar![](https://openclaw.ai/ecosystem/banners/acpx.png)acpx![](https://openclaw.ai/ecosystem/banners/mcporter.png)mcporter![](https://openclaw.ai/ecosystem/logos/tachikoma.png)Tachikoma![](https://openclaw.ai/ecosystem/logos/clawpatch.svg)clawpatch![](https://openclaw.ai/ecosystem/banners/clawbench.png)clawbench![](https://openclaw.ai/ecosystem/logos/peekaboo.png)Peekaboo![](https://openclaw.ai/ecosystem/banners/cookbook.png)cookbook![](https://openclaw.ai/ecosystem/banners/plugin-inspector.png)plugin-inspector![](https://openclaw.ai/ecosystem/banners/wacrawl.png)wacrawl![](https://openclaw.ai/ecosystem/banners/crabpot.svg)crabpotAll projects

© 2026 OpenClaw Foundation

[Status](https://clawhub.betteruptime.com/)· [Deployed on Vercel](https://vercel.com/)· [Powered by Convex](https://www.convex.dev/)

```
....:: clawhub/openclaw ::....  skills plugins publishers trust signals   :::: signed manifests ::::: moderated releases ::::: version history ::::   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins
>>> install scan publish verify    @@ gateway @@ registry @@ agents @@     hooks runners slash-commands skill.md templates scanners review-bots   ---- downloads installs stars lineage ownership docs package integrity
  30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins     safe browse paths   official gateways   publisher handles   org trust
:::: signed manifests ::::: moderated releases ::::: version history ::::   ---- downloads installs stars lineage ownership docs package integrity   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals
  hooks runners slash-commands skill.md templates scanners review-bots     safe browse paths   official gateways   publisher handles   org trust   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@
openclaw ecosystem    crabbox clickclack crawler packs gateway plugins   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship
---- downloads installs stars lineage ownership docs package integrity   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@   :::: signed manifests ::::: moderated releases ::::: version history ::::
  safe browse paths   official gateways   publisher handles   org trust     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship     hooks runners slash-commands skill.md templates scanners review-bots
....:: clawhub/openclaw ::....  skills plugins publishers trust signals   :::: signed manifests ::::: moderated releases ::::: version history ::::   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins
>>> install scan publish verify    @@ gateway @@ registry @@ agents @@     hooks runners slash-commands skill.md templates scanners review-bots   ---- downloads installs stars lineage ownership docs package integrity
  30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins     safe browse paths   official gateways   publisher handles   org trust
:::: signed manifests ::::: moderated releases ::::: version history ::::   ---- downloads installs stars lineage ownership docs package integrity   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals
  hooks runners slash-commands skill.md templates scanners review-bots     safe browse paths   official gateways   publisher handles   org trust   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@
openclaw ecosystem    crabbox clickclack crawler packs gateway plugins   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship
---- downloads installs stars lineage ownership docs package integrity   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@   :::: signed manifests ::::: moderated releases ::::: version history ::::
  safe browse paths   official gateways   publisher handles   org trust     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship     hooks runners slash-commands skill.md templates scanners review-bots
....:: clawhub/openclaw ::....  skills plugins publishers trust signals   :::: signed manifests ::::: moderated releases ::::: version history ::::   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins
>>> install scan publish verify    @@ gateway @@ registry @@ agents @@     hooks runners slash-commands skill.md templates scanners review-bots   ---- downloads installs stars lineage ownership docs package integrity
  30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins     safe browse paths   official gateways   publisher handles   org trust
:::: signed manifests ::::: moderated releases ::::: version history ::::   ---- downloads installs stars lineage ownership docs package integrity   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals
  hooks runners slash-commands skill.md templates scanners review-bots     safe browse paths   official gateways   publisher handles   org trust   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@
openclaw ecosystem    crabbox clickclack crawler packs gateway plugins   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship
---- downloads installs stars lineage ownership docs package integrity   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@   :::: signed manifests ::::: moderated releases ::::: version history ::::
  safe browse paths   official gateways   publisher handles   org trust     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship     hooks runners slash-commands skill.md templates scanners review-bots
....:: clawhub/openclaw ::....  skills plugins publishers trust signals   :::: signed manifests ::::: moderated releases ::::: version history ::::   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins
>>> install scan publish verify    @@ gateway @@ registry @@ agents @@     hooks runners slash-commands skill.md templates scanners review-bots   ---- downloads installs stars lineage ownership docs package integrity
  30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins     safe browse paths   official gateways   publisher handles   org trust
:::: signed manifests ::::: moderated releases ::::: version history ::::   ---- downloads installs stars lineage ownership docs package integrity   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals
  hooks runners slash-commands skill.md templates scanners review-bots     safe browse paths   official gateways   publisher handles   org trust   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@
openclaw ecosystem    crabbox clickclack crawler packs gateway plugins   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship
---- downloads installs stars lineage ownership docs package integrity   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@   :::: signed manifests ::::: moderated releases ::::: version history ::::
  safe browse paths   official gateways   publisher handles   org trust     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship     hooks runners slash-commands skill.md templates scanners review-bots
....:: clawhub/openclaw ::....  skills plugins publishers trust signals   :::: signed manifests ::::: moderated releases ::::: version history ::::   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins
>>> install scan publish verify    @@ gateway @@ registry @@ agents @@     hooks runners slash-commands skill.md templates scanners review-bots   ---- downloads installs stars lineage ownership docs package integrity
  30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins     safe browse paths   official gateways   publisher handles   org trust
:::: signed manifests ::::: moderated releases ::::: version history ::::   ---- downloads installs stars lineage ownership docs package integrity   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals
  hooks runners slash-commands skill.md templates scanners review-bots     safe browse paths   official gateways   publisher handles   org trust   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@
openclaw ecosystem    crabbox clickclack crawler packs gateway plugins   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship
---- downloads installs stars lineage ownership docs package integrity   >>> install scan publish verify    @@ gateway @@ registry @@ agents @@   :::: signed manifests ::::: moderated releases ::::: version history ::::
  safe browse paths   official gateways   publisher handles   org trust     30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship     hooks runners slash-commands skill.md templates scanners review-bots
....:: clawhub/openclaw ::....  skills plugins publishers trust signals   :::: signed manifests ::::: moderated releases ::::: version history ::::   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins
>>> install scan publish verify    @@ gateway @@ registry @@ agents @@     hooks runners slash-commands skill.md templates scanners review-bots   ---- downloads installs stars lineage ownership docs package integrity
  30 skills 12 plugins    /api/v1/skills   /owners   /audit   /ship   openclaw ecosystem    crabbox clickclack crawler packs gateway plugins     safe browse paths   official gateways   publisher handles   org trust
:::: signed manifests ::::: moderated releases ::::: version history ::::   ---- downloads installs stars lineage ownership docs package integrity   ....:: clawhub/openclaw ::....  skills plugins publishers trust signals
```