# Carpe Diem 智慧蒸馏总结

> 本文档汇总了 Carpe Diem 智慧蒸馏工作的完整全景——从研究到产出，从人物到卡片。
> 最后更新：2026-09-01（第四阶段完成）

---

## 一、蒸馏哲学

Carpe Diem 的智慧蒸馏遵循三条铁律：

| 规则 | 含义 | 检查标准 |
|------|------|---------|
| **不露来源** | 所有卡片的语言是 Carpe Diem 自己的，不出现人名、书名、公司名 | 扫描全文：零来源名称 |
| **不抽象** | 不是"什么是 X"，而是"当你遇到 Y 时，怎么做 Z" | 每条都有触发条件 + 行为指导 |
| **可操作** | 用户直接得到 actionable 的指导，不是"大师名言" | 指导步骤可在 3-5 轮对话内执行 |

我们不模拟 Paul Graham 的语气、不照搬 Lean Startup 的完整体系、不引入理论官僚主义。每个智慧来源被提炼为 1-3 条可操作的规则，以**行为卡**形式嵌入 Carpe Diem 的现有流程。

---

## 二、研究阶段：覆盖了谁

### Discover 阶段（发现方向）

| 人物 | 核心智慧 | 对 Carpe Diem 的作用 |
|------|---------|-------------------|
| Paul Graham | 从自身摩擦出发、"脏活测试"、做不规模化的手工事 | 引导用户从个人生活摩擦找方向 |
| Rob Fitzpatrick | Mom Test——聊用户的生活，不聊自己的想法 | 帮用户区分"承诺信号"和"礼貌性赞美" |
| Clayton Christensen | JTBD——用户"雇用"产品完成工作 | 帮用户从功能/社交/情感三维度描述机会 |
| Peter Thiel | 从 0 到 1——秘密测试、垄断定位 | 帮用户问"为什么没人做这个" |
| Jason Fried & DHH | Scratch your own itch、最小切口、可持续性 | 帮用户用"不做什么"检验方向 |

### Validate 阶段（验证假设）

| 人物 | 核心智慧 | 对 Carpe Diem 的作用 |
|------|---------|-------------------|
| Eric Ries | Build-Measure-Learn 验证循环 | 验证流程的基础框架 |
| Steve Blank | Customer Development——走出办公室 | 不能只靠桌面研究 |
| Ash Maurya | Lean Canvas——风险排序 | 帮用户优先验证最危险的假设 |
| David Bland | Test Card——实验系统化 | 把假设写成可测试的"如果…那么…" |
| Cindy Alvarez | 低成本持续验证 | 验证不是一次性活动 |

**经典验证案例**：Zappos（手工拍照验证）、Dropbox（视频验证）、Buffer（落地页先行）、Groupon（手工 PDF 优惠券）、Food on the Table（跟用户回家）、AppSumo（手工测试）、Dollar Shave Club（手工打包）、Product Hunt（手工邀请）、Kickstarter（视频验证）、Gumroad（MVP 落地页）

### Plan 阶段（制定计划）

| 人物 | 核心智慧 | 对 Carpe Diem 的作用 |
|------|---------|-------------------|
| Ryan Singer (Shape Up) | Appetite 约束、Hill Chart 确定性分级 | 限制时间，而非限制范围 |
| Eric Evans (DDD) | Bounded Context、Ubiquitous Language | 上下文边界和统一语言 |
| Michael Nygard (Release It!) | 生产环境实战、容错设计 | 计划要考虑崩溃和恢复 |
| Frederick Brooks (Mythical Man-Month) | Brooks 定律、没有银弹 | 计划和实际是不同的 |
| Martin Fowler (Refactoring) | 技术债务、持续重构 | 计划要包含重构周期 |
| Simon Brown (C4 Model) | 架构可视化——Context/Container/Component/Code | 沟通架构的通用语言 |
| Richard Rumelt (Good Strategy) | 诊断→方针→连贯行动 | 战略不是目标，是连贯行动 |
| Alistair Cockburn (Agile) | 不确定性的三个层次 | 按不确定性级别选择计划方法 |

### Track 阶段（追踪进度）

| 人物 | 核心智慧 | 对 Carpe Diem 的作用 |
|------|---------|-------------------|
| Gene Kim (The Phoenix Project) | 三步工作法——流动/反馈/持续学习 | 追踪不再是"老板看你完没完成" |
| Nicole Forsgren (Accelerate) | 四种关键指标——部署频率/变更前置时间/变更失败率/恢复时间 | 用指标驱动决策 |
| David J. Anderson (Kanban) | 可视化工作流、WIP 限制、瓶颈管理 | 可视化进度并识别瓶颈 |
| Eliyahu Goldratt (The Goal) | Theory of Constraints——找到并消除瓶颈 | 把约束作为追踪焦点 |
| Kent Beck (XP/TDD) | 测试驱动、持续集成、简单设计 | 追踪质量信号 |
| Ryan Singer (Shape Up) | Hill Chart——不确定性可视化 | 把"不知道"也画出来 |

### 跨阶段通用

| 人物 | 核心智慧 | 对 Carpe Diem 的作用 |
|------|---------|-------------------|
| DHH (Rework) | 减法思维、默认说不、不要做大 | 贯穿所有阶段的决策原则 |
| John Ousterhout (A Philosophy of Software Design) | 复杂度管理——每次改动都在降低复杂度 | 复杂度是持续的敌人 |
| Geoffrey Moore (Crossing the Chasm) | 滩头阵地——先攻一个窄市场再扩张 | 市场聚焦策略 |
| Paul Graham (Maker's Schedule) | 创造者日程 vs 管理者日程 | 保护创造者的连续工作块 |

**跨阶段项目案例**：GitHub（从周末项目到收购）、Airbnb（从充气床垫到上市）、Superhuman（从邮件到 PMF 标杆）、Stripe（从开发者 API 到支付巨头）

---

## 三、产出成果

### 3.1 研究文件（6 份）

| 文件 | 内容 | 行数 |
|------|------|------|
| `references/wisdom/researcher-t1-discover-sources.md` | Discover 阶段 5 位思想领袖研究 | 227 |
| `references/wisdom/researcher-t2-validate-sources.md` | Validate 阶段 6 位人物 + 10 个验证案例 | ~200+ |
| `docs/research/2026-08-30-plan-stage-wisdom-sources.md` | Plan 阶段 8 位思想领袖研究 | ~200+ |
| `docs/research/2026-08-30-track-stage-wisdom-sources.md` | Track 阶段 6 位人物研究 | ~200+ |
| `docs/research/2026-08-30-cross-stage-wisdom-sources.md` | 跨阶段 4 位人物 + 4 个项目案例 | ~200+ |
| **`docs/wisdom-distillation-plan.md`** | **综合规划蓝图（汇总文件）** | **549** |

### 3.2 行为卡（33 张 — 全阶段完成）

| 阶段 | 卡片 | 文件 | 行数 | 关键问题 |
|------|------|------|------|---------|
| **Discover** | Mom Test | `mentors/discover/mom-test.md` | 63 | 如何区分真实需求和礼貌性赞美 |
| **Discover** | Scratch Your Itch | `mentors/discover/scratch-your-itch.md` | 70 | 如何从个人摩擦发现方向 |
| **Discover** | 工作陈述 | `mentors/discover/jtbd-work-statement.md` | 83 | 如何用"情境+进展+替代方案"定义方向 |
| **Discover** | 反共识检验 | `mentors/discover/secret-test.md` | 80 | 如何用反共识问题检验方向独特性，避免在热门赛道中盲目跟随 |
| **Discover** | 脏活测试 | `mentors/discover/dirty-work-test.md` | 87 | 如何用"脏活指数"判断方向是否因为没人愿意做而有独特机会 |
| **Validate** | Test Card | `mentors/validate/test-card.md` | 158 | 如何把假设写成可测试的预测 |
| **Validate** | Handmade First | `mentors/validate/handmade-first.md` | 141 | 如何不写代码就验证需求 |
| **Validate** | 行为信号 | `mentors/validate/behavior-signal.md` | 167 | 如何区分态度信号和行为信号，只基于行为做决策 |
| **Validate** | 持续验证 | `mentors/validate/continuous-check.md` | 198 | 如何把验证从一次性事件变成持续节奏 |
| **Plan** | 战略内核 | `mentors/plan/strategy-kernel.md` | — | 如何把"列目标"变成"诊断→方针→行动" |
| **Plan** | 时间预算约束 | `mentors/plan/appetite-constraint.md` | — | 如何先定时间预算再定范围 |
| **Plan** | 架构可视化 | `mentors/plan/c4-architecture.md` | — | 如何从系统上下文图逐层展开架构 |
| **Plan** | 上下文边界 | `mentors/plan/bounded-context.md` | 106 | 如何按业务职责划分模块边界，建立术语表 |
| **Plan** | ADR 增强 | `mentors/plan/adr-rfc-enhance.md` | 102 | 如何用"未解决问题"和"采用策略"字段让 ADR 从文档走向落地 |
| **Plan** | Pitch 格式 | `mentors/plan/pitch-format.md` | 100 | 如何用"问题、时间预算、方案、风险陷阱、非目标"五要素统一计划格式 |
| **Plan** | 稳定性设计模式 | `mentors/plan/stability-patterns.md` | 95 | 如何用断路器、舱壁隔离、超时/重试/幂等方式确保系统优雅降级 |
| **Plan** | 测试优先 | `mentors/plan/test-first.md` | 110 | 如何把测试从"验证"变为"安全网"，用分支覆盖保障重构安全 |
| **Plan** | 文档即交付物 | `mentors/plan/document-as-deliverable.md` | 92 | 如何把文档列为里程碑交付物，确保代码和文档同步提交 |
| **Track** | 确定性分级 | `mentors/track/certainty-level.md` | — | 如何用确定性等级替代完成百分比 |
| **Track** | WIP 检测 | `mentors/track/wip-detection.md` | — | 如何检测在制品数量并减少上下文切换 |
| **Track** | 约束诊断 | `mentors/track/constraint-diagnosis.md` | — | 如何找到并消除瓶颈 |
| **Track** | 四种量化指标 | `mentors/track/four-metrics.md` | 260 | 如何用四个指标替代"感觉"判断项目健康度 |
| **Track** | 里程碑状态 | `mentors/track/milestone-state.md` | 265 | 如何用测试证据和集成频率判断真实完成状态 |
| **Track** | 心跳 | `mentors/track/heartbeat.md` | 277 | 如何建立"流动→反馈→学习"的持续追踪脉搏 |
| **Track** | 集成健康度 | `mentors/track/integration-health.md` | 280 | 如何用集成频率、分支老化、合并粒度、CI 通过率评估项目真实流动状态 |
| **Track** | 定期发车 | `mentors/track/regular-departure.md` | 245 | 如何用固定时间表替代范围承诺，让交付节奏可预测 |
| **Track** | 价值流 | `mentors/track/value-stream.md` | 320 | 如何从想法到交付全流程成像，量化等待时间，定位偏差环节 |
| **Cross** | Beachhead | `mentors/cross/beachhead.md` | 72 | 如何先攻窄市场再扩张 |
| **Cross** | Say No By Default | `mentors/cross/say-no-by-default.md` | 71 | 如何用减法做决策 |
| **Cross** | 复杂度预算 | `mentors/cross/complexity-budget.md` | 125 | 如何评估每个改动的复杂度成本，避免失控 |
| **Cross** | 手工服务不扩展 | `mentors/cross/handmade-validation.md` | 112 | 如何在自动化之前先亲手服务用户，用不可扩展的手工服务获取深度反馈 |
| **Cross** | PMF 满意度调查 | `mentors/cross/pmf-survey.md` | 111 | 如何用"如果不能再使用，你会多失望"调查和 40% 阈值判断 PMF |
| **Cross** | 用户行为指标 | `mentors/cross/user-behavior-metric.md` | 133 | 如何区分虚荣指标和可行动指标，用同期群分析指导决策 |

### 3.3 索引与集成

| 文件 | 内容 | 行数 |
|------|------|------|
| `references/wisdom/mentors/README.md` | 行为卡索引（33 张）、阶段匹配规则、触发条件匹配规则 | 128 |
| `SKILL.md`（已更新） | 步骤 6 扩展为双类智慧卡片加载机制，涵盖全阶段 33 张行为卡 | — |

---

## 四、完成状态一览

```
阶段划分：        Discover → Validate → Plan → Track → 跨阶段
研究完成：          ✅         ✅        ✅       ✅       ✅
规划文档：          ✅         ✅        ✅       ✅       ✅

卡片实现：
  第一阶段（核心）:  ✅ 6 张 — mom-test, scratch-your-itch, test-card, 
                               handmade-first, beachhead, say-no-by-default
  第二阶段（计划）:  ✅ 已集成 — strategy-kernel, appetite-constraint, c4-architecture
                               (由第三阶段合并交付)
  第三阶段（追踪+深化）: ✅ 14 张 — certainty-level, wip-detection, constraint-diagnosis,
                               jtbd-work-statement, behavior-signal, continuous-check,
                               bounded-context, four-metrics, milestone-state, 
                               heartbeat, complexity-budget
  第四阶段（完善与扩展）: ✅ 13 张 — secret-test, dirty-work-test,
                                adr-rfc-enhance, pitch-format, stability-patterns,
                                test-first, document-as-deliverable,
                                integration-health, regular-departure, value-stream,
                                handmade-validation, pmf-survey, user-behavior-metric
  总计: 33 张 — 全阶段完成 ✅
```

---

## 五、蒸馏路线图

```
第一阶段（已完成 ✅）：
  discover/mom-test          — 源自 Rob Fitzpatrick
  discover/scratch-your-itch — 源自 Paul Graham + Jason Fried/DHH
  validate/test-card         — 源自 David Bland
  validate/handmade-first   — 源自 Zappos/Dropbox/Buffer 等 10 个验证案例
  cross/beachhead            — 源自 Geoffrey Moore
  cross/say-no-by-default    — 源自 DHH + Jason Fried

第二阶段（已完成 ✅）：
  plan/strategy-kernel       — 源自 Richard Rumelt
  plan/appetite-constraint   — 源自 Ryan Singer (Shape Up)
  plan/c4-architecture       — 源自 Simon Brown
  track/certainty-level      — 源自 Ryan Singer (Hill Chart)
  track/wip-detection        — 源自 David J. Anderson (Kanban)
  track/constraint-diagnosis — 源自 Eliyahu Goldratt

第三阶段（已完成 ✅）：
  discover/jtbd-work-statement  — 源自 Clayton Christensen
  validate/behavior-signal      — 源自 Steve Blank + Eric Ries
  validate/continuous-check     — 源自 Cindy Alvarez
  plan/bounded-context          — 源自 Eric Evans
  track/four-metrics            — 源自 Nicole Forsgren
  track/milestone-state         — 源自 Kent Beck (XP)
  track/heartbeat               — 源自 Gene Kim (DevOps)
  cross/complexity-budget       — 源自 John Ousterhout

第四阶段（已完成 ✅）：
  discover/secret-test            — 源自 Peter Thiel
  discover/dirty-work-test        — 源自 Paul Graham
  plan/adr-rfc-enhance            — 源自 Michael Nygard
  plan/pitch-format               — 源自 Ryan Singer (Shape Up)
  plan/stability-patterns         — 源自 Michael Nygard
  plan/test-first                 — 源自 Kent Beck (XP)
  plan/document-as-deliverable    — 源自 Martin Fowler
  track/integration-health        — 源自 Kent Beck (XP) + Gene Kim
  track/regular-departure         — 源自 Ryan Singer (Shape Up)
  track/value-stream              — 源自 David J. Anderson (Kanban)
  cross/handmade-validation      — 源自 Paul Graham + 经典验证案例
  cross/pmf-survey                — 源自 Superhuman 等 PMF 方法
  cross/user-behavior-metric      — 源自 Nicole Forsgren + Eric Ries
```

---

## 六、关键数字

| 指标 | 数字 |
|------|------|
| 研究覆盖的人物 | **24 位** |
| 研究覆盖的项目/书籍案例 | **16 个** |
| 研究文件总行数 | **~1,400+ 行** |
| 规划文档 | **549 行** |
| 已创建的行为卡 | **33 张** |
| 已完成的行为卡行数 | **~3,500+ 行** |
| 规划中的总卡片数 | **33 张**（P0: 12 + P1: 14 + P2: 7） |
| 总卡片完成率 | **100%**（33/33） |

---

*本文档随智慧蒸馏工作持续推进而更新。*