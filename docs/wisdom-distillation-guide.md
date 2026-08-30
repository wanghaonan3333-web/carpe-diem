# Carpe Diem 智慧蒸馏指南

> 汇总当前蒸馏成果，并定义如何持续扩展新的智慧来源。
> 最后更新：2026-09-01

---

## 一、当前成果速览

Carpe Diem 的智慧蒸馏工作已全部完成（四阶段，共 33 张行为卡）：

| 指标 | 数值 |
|:----|:----:|
| 行为卡总数 | **33 张**（P0: 12 + P1: 14 + P2: 7） |
| 覆盖的思想领袖 | **24 位** |
| 覆盖的工程案例/项目 | **16 个** |
| 研究文件 | **5 份**（~1,400 行） |
| 规划蓝图 | `docs/wisdom-distillation-plan.md`（549 行） |
| 总结文档 | `docs/wisdom-distillation-summary.md`（231 行） |
| 行为卡代码行 | **~2,200+ 行** |

### 卡片分布

| 阶段 | 卡片 | 数量 |
|:----|:----|:----:|
| **Discover** | `mom-test`, `scratch-your-itch`, `jtbd-work-statement`, `secret-test`, `dirty-work-test` | 5 |
| **Validate** | `test-card`, `handmade-first`, `behavior-signal`, `continuous-check` | 4 |
| **Plan** | `strategy-kernel`, `appetite-constraint`, `c4-architecture`, `bounded-context`, `adr-rfc-enhance`, `pitch-format`, `stability-patterns`, `test-first`, `document-as-deliverable` | 9 |
| **Track** | `certainty-level`, `wip-detection`, `constraint-diagnosis`, `four-metrics`, `milestone-state`, `heartbeat`, `integration-health`, `regular-departure`, `value-stream` | 9 |
| **Cross** | `beachhead`, `say-no-by-default`, `complexity-budget`, `handmade-validation`, `pmf-survey`, `user-behavior-metric` | 6 |

### 已覆盖的智慧来源

| 阶段 | 人物 |
|:----|:----|
| Discover | Paul Graham, Rob Fitzpatrick, Clayton Christensen, Peter Thiel, Jason Fried & DHH |
| Validate | Eric Ries, Steve Blank, Ash Maurya, David Bland, Cindy Alvarez |
| Plan | Ryan Singer, Eric Evans, Michael Nygard, Frederick Brooks, Martin Fowler, Simon Brown, Richard Rumelt, Alistair Cockburn |
| Track | Gene Kim, Nicole Forsgren, David J. Anderson, Eliyahu Goldratt, Kent Beck, Ryan Singer |
| Cross | DHH, John Ousterhout, Geoffrey Moore, Paul Graham |

### 已覆盖的工程案例

Zappos, Dropbox, Buffer, Groupon, Airbnb, Superhuman, Stripe, GitHub, Basecamp, Linux Kernel, Kubernetes, Mozilla Firefox, React, SQLite, PostgreSQL, Ruby on Rails

---

## 二、蒸馏架构

### 2.1 三层模型

```
研究层 (Research)
  └── 人物/项目/书籍的深度研究 → 产出研究文件（如 researcher-t1-discover-sources.md）
       │
规划层 (Plan)
  └── 综合规划蓝图，确定优先级和触发点 → 产出 wisdom-distillation-plan.md
       │
实现层 (Cards)
  └── 行为卡（mentors/ 目录）+ 集成到 SKILL.md
       ├── references/wisdom/mentors/<stage>/<card-name>.md
       ├── references/wisdom/mentors/README.md    ← 索引 + 触发规则
       ├── SKILL.md                               ← 步骤6b 加载列表
       └── docs/wisdom-distillation-summary.md    ← 完成状态
```

### 2.2 行为卡结构

每张行为卡统一为 4 个部分：

```
1. 问题本质   — 为什么这个行为很重要（2-3 句）
2. 触发条件   — 3-5 个具体场景，什么情况下该激活
3. 行为指导   — 5-6 条可操作步骤，用户可以直接执行
4. 不适用场景 — 3-5 个，什么时候不该用
```

### 2.3 三条铁律（不可违反）

| 规则 | 含义 | 检查标准 |
|:----|:----|:---------|
| **不露来源** | 全文使用 Carpe Diem 自己的语言，不出现人名、书名、公司名 | grep 扫描全文：零命中 |
| **不抽象** | 不是"什么是 X"，而是"当你遇到 Y 时，怎么做 Z" | 每条都有触发条件 + 行为指导 |
| **可操作** | 用户直接得到 actionable 的指导，不是"大师名言" | 指导步骤可在 3-5 轮对话内执行 |

### 2.4 集成点

新卡片需要更新 **3 个文件**：

1. **`references/wisdom/mentors/README.md`** — 添加索引表条目 + 触发条件匹配规则
2. **`SKILL.md`** — 步骤6b 加载列表添加新卡片名称
3. **`docs/wisdom-distillation-summary.md`** — 更新完成状态

---

## 三、如何蒸馏新智慧来源

### 3.1 完整工作流

```
阶段 A：研究
  1. 确定要蒸馏的人物/项目/书籍
  2. 研究其核心智慧（1-3 条可蒸馏规则）
  3. 产出研究文件（可选，复杂来源建议写）
  4. 确定适用阶段和触发点

阶段 B：创建行为卡
  5. 按统一格式写行为卡（4 个部分）
  6. 三次检查：不露来源？不抽象？可操作？
  7. 保存到 mentors/<stage>/<card-name>.md

阶段 C：集成
  8. 更新 mentors/README.md（索引 + 触发条件）
  9. 更新 SKILL.md（步骤6b 加载列表）
  10. 更新 wisdom-distillation-summary.md

阶段 D：审核
  11. 全文扫描：grep 是否有来源名称泄漏
  12. 检查格式一致性
  13. 确保不适用场景覆盖了边界情况
```

### 3.2 详细步骤

#### 步骤 1：确定蒸馏对象

可能的来源类型：

| 类型 | 例子 | 评估标准 |
|:----|:----|:---------|
| **思想领袖** | Paul Graham, Eric Ries | 有可转化为行为规则的核心理念 |
| **工程案例** | SQLite, Kubernetes, GitHub | 多年运行的工程实践，有明确机制 |
| **书籍/方法论** | Shape Up, The Mom Test, Accelerate | 有明确的框架或步骤 |
| **个人经验** | 你自己的项目经验 | 有具体的故事和反思 |

**选择标准**：优先选择"可验证的工程实践"（如 Linux Kernel 治理模型），其次是"可转化为可操作规则的个人智慧"（如 Paul Graham 的脏活测试）。

#### 步骤 2：研究核心智慧

提取 1-3 条可蒸馏的规则。不要试图概括整个体系，只提取对 Carpe Diem 四阶段有直接作用的部分。

对于每个智慧来源，回答：

- 这个智慧最适合 Carpe Diem 的哪个阶段？
- 用户在什么场景下会需要这个智慧？（触发条件）
- 用户应该具体做什么？（行为指导）
- 什么情况下这个智慧不适用？（反向提醒）

#### 步骤 3：确定阶段和优先级

| 优先级 | 含义 |
|:------|:----|
| **P0** | 核心必需——没有这张卡，阶段引导有重大缺口 |
| **P1** | 重要——有这张卡更好，但阶段可以正常运作 |
| **P2** | 有价值——锦上添花，补充特定场景 |

#### 步骤 4：写行为卡

使用模板：

```markdown
# 卡片名称

## 问题本质

2-3 句话说明为什么这个行为很重要。

## 触发条件

1. 场景一：...
2. 场景二：...
3. 场景三：...
4. 场景四：...

## 行为指导

1. **第一步**：...
2. **第二步**：...
3. **第三步**：...
4. **第四步**：...
5. **第五步**：...
6. **第六步**：...

## 不适用场景

1. ...
2. ...
3. ...
4. ...
```

**关键规则**：
- ❌ 不要出现"Paul Graham 说"、"根据 The Mom Test"、"Zappos 的案例表明"
- ✅ 用"当用户说「很多人说好」时，可以试试这个方法"替代
- ❌ 不要解释"什么是 X"
- ✅ 直接给出"当你遇到 Y 时，怎么做 Z"
- ❌ 不要写"你应该理解这个概念"
- ✅ 写"你可以试试这个步骤"

#### 步骤 5：集成到系统

**更新 `mentors/README.md`**：

1. 在对应阶段的表格中添加一行
2. 在"触发条件匹配"部分添加一条触发规则
3. 如果跨阶段，在"阶段匹配规则"表中更新对应阶段

**更新 `SKILL.md`**：

在步骤 6b 的加载列表中添加新卡片名称。例如：
```markdown
Discover → `mom-test`、`scratch-your-itch`、`jtbd-work-statement`、`secret-test`、`dirty-work-test`、`<new-card>`
```

**更新 `wisdom-distillation-summary.md`**：

更新卡片表格和完成状态。

#### 步骤 6：审核

```
三条铁律检查：
  [ ] 不露来源 — grep -n "Paul Graham\|书名\|公司名" 卡文件 → 零命中
  [ ] 不抽象   — 每张卡都有触发条件 + 行为指导部分
  [ ] 可操作   — 指导步骤可在 3-5 轮对话内执行

格式检查：
  [ ] 有"问题本质"部分
  [ ] 有"触发条件"部分（3-5 个）
  [ ] 有"行为指导"部分（5-6 条）
  [ ] 有"不适用场景"部分（3-5 个）

集成检查：
  [ ] mentors/README.md 已更新
  [ ] SKILL.md 步骤6b 已更新
  [ ] 如果跨阶段，阶段匹配规则已更新
  [ ] 触发条件匹配规则已添加
```

---

## 四、常见问题

### Q: 可以两个来源合并到一张卡吗？

可以。例如 `handmade-validation` 卡融合了 Paul Graham 的 "Do Things That Don't Scale" 和 Airbnb 的手工验证案例——两者指向同一个行为指导。只要合并后的卡片不出现来源名称即可。

### Q: 跨阶段卡和阶段卡的区分是什么？

- **阶段卡**：只在特定阶段激活（如 `mom-test` 只在 Discover）
- **跨阶段卡**：在多个阶段都可能触发（如 `say-no-by-default` 适用于所有阶段）

跨阶段卡放在 `cross/` 目录，在 `mentors/README.md` 的"阶段匹配规则"中声明适用哪些阶段。

### Q: 如何判断一张卡是 P0/P1/P2？

- **P0**：如果不加载这张卡，用户在该阶段会错过关键行为指导（如 `mom-test` 防止被虚假反馈误导）
- **P1**：加载后显著提升引导质量，但不加载也能完成阶段（如 `jtbd-work-statement` 提供更结构化的方向定义）
- **P2**：特定场景下有价值，但大部分用户不会触发（如 `stability-patterns` 只在涉及外部依赖时有用）

### Q: 蒸馏工程案例和蒸馏人物有什么不同？

工程案例（如 Kubernetes KEP 状态机、Mozilla Firefox 发布火车）通常有**明确的机制和规则**，更容易转化为可操作步骤。人物智慧（如 Paul Graham 的脏活测试）需要更多提炼才能变成可操作规则。

**优先顺序**：工程案例 > 人物智慧 > 理论框架

### Q: 为什么不露来源这么重要？

Carpe Diem 的 Agent 角色是"项目点火导师"，不是"哪位大师的替身"。如果卡片中出现"Paul Graham 认为"，用户会被引导去思考"Paul Graham 是谁"而不是"我该怎么做"。全用 Carpe Diem 自有语言让 Agent 始终保持**自己的声音**，用户信任的是系统的引导，而非某个外部权威的背书。

---

## 五、未来扩展方向

### 5.1 新增人物/来源的建议

根据当前阶段分布，以下方向可能有扩展空间：

| 方向 | 可能的来源 | 建议阶段 |
|:----|:----------|:--------|
| AI/ML 项目管理 | Andrej Karpathy, Google PAIR | Plan, Track |
| 开源社区运营 | Nadia Eghbal, 常见开源治理模型 | Cross |
| 设计思维 | Don Norman, IDEO, Design Sprint | Discover, Validate |
| 增长与留存 | Andrew Chen, Brian Balfour | Validate, Cross |
| 异步/远程协作 | Basecamp, GitLab Handbook | Plan, Track |
| 风险管理 | Nassim Taleb (反脆弱) | Cross, Plan |
| 更多工程案例 | Redis, nginx, curl, FFmpeg | 各阶段 |

### 5.2 可以添加的卡片类型

除了当前的行为卡，还可以考虑：

- **反模式卡**：列出常见错误模式，帮助用户识别和避免（如"过早优化"、"功能蔓延"）
- **检查清单卡**：提供可复用的检查清单（如"生产就绪检查清单"）
- **对话模板卡**：提供具体的对话模板（如"用户访谈问题模板"）

---

*本指南随智慧蒸馏工作持续推进而更新。*