# 行为卡（Mentor 卡片）

> 这些卡片是 Carpe Diem 的"行为导师"——在特定阶段触发时，提供可操作的行为指导。
> 每张卡片回答：**当前最应该做什么，不做什么，以及为什么。**

行为卡的结构统一为：
1. **问题本质** — 为什么这个行为很重要
2. **触发条件** — 什么情况下该激活这张卡
3. **行为指导** — 具体该怎么做（可操作步骤）
4. **不适用场景** — 什么时候不该用

## 卡片总览

### Discover 阶段

| 卡片 | 触发条件 | 为您解决的问题 |
|------|---------|--------------|
| [Mom Test — 识别用户反馈中的真实信号](discover/mom-test.md) | 用户正在收集方向反馈，或因为"很多人说好"而决定推进 | 区分"礼貌性赞美"和"真实需求信号"，避免被虚假反馈误导 |
| [从自身摩擦出发找项目](discover/scratch-your-itch.md) | 用户说"不知道做什么方向"，或花大量时间研究市场报告 | 从个人生活摩擦中发现真实方向，而非从热门赛道分析切入 |
| [用工作陈述定义方向](discover/jtbd-work-statement.md) | 用户在形成机会地图，但描述方式是"做一个 XX 产品"而非"解决 XX 问题" | 把"产品描述"转化为"工作陈述"，从情境、进展、替代方案三个维度定义方向 |
| [反共识检验](discover/secret-test.md) | 用户评估方向时关注"市场规模"和"竞争强度"，忽略了"独特性"维度 | 用反共识问题检验方向是否真正独树一帜，避免在热门赛道中盲目跟随 |
| [脏活测试](discover/dirty-work-test.md) | 用户倾向于选择"听起来很酷"的方向而非"看起来无聊"的方向 | 用"脏活指数"判断方向是否因为没人愿意做而有独特机会 |

### Validate 阶段

| 卡片 | 触发条件 | 为您解决的问题 |
|------|---------|--------------|
| [假设验证卡](validate/test-card.md) | 用户在 Validate 阶段列出待验证假设 | 把模糊假设写成可测试的预测，让验证结果不再模棱两可 |
| [手工验证优先](validate/handmade-first.md) | 用户考虑"先做个原型"来验证想法 | 不写一行代码就测试用户是否愿意付钱，用最小成本获得最大学习 |
| [行为信号](validate/behavior-signal.md) | 用户收集到反馈（尤其是正面反馈）并准备以此做决策 | 区分"态度信号"（用户说好）和"行为信号"（用户做了什么），只基于行为信号做决策 |
| [持续验证](validate/continuous-check.md) | Validate 阶段完成并进入 Plan 阶段，或项目推进过程中出现新假设 | 把验证从"一次性事件"变成"贯穿项目始终的节奏"，设置验证保质期和重新验证条件 |

### Plan 阶段

| 卡片 | 触发条件 | 为您解决的问题 |
|------|---------|--------------|
| [战略内核](plan/strategy-kernel.md) | Plan 阶段用户提供的是"功能清单"而非"核心挑战" | 把"列目标"变成"诊断核心挑战→制定指导方针→规划一致行动" |
| [时间预算约束](plan/appetite-constraint.md) | Plan 阶段规划里程碑范围时，用户先列功能清单再估算时间 | 先定时间预算再定范围，让范围去适应时间而非让时间去适应范围 |
| [架构可视化](plan/c4-architecture.md) | Plan 阶段进入架构章节时，用户直接讨论技术选型而非系统全貌 | 从系统上下文图开始逐层展开，确保可版本化、可 Diff 审查 |
| [上下文边界](plan/bounded-context.md) | Plan 阶段进入"架构、组件、数据流"章节，按技术层而非业务职责划分模块 | 按业务职责划分模块边界，建立术语表，明确接口契约 |
| [ADR 增强](plan/adr-rfc-enhance.md) | Plan 阶段进入"架构决策"章节，用户编写或评审 ADR 时 | 在 ADR 中增加"未解决问题"和"采用策略"字段，让决策从文档走向落地 |
| [Pitch 格式](plan/pitch-format.md) | Plan 阶段组织章节结构时，各章节格式不统一 | 用"问题、时间预算、方案、风险陷阱、非目标"五要素统一计划章节格式 |
| [稳定性设计模式](plan/stability-patterns.md) | Plan 阶段架构涉及外部依赖或多服务时，未讨论故障场景 | 用断路器、舱壁隔离、超时/重试/幂等方式保护系统，确保故障时优雅降级 |
| [测试优先](plan/test-first.md) | Plan 阶段进入"测试策略"章节，或用户说"测试后面再补" | 把测试从"验证"变为"安全网"，用分支覆盖和回归测试保障重构安全 |
| [文档即交付物](plan/document-as-deliverable.md) | Plan 阶段定义交付物时，只列出了"代码功能"未包含"文档" | 把文档列为里程碑交付物，确保代码和文档同步提交、同步验收 |

### Track 阶段

| 卡片 | 触发条件 | 为您解决的问题 |
|------|---------|--------------|
| [确定性分级](track/certainty-level.md) | Track 阶段开始报告里程碑进度时 | 区分"上坡（还不知怎么做）"和"下坡（知道怎么做）"，用确定性等级替代完成百分比 |
| [WIP 检测](track/wip-detection.md) | Track 阶段发现多个里程碑同时处于"进行中"状态 | 统计在制品数量，超过阈值时建议集中推进，减少上下文切换 |
| [约束诊断](track/constraint-diagnosis.md) | Track 阶段发现进度偏差，里程碑卡在同一个环节 | 找到并消除瓶颈，用约束决定整个项目的节奏 |
| [四种量化指标](track/four-metrics.md) | Track 阶段需要判断项目整体健康度时 | 用合并频率、前置时间、变更失败率、恢复时间四个信号替代"感觉"，辅助判断项目状态 |
| [里程碑状态](track/milestone-state.md) | Track 阶段检查里程碑是否真正完成时 | 用测试证据、集成频率和 CI 状态替代"声称完成"，判断里程碑的真实完成状态 |
| [心跳](track/heartbeat.md) | Track 阶段开始执行时，建立持续反馈循环 | 用"流动→反馈→学习"的三段式循环替代单向汇报，让每次 Track 都是上一次心跳的延续 |
| [集成健康度](track/integration-health.md) | Track 阶段采集流动证据时，发现代码在分支上累积或合并冲突增多 | 用集成频率、分支老化、合并粒度、CI 首次通过率四个维度评估项目真实流动状态 |
| [定期发车](track/regular-departure.md) | 特性超出预期时间或交付时间被多次推迟时 | 用固定时间表替代范围承诺，让交付节奏可预测 |
| [价值流](track/value-stream.md) | Track 阶段发现进度偏差，需要定位"问题出在哪个环节" | 从想法到交付的全流程成像，量化等待时间，定位偏差在哪一环 |

### 跨阶段通用

| 卡片 | 触发条件 | 适用阶段 | 为您解决的问题 |
|------|---------|---------|--------------|
| [先攻一个窄市场再扩张](cross/beachhead.md) | Discover 评估方向/ Track 完成里程碑后考虑下一步 | Discover, Track | 找到"能赢的细分市场"而非"最大的市场"，先聚焦再扩张 |
| [默认说"不"](cross/say-no-by-default.md) | 任何阶段面临"要不要加功能/方向/范围"的决策 | 全阶段 | 用减法思维做决策——知道拒绝什么比知道加什么更重要 |
| [复杂度预算](cross/complexity-budget.md) | 任何阶段面临"要不要加这个功能/模块/依赖"的决策，或审查架构变更时 | 全阶段 | 评估每个改动的复杂度成本，避免复杂度失控，用"深模块"替代"浅模块" |
| [手工服务不扩展](cross/handmade-validation.md) | Cross 阶段考虑扩大用户规模时，或用户想先做自动化而非手工服务 | Validate, Cross | 在自动化之前先亲手服务用户，用不可扩展的手工服务获取深度反馈和信任 |
| [PMF 满意度调查](cross/pmf-survey.md) | Cross 阶段需要判断产品是否达到产品-市场匹配时 | Cross, Track | 用"如果不能再使用，你会多失望"简洁调查和 40% 阈值判断是否达到 PMF |
| [用户行为指标](cross/user-behavior-metric.md) | Cross 阶段评估产品健康度时，用户在看"总用户数"等虚荣指标 | Cross, Track | 区分虚荣指标和可行动指标，用同期群分析和关键行为时刻指导决策 |

## 自动加载规则

SKILL.md 的"每次调用"流程第6步会根据当前阶段自动匹配并加载行为卡。

### 阶段匹配规则

| 当前阶段 | 自动加载的卡片 | 匹配逻辑 |
|----------|--------------|---------|
| **Discover** | `discover/mom-test`, `discover/scratch-your-itch`, `discover/jtbd-work-statement`, `discover/secret-test`, `discover/dirty-work-test`, `cross/beachhead`, `cross/say-no-by-default`, `cross/complexity-budget`, `cross/handmade-validation`, `cross/pmf-survey`, `cross/user-behavior-metric` | 所有 Discover 阶段卡 + 跨阶段通用卡 |
| **Validate** | `validate/test-card`, `validate/handmade-first`, `validate/behavior-signal`, `validate/continuous-check`, `cross/say-no-by-default`, `cross/complexity-budget`, `cross/handmade-validation`, `cross/pmf-survey`, `cross/user-behavior-metric` | 所有 Validate 阶段卡 + 跨阶段通用卡 |
| **Plan** | `plan/strategy-kernel`, `plan/appetite-constraint`, `plan/c4-architecture`, `plan/bounded-context`, `plan/adr-rfc-enhance`, `plan/pitch-format`, `plan/stability-patterns`, `plan/test-first`, `plan/document-as-deliverable`, `cross/beachhead`, `cross/say-no-by-default`, `cross/complexity-budget`, `cross/handmade-validation`, `cross/pmf-survey`, `cross/user-behavior-metric` | 所有 Plan 阶段卡 + 跨阶段通用卡 |
| **Track** | `track/certainty-level`, `track/wip-detection`, `track/constraint-diagnosis`, `track/four-metrics`, `track/milestone-state`, `track/heartbeat`, `track/integration-health`, `track/regular-departure`, `track/value-stream`, `cross/beachhead`, `cross/say-no-by-default`, `cross/complexity-budget`, `cross/handmade-validation`, `cross/pmf-survey`, `cross/user-behavior-metric` | 所有 Track 阶段卡 + 跨阶段通用卡 |

### 触发条件匹配

除了按阶段自动加载外，当用户的状态或对话触发某张卡片的**触发条件**时，也应加载该卡片（即使当前阶段不是该卡片的主阶段）：

- 用户说"很多人在做这个方向，但我们可以做得更好" → 加载 `secret-test`
- 用户说"这个方向太 boring 了，不值得做" → 加载 `dirty-work-test`
- 用户说"很多人说这个方向好" → 加载 `mom-test`
- 用户说"不知道做什么" → 加载 `scratch-your-itch`
- 用户在形成机会地图时描述方式是"做一个 XX 产品"而非"解决 XX 问题" → 加载 `jtbd-work-statement`
- 用户说"我的想法确实很好，很多人说不错" → 加载 `behavior-signal`
- 用户说"Validate 已经通过了，可以安心推进了" → 加载 `continuous-check`
- 用户说"这个功能加上去应该会有人用" → 加载 `say-no-by-default`
- 用户说"这个市场太小了" → 加载 `beachhead`
- 用户说"先做出来再说，后面再优化" → 加载 `complexity-budget`
- 用户在架构审查时发现"模块接口太多，但内部处理很浅" → 加载 `complexity-budget`
- 用户在 Validate 阶段列出假设 → 加载 `test-card`
- 用户说"我想先做个原型" → 加载 `handmade-first`
- 用户提供的是"功能清单"而非"核心挑战" → 加载 `strategy-kernel`
- 用户先列功能清单再问"需要多少时间" → 加载 `appetite-constraint`
- 用户直接讨论技术选型而非系统全貌 → 加载 `c4-architecture`
- 用户按技术层划分模块，而非按业务职责 → 加载 `bounded-context`
- 用户编写或评审 ADR 时，发现"决策看起来没问题，但不知道具体怎么落地" → 加载 `adr-rfc-enhance`
- 用户说"我们先列一下计划需要包含哪些章节" → 加载 `pitch-format`
- 用户说"这个外部服务应该很稳定，不太可能出问题" → 加载 `stability-patterns`
- 用户说"测试后面再补" 或 "这部分代码我不敢动" → 加载 `test-first`
- 用户说"这个功能很简单，不需要文档" 或 "文档下次补上" → 加载 `document-as-deliverable`
- 用户报告"感觉一直在做，但好像没完成什么" → 加载 `wip-detection`
- 用户说"不知道哪个环节拖了后腿" → 加载 `constraint-diagnosis`
- 用户说"感觉项目进展不错" 或 "项目好像变慢了" → 加载 `four-metrics`
- 用户说"这个功能做完了" 或 "代码写完了，但还没来得及测试" → 加载 `milestone-state`
- 用户说"上次 Track 说的问题还在吗" 或 "感觉同样的偏差出现了好几次" → 加载 `heartbeat`
- 用户说"代码写完了，但还没合并" 或 "合并的时候出了很多冲突" → 加载 `integration-health`
- 用户说"这个特性快做完了，再等两天就好" 或 "再加一个小功能" → 加载 `regular-departure`
- 用户说"代码写完了，但还在等测试/审查/部署" 或 "感觉一直在做，但好像没完成什么" → 加载 `value-stream`
- 用户说"我们要把这个流程自动化" 或 "手工服务太慢，效率太低" → 加载 `handmade-validation`
- 用户说"产品应该达到 PMF 了" 或 "不确定是否准备好扩大规模" → 加载 `pmf-survey`
- 用户在看"总用户数"、"总浏览量"、"总下载量"来判断产品健康度 → 加载 `user-behavior-metric`

### 加载方式

1. 先阅读本文件了解可用卡片
2. 根据当前阶段和用户对话状态，选择匹配的卡片
3. 加载卡片后，在对话中自然引用其行为指导，而非生硬照搬
4. 一张卡片的内容可以合并到当前阶段的引导中，而不是单独作为"卡片的引用"