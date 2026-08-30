# Carpe Diem — AgentTeams 进展交接文档

> 将此文档交给新会话，配合 `docs/carpe-diem-v0.2-dev-plan.md` 使用
> 工作区目录：`/Users/zhaochuan/Documents/ChatGPT/Carpe Diem/`

---

## 一、项目是什么

Carpe Diem 是一个 OpenClaw Skill，帮拥有 Coding Agent 但没有项目方向的开发者完成 **发现→验证→规划→跟踪** 四阶段。

核心定位：**项目点火导师 + 多 Agent 协作框架**

---

## 二、当前状态

### 已完成的改进

| 改进 | 文件 | 说明 |
|------|------|------|
| Trigger 条件块 | `SKILL.md` | 新增 `## Trigger` 章节，明确激活/不激活场景 |
| 阶段转换规则 | `SKILL.md` | 12 条阶段转换规则 + 下一个项目循环 |
| 英文版 | `SKILL.en.md` | 完整翻译（4991 字节） |
| 权限声明 | `manifest.json` | 新增 `required_capabilities` 字段 |
| 状态转换图 | `references/stage-transition-graph.md` | Mermaid 图 + 阶段说明 |
| 方法论卡片 | `references/wisdom/real-world-patterns/` | 4 张卡片：最佳实践、Agent 构建、上下文工程、Agent Skills |
| 文章摘要 | `references/wisdom/researcher-t1-summary.md` | 7 篇 Anthropic 博客文章摘要 |
| 开发计划 | `docs/carpe-diem-v0.2-dev-plan.md` | 完整五阶段开发计划（688 行） |
| 进展文档 | `docs/progress-and-roadmap.md` | 项目进展与路线图 |

### 原有资产

| 资产 | 说明 |
|------|------|
| `scripts/carpe_diem.py` | 1077 行确定性脚本，已有路径遍历防护 |
| `tests/` | 8 个测试文件，共 1061 行 |
| `references/stages/` | 四阶段引导文件 |
| `templates/` | 计划/交接/进度模板 |
| `adapters/` | 4 平台安装指南 |

---

## 三、核心目标：嵌入多 Agent 协作协议

**核心思想**：把 AgentTeams 的文件协议嵌入 Carpe Diem，让 Carpe Diem 成为一个不依赖 DSH 的独立多 Agent 协作框架。

### 文件协议

```
.carpe-diem/team/
├── team.json              # 团队元数据（revision 乐观锁）
├── members/               # 成员状态
├── tasks/MANIFEST.json    # 任务索引（拓扑排序）
├── tasks/t1.json          # 单个任务
├── mailboxes/             # 消息队列
└── dashboard.html         # 🔜 HTML 进度看板
```

### 对比 DSH AgentTeams 的简化

| DSH 有的 | 嵌入式方案 | 原因 |
|----------|-----------|------|
| 自动唤醒成员 | ❌ 成员自己读任务 | 跨平台无法统一 |
| attempt_id 机制 | ❌ revision 替代 | 简化实现 |
| 成员间直接通信 | ❌ mailbox 单向 | 避免复杂路由 |
| 分布式状态 | ❌ 本地文件系统 | 跨机器用 Git |

---

## 四、接下来做什么

### 第一步：Phase 1 — v0.1.1 发版收尾（3 天）

**1.1 wisdom 卡片接入 SKILL.md**
- 在 `SKILL.md` 的 `## 每次调用` 中加第 6 步
- 当用户方向匹配时自动加载对应 wisdom 卡片
- 验收：Agent 在 Discover 阶段能自动选择并加载卡片

**1.2 验证安装流程**
```bash
python3 scripts/carpe_diem.py install plan --platform codex --source . --target /tmp/test-install/carpe-diem --json
python3 scripts/carpe_diem.py install apply --plan /tmp/install-plan.json --yes
python3 scripts/carpe_diem.py install verify --target /tmp/test-install/carpe-diem
python3 scripts/carpe_diem.py install uninstall --target /tmp/test-install/carpe-diem --yes
```

**1.3 更新 ClawHub 发布**
- 发布 v0.1.1
- 更新英文 description

### 第二步：Phase 2 — 团队协作协议设计（3 天）

**2.1 读 DSH AgentTeams 源码**
```
/Users/zhaochuan/Documents/ChatGPT/deepseek-harness/packages/experimental/agent-team/src/
├── types.ts        219行 — 类型定义
├── task-board.ts   297行 — 任务管理
├── mailbox.ts      338行 — 消息队列
├── fold.ts         291行 — 流程编排
└── roster.ts       485行 — 成员管理
```

**2.2 设计 Carpe Diem 团队协议** → 定义 `.carpe-diem/team/` 文件结构

**2.3 编写 `references/team-workflow.md`** → 方法论说明文档

### 第三步：Phase 3 — 团队脚本开发（8 天）

**3.1 `scripts/carpe_diem_team.py`（约 800 行）**

子命令：
```
team create <name>                    # 创建团队
team status                           # 查看团队状态
team delete                           # 删除团队

member add <name> --role <role>       # 添加成员
member remove <name>                  # 移除成员

task create <subject>                 # 创建任务
  --assignee <name>                   # 分配给成员
  --depends-on <task_id>              # 依赖任务
task list                             # 列出任务
task claim <task_id>                  # 认领任务
task update <task_id>                 # 更新任务状态
  --status <status>                   # pending/in_progress/completed/failed
  --output <text>                     # 完成输出

message send <to> <content>           # 发送消息
message list                          # 查看未读消息

team dashboard --html                 # 生成 HTML 进度看板
```

**3.2 HTML 进度看板（`team dashboard --html`）**

生成 `.carpe-diem/team/dashboard.html`，三列看板：
- ✅ 已完成 — 绿色卡片
- 🔄 进行中 — 橙色卡片
- ⏳ 等待中 — 灰色卡片（显示依赖）

顶部：统计数字 + 进度条
底部：最近活动时间线

**3.3 测试套件（`tests/test_team.py`，约 300 行）**

8 个测试用例：
1. 创建团队 → 目录结构正确
2. 添加成员 → 成员文件存在
3. 创建任务 → 任务文件 + MANIFEST 更新
4. 任务依赖 → 不可认领有未完成依赖的任务
5. 完成任务 → 下游任务变为可认领
6. 发送消息 → 消息文件写入
7. revision 冲突 → 旧写入被拒绝
8. 完整流程 → 创建→分配→认领→完成→汇总

### 第四步：Phase 4 — SKILL.md 集成（3 天）

**4.1 SKILL.md 新增 `## 团队协作模式` 章节**

**4.2 `references/stages/plan.md` 改造**
- 计划批准后自动拆分任务到 `.carpe-diem/team/tasks/`

**4.3 `references/stages/track.md` 改造**
- 读取团队任务状态
- 自动刷新 `dashboard.html`
- 汇总团队进度报告

### 第五步：Phase 5 — 方法论卡片 + 项目模板（6 天）

**5.1 项目类型模板**（`references/wisdom/project-archetypes/`）
- CLI 工具模板
- Web 应用模板
- 开发者工具模板

**5.2 ADR 输出** — Plan 阶段自动生成 `docs/adr/NNNN-title.md`

**5.3 更多 wisdom 卡片** — 从 Anthropic 博客继续蒸馏

---

## 五、关键文件路径

```
/Users/zhaochuan/Documents/ChatGPT/Carpe Diem/
├── SKILL.md                          # 主指令
├── SKILL.en.md                       # 英文版
├── manifest.json                     # 包清单
├── scripts/carpe_diem.py             # 现有确定性脚本（1077行）
├── references/
│   ├── methodology.md                # 带领式引导方法论
│   ├── state-schema.md               # 状态模式
│   ├── safety-boundaries.md          # 安全边界
│   ├── stage-transition-graph.md     # 阶段转换图
│   ├── stages/                       # 四阶段文件
│   └── wisdom/                       # 方法论卡片库
│       ├── README.md
│       ├── researcher-t1-summary.md
│       └── real-world-patterns/
│           ├── claude-code-best-practices.md
│           ├── building-effective-agents.md
│           ├── context-engineering.md
│           └── agent-skills.md
├── tests/                            # 1061 行测试
├── templates/                        # 计划/交接/进度模板
├── adapters/                         # 4 平台安装指南
└── docs/
    ├── progress-and-roadmap.md       # 项目进展
    ├── carpe-diem-v0.2-dev-plan.md   # 完整开发计划（688行）
    └── superpowers/
        ├── specs/2026-08-27-carpe-diem-design.md
        └── plans/2026-08-27-carpe-diem-v0.1-implementation.md
```

---

## 六、工作方式：必须用 AgentTeams

**所有改进工作必须用 AgentTeams 完成。** 流程：

1. `agent_teams_create` — 创建团队，根据任务需要命名
2. `agent_teams_add_member` — 添加成员，明确角色
3. `agent_teams_create_task` — 创建任务，分配 dependencies
4. `agent_teams_claim_task` — 成员认领任务
5. `agent_teams_send_message` — 指导成员工作
6. `agent_teams_update_task` — 标记完成
7. `agent_teams_delete` — 全部完成后解散团队

**注意**：编辑文件需要 `danger-full-access` 权限，因为项目不在 DSH 默认工作区内。

---

## 七、关键约束

- ❌ 不要引用 HA7CH School
- ✅ 使用"带领式引导"替代
- ✅ 所有方法论卡片放在 `references/wisdom/` 下
- ✅ 团队协议文件放在 `.carpe-diem/team/` 下
- ✅ 保持 Python 标准库依赖，不引入第三方包
- ✅ 先读 `docs/carpe-diem-v0.2-dev-plan.md` 了解完整计划