# Carpe Diem v0.1 实施计划

- 日期：2026-08-27
- 依据：`docs/superpowers/specs/2026-08-27-carpe-diem-design.md`
- 目标：交付一个不自带模型、可安装到多种 Agent、能完成 Discover / Validate / Plan / Track 的开源 Skill，并完成首轮本地内测。

## 1. 实施约束

1. 仓库根目录就是权威 Skill，不维护平台专属方法分叉。
2. 宿主 Agent 负责对话、推理和联网研究；本地脚本只做确定性工作。
3. Carpe Diem 不编写项目业务代码，Track 保持只读。
4. 所有长期画像变化先产生候选 Diff，再由用户确认。
5. 所有项目状态默认本地保存，不进入 Git。
6. 先写失败测试，再写满足测试的最小实现。
7. 每个里程碑独立验证；失败时不继续叠加功能。

## 2. 目标文件树

```text
carpe-diem/
├── SKILL.md
├── manifest.json
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── .gitignore
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/ci.yml
├── references/
│   ├── methodology.md
│   ├── state-schema.md
│   ├── safety-boundaries.md
│   └── stages/
│       ├── discover.md
│       ├── validate.md
│       ├── plan.md
│       └── track.md
├── templates/
│   ├── project-plan.md
│   ├── project-handoff.md
│   └── progress-summary.md
├── scripts/
│   └── carpe_diem.py
├── adapters/
│   ├── codex/INSTALL.md
│   ├── claude-code/INSTALL.md
│   ├── cursor/INSTALL.md
│   └── openclaw/INSTALL.md
├── tests/
│   ├── fixtures/
│   ├── test_structure.py
│   ├── test_state.py
│   ├── test_project.py
│   ├── test_evidence.py
│   ├── test_plan.py
│   ├── test_install.py
│   └── test_guidance.py
└── docs/
    ├── internal-testing.md
    └── superpowers/
```

## 3. 里程碑 M0：开源 Skill 骨架

### 任务

1. 先创建 `tests/test_structure.py`，要求根文件、引用文件、模板、适配器和 frontmatter 存在。
2. 运行结构测试，确认因文件缺失而失败。
3. 创建最小文件树和合法 `SKILL.md` frontmatter。
4. 创建 `manifest.json`，声明版本 `0.1.0`、schema 版本和文件清单。
5. 添加 Apache-2.0 `LICENSE`、贡献指南、行为准则和 Issue 模板。
6. 添加仅运行标准库 `unittest` 的 CI。

### 验证

```bash
python3 -m unittest tests.test_structure -v
python3 -m unittest discover -s tests -v
```

### 完成标准

- 根目录可被识别为 Agent Skill。
- manifest 中列出的所有文件存在。
- 仓库不含密钥、个人路径或生成状态。

## 4. 里程碑 M1：沟通引导内核与四阶段 Playbook

### 任务

1. 在 `tests/test_guidance.py` 中建立结构契约，检查每个阶段必须具有：一句话本质、进入条件、主动讲授、Agent 动作、用户决策、成功信号、常见误区、状态写入、下一步路由。
2. 添加黄金对话负面 fixture：连续盘问、随机创意列表、竞品链接堆积、Track 越界开发。
3. 添加黄金对话正面 fixture：先给判断、单一选择、打断后回主线、证据化推荐、跨阶段续接。
4. 编写 `references/methodology.md`，固化“钩子 -> 讲清 -> 证据 -> 建议 -> 单一决定 -> 记录”的引导块。
5. 编写 Discover、Validate、Plan、Track 四份阶段文件。
6. 编写 `SKILL.md` 路由逻辑：读取状态、选择阶段、渐进加载、更新 `next_recommended`。

### 验证

```bash
python3 -m unittest tests.test_guidance -v
```

### 完成标准

- Skill 不依赖连续开放式提问推进。
- 每个阶段明确“说什么、做什么、存什么、何时退出”。
- Track 文件明确禁止业务开发。

## 5. 里程碑 M2：双层记忆与事件历史

### 任务

1. 在 `tests/test_state.py` 中先覆盖：首次创建、读取、候选 Diff、确认应用、纠正、遗忘、便携导出、原子写入、revision 冲突、损坏文件恢复和 schema 迁移预览。
2. 在 `tests/test_project.py` 中先覆盖：项目初始化、阶段变更、候选淘汰、里程碑更新、事件追加、下一步续接和 `.gitignore` 拒绝降级。
3. 实现 `scripts/carpe_diem.py state ...` 子命令。
4. 实现 `project init/status/event` 子命令。
5. 所有 JSON 输出提供人类可读和 `--json` 两种形式。
6. 所有写入使用同目录临时文件、`fsync` 和原子替换；冲突时不覆盖。

### 验证

```bash
python3 -m unittest tests.test_state tests.test_project -v
```

### 完成标准

- 个人画像和项目状态严格分离。
- 未确认画像不会作为长期事实写入。
- 损坏、冲突和不可写路径不会造成静默数据丢失。
- 便携导出不包含绝对路径、凭据或原始内容。

## 6. 里程碑 M3：计划、交接与质量门槛

### 任务

1. 编写三个模板：正式计划、开发交接、进度摘要。
2. 在 `tests/test_plan.py` 中覆盖：必需章节、空白章节、`TBD/TODO`、缺少验收标准、缺少非目标、缺少证据来源、缺少第一个里程碑。
3. 实现 `plan validate`，输出阻塞问题和警告。
4. 实现 `plan diff`，只允许比较 Carpe Diem 管理的计划和交接文件。
5. 在 Plan Playbook 中强制逐段设计、自查、用户批准、再写入。
6. 在 Handoff 规则中明确写入结束后不开始开发、不产生 Git 提交。

### 验证

```bash
python3 -m unittest tests.test_plan -v
```

### 完成标准

- 空白或矛盾计划无法通过验证。
- 开发 Agent 能从交接包知道目标、范围、验收和禁止事项。
- Carpe Diem 在交接后进入 Track，而不是 Implementation。

## 7. 里程碑 M4：只读 Git 证据与进度跟踪

### 任务

1. 在 `tests/test_evidence.py` 中使用临时 Git 仓库覆盖：无仓库、空仓库、有提交、脏工作区、分支变化、HEAD 前进、历史重写和命令失败。
2. 实现 `evidence git`，只执行只读 Git 子命令。
3. 输出 HEAD、分支、提交摘要、工作区状态和从上次 HEAD 到当前 HEAD 的变化范围。
4. 不保存完整 Diff；事件只保存 Git 引用、里程碑变化和摘要。
5. 不运行项目测试；只接受已有测试或 CI 证据引用。
6. Track Playbook 区分“声称完成”和“有证据完成”。

### 验证

```bash
python3 -m unittest tests.test_evidence -v
```

### 完成标准

- 证据采集不改变 Git 状态。
- 脏工作区不被清理或覆盖。
- 历史不一致时明确报告，不伪造连续进度。

## 8. 里程碑 M5：安装、验证与跨 Agent 适配

### 任务

1. 核对 Codex、Claude Code、Cursor、OpenClaw 当前官方 Skill 目录和发现规则。
2. 在 `tests/test_install.py` 中覆盖：平台检测、安装计划、显式确认、快照复制、内容 fingerprint、重复安装、版本冲突、验证失败和卸载边界。
3. 实现 `install detect/plan/apply/verify/uninstall`。
4. 安装前展示目标，安装后重新扫描目标文件与 fingerprint；复制完成不等于验证成功。
5. 编写四个平台的 `INSTALL.md`，方法逻辑只引用根 Skill。
6. 在真实可用环境中逐一做发现与触发烟雾测试；不可用环境明确记录为未验证，而不是声称支持。

### 验证

```bash
python3 -m unittest tests.test_install -v
python3 scripts/carpe_diem.py doctor --json
```

### 完成标准

- 同一版本 Skill 可安装到目标环境。
- 卸载只删除安装器自己确认过的相同 fingerprint 快照。
- 平台适配器不复制核心方法论。

## 9. 里程碑 M6：文档、总验证与首轮内测

### 任务

1. 完成 `README.md`：问题、演示、安装、使用、隐私、职责边界和贡献方式。
2. 完成 `docs/internal-testing.md`，包含三轮内测步骤和七项评分表。
3. 运行全量测试、编译检查、结构检查和 `doctor`。
4. 在当前 Codex 环境做第一轮冷启动演练，使用隔离的临时用户目录和临时空仓库。
5. 检查引导是否出现连续问卷、随机点子、无证据原创声明或越界开发。
6. 记录首次内测结果、失败点和下一版修正，不把演练状态混入真实用户画像。
7. 若本机可用，再执行至少一个第二宿主的跨 Agent 状态恢复烟雾测试；否则把该项标为待真实环境验证。

### 总验证

```bash
python3 -m compileall scripts tests
python3 -m unittest discover -s tests -v
python3 scripts/carpe_diem.py doctor --json
git diff --check
```

### 完成标准

- 全量自动测试通过。
- 首轮内测产生可审阅记录。
- `Guidance`、`Clarity`、`Handoff` 的演练评分均不低于 4。
- Carpe Diem 没有写入业务代码或真实个人画像。

## 10. 提交顺序

建议按里程碑产生可独立审阅的提交：

1. `chore: scaffold Carpe Diem skill`
2. `feat: add guided project discovery playbooks`
3. `feat: add local profile and project state`
4. `feat: add plan and handoff validation`
5. `feat: add read-only project tracking evidence`
6. `feat: add cross-agent installation adapters`
7. `docs: add usage and internal testing guide`

提交只发生在各里程碑验证通过后；不为了匹配提交数量拆分未完成状态。

## 11. 实施完成判定

只有同时满足以下条件，v0.1 才算完成：

- 规格中的必需文件和行为全部存在；
- 自动测试、结构验证和 `doctor` 通过；
- 至少在 Codex 中真实发现并触发 Skill；
- 至少完成一轮隔离内测；
- 未验证的其他 Agent 支持被清楚标记；
- 工作区无意外生成状态、个人路径或凭据；
- README 能让新的贡献者理解产品边界并复现验证。
