# Carpe Diem Plan & Track 阶段智慧来源研究

> 研究日期：2026-08-30
> 研究范围：Plan 阶段（打磨完整实施计划）与 Track 阶段（记录开发进度与计划偏差）对应的思想领袖、书籍和项目
> 研究目的：确定哪些人、书、项目的智慧可以蒸馏为 Carpe Diem 的 Agent 行为，使 Plan 阶段产出更可靠的实施计划，Track 阶段更准确地识别偏差

## 目录

- [核心发现](#核心发现)
- [人物研究](#人物研究)
  - [1. Ryan Singer — Shape Up](#1-ryan-singer--shape-up)
  - [2. Eric Evans — Domain-Driven Design](#2-eric-evans--domain-driven-design)
  - [3. Michael Nygard — Release It!](#3-michael-nygard--release-it)
  - [4. Frederick Brooks — The Mythical Man-Month](#4-frederick-brooks--the-mythical-man-month)
  - [5. Martin Fowler — Refactoring](#5-martin-fowler--refactoring)
  - [6. Simon Brown — C4 Model](#6-simon-brown--c4-model)
  - [7. Richard Rumelt — Good Strategy/Bad Strategy](#7-richard-rumelt--good-strategybad-strategy)
  - [8. Alistair Cockburn — Hexagonal Architecture](#8-alistair-cockburn--hexagonal-architecture)
- [项目案例研究](#项目案例研究)
  - [1. Basecamp — Shape Up 流程](#1-basecamp--shape-up-流程)
  - [2. Linux Kernel — 治理模型](#2-linux-kernel--治理模型)
  - [3. React — RFC 流程](#3-react--rfc-流程)
  - [4. SQLite — 测试哲学](#4-sqlite--测试哲学)
  - [5. PostgreSQL — 社区治理](#5-postgresql--社区治理)
- [Plan 阶段智慧蒸馏建议](#plan-阶段智慧蒸馏建议)
- [Track 阶段智慧蒸馏建议](#track-阶段智慧蒸馏建议)
- [综合推荐行动卡](#综合推荐行动卡)

---

## 核心发现

1. **Plan 阶段最急需的智慧不是"如何写计划"，而是"如何让计划可执行、可验证、可调整"**。Carpe Diem 的 Plan 阶段已经有完整的章节结构（定位→体验→架构→ADR→测试→里程碑→协议），但缺少的是：**约束机制**（Shape Up 的 appetite）、**战略连贯性**（Rumelt 的 kernel）、**架构描述语言**（C4 的上下文/容器/组件/代码）。
2. **Track 阶段最缺的是"不确定性可视化"**。现有 Track 阶段依赖 Git/测试/CI 等客观证据，但没有 Hill Chart 这样的工具来区分"还在弄清怎么做"和"知道怎么做"。
3. **项目案例比人物更值得蒸馏**。Linux Kernel 的 subsystem maintainer 模型、React 的 RFC 流程、SQLite 的测试哲学——这些是已经运行多年的工程实践，有明确的机制和结果，比个人观点更适合转成 Agent 行为。

---

## 人物研究

### 1. Ryan Singer — Shape Up

**核心著作**：[Shape Up: Stop Running in Circles and Ship Work that Matters](https://basecamp.com/shapeup)（Basecamp 免费在线出版，2019）

**核心智慧**：

| 概念 | 说明 | 对 Carpe Diem 的价值 |
|------|------|---------------------|
| **Appetite（胃口/投入上限）** | 先固定时间预算，再确定范围。不是"需要多少时间"，而是"我们愿意投入多少"。 | Plan 阶段每个里程碑都应声明 appetite，防止范围膨胀 |
| **Pitch（提案）** | 包含问题、appetite、方案、风险陷阱（rabbit holes）、非目标（no-gos）的结构化提案 | Plan 阶段的"目标与非目标"章节可以借鉴 pitch 格式 |
| **Hill Chart（山丘图）** | 横轴=时间，纵轴=确定性。上坡=仍在弄清怎么做，下坡=知道怎么做，只做任务计数掩盖未知 | Track 阶段最缺失的工具，可以转为"证据确定性"分级 |
| **Fixed time, variable scope** | 固定截止日期，调整范围而非延期 | 防止"计划延期→更多计划→继续延期"的恶性循环 |
| **Betting Table（投注桌）** | 每周期开始时的决策会议，选择下一个周期的项目 | 对应 Carpe Diem 的"下一阶段交接建议"决策点 |
| **Set boundaries（设边界）** | 明确范围允许什么、不允许什么，让团队自主裁量 | 对应 Plan 阶段的"非目标"和"禁止范围" |

**对 Carpe Diem Plan 阶段的启发**：

1. **Appetite 约束**：每个里程碑必须声明 `appetite: N 天/周`，以及 `must-have` / `nice-to-have` / `cuttable` 三层范围。当范围超出 appetite 时，默认操作是缩小范围而非延长。
2. **Pitch 式提案**：Plan 阶段的每个章节（架构、测试、里程碑）都应先以 pitch 格式呈现：`问题 → 投入上限 → 方案 → 已知风险 → 非目标`，再让用户确认。
3. **Rabbit holes 预识别**：在 Plan 阶段明确列出最可能拖延的陷阱场景，以及触发后如何降级（缩小范围、暂停、求助）。

**对 Carpe Diem Track 阶段的启发**：

1. **Hill Chart 确定性分级**：将现有"有证据完成/声称完成/未完成/无法判断"四类状态，扩展为"确定性等级"：上坡（仍有关键未知）、下坡（已知怎么做）、已完成。只有当任务进入下坡后，进度才可信。
2. **不把任务完成数当进度**：Shape Up 最核心的教训——"花了 3 周，完成了 80% 的任务"不等于"80% 完成"。Track 应报告"哪些已进入下坡"和"上坡还剩哪些未知"。

**可蒸馏规则**：
- Plan 阶段：每个里程碑包含 `appetite、must-have、nice-to-have、cuttable、rabbit-holes、no-gos`
- Track 阶段：同时报告交付证据 + 最大未知，把长期不动的范围拆小或重新定义
- 超限时默认缩范围或重新 Plan，而不是悄悄延长

**不可泛化边界**：六周周期、betting table、无 backlog 等是 Basecamp 的组织实践，不应整套照搬；Hill Chart 的主观位置不能替代 Carpe Diem 现有的 Git、测试、CI、Issue 等客观证据。

---

### 2. Eric Evans — Domain-Driven Design

**核心著作**：*Domain-Driven Design: Tackling Complexity in the Heart of Software*（Addison-Wesley, 2003）

**核心智慧**：

| 概念 | 说明 | 对 Carpe Diem 的价值 |
|------|------|---------------------|
| **Ubiquitous Language（通用语言）** | 团队和领域专家使用同一套术语，代码中的命名与业务语言一致 | Plan 阶段"用户体验"章节应产出术语表，ADR 和代码保持术语一致 |
| **Bounded Context（限界上下文）** | 每个模型有明确的边界，不同上下文间的术语可以不同，但映射关系必须显式 | 架构决策的核心工具：模块边界划分、接口契约 |
| **Entity / Value Object / Aggregate** | 区分有身份标识的对象、仅凭属性定义的对象、以及一致性边界 | Plan 阶段"数据流"章节的建模基础 |
| **Domain Event / Event Sourcing** | 用事件记录状态变化 | Track 阶段的事件历史机制（Carpe Diem 已有事件记录，可强化） |
| **Strategic Design（战略设计）** | 在大型系统中划分上下文、定义上下文间的关系（合作关系、共享内核、客户-供应商、防腐层） | 多模块架构计划的核心框架 |

**对 Carpe Diem Plan 阶段的启发**：

1. **限界上下文作为架构模块划分标准**：Plan 阶段"架构、组件、数据流"章节，应先用 bounded context 识别模块边界，再细化内部结构。每个上下文有明确的职责、术语和接口契约。
2. **通用语言产出**：Plan 阶段应产出"项目术语表"（Glossary），确保所有 ADR、里程碑描述、测试用例使用同一套术语。这是防止"开发 Agent 误解需求"的关键。
3. **防腐层（Anti-Corruption Layer）**：当项目依赖外部系统或遗留代码时，Plan 阶段应识别哪些接口需要防腐层，防止外部变化污染核心领域。

**对 Carpe Diem Track 阶段的启发**：

1. **领域事件作为进度证据**：Track 阶段可以匹配"实际发生的事件" vs "计划中的事件序列"，检测偏差。例如"用户注册事件"是否如期发生。
2. **上下文映射变化**：当外部依赖发生变化时，Track 应识别上下文映射是否需要更新。

**可蒸馏规则**：
- Plan 阶段的架构设计，先识别 bounded context，再细化每个 context 的内部结构
- 产出项目术语表，确保 ADR、测试、里程碑使用同一套术语
- 外部依赖接口识别防腐层需求

**不可泛化边界**：DDD 假设有领域专家和业务复杂度；对于简单 CRUD 项目或纯技术工具，DDD 的 tactical patterns（Entity、Value Object、Repository、Factory）可能过度设计；不要求所有项目生成完整的 context map，只在架构复杂度高时使用。

---

### 3. Michael Nygard — Release It!

**核心著作**：*Release It! Design and Deploy Production-Ready Software*（Pragmatic Bookshelf, 2nd Edition 2018）

**核心智慧**：

| 概念 | 说明 | 对 Carpe Diem 的价值 |
|------|------|---------------------|
| **Stability Patterns（稳定性模式）** | Circuit Breaker、Bulkhead、Timeout、Handshaking 等模式 | Plan 阶段"错误处理"章节的核心参考 |
| **Antifragility（反脆弱性）** | 系统不仅应承受压力，还应在压力中变得更强 | Plan 阶段的"风险与降级"设计理念 |
| **Production Readiness Checklist** | 系统上线前的检查清单 | Plan 阶段"验收标准"的补充 |
| **Failure as a Feature** | 把故障作为系统设计的一部分，测试故障路径 | 对应 Carpe Diem Plan 阶段的"错误处理"章节 |
| **Escape Hatch（逃生舱）** | 提供降级路径，让用户在功能不可用时仍能继续 | 里程碑设计时应包含降级路径 |

**对 Carpe Diem Plan 阶段的启发**：

1. **错误处理模式化**：Plan 阶段"错误处理、安全和隐私"章节，可以直接引用 Stability Patterns：每个外部依赖和关键路径，都应指定超时、熔断、隔离策略。
2. **生产就绪检查清单**：在 Plan 阶段末尾生成一份"生产就绪检查清单"，包含：监控、告警、日志、备份、恢复、容量、安全审计等条目。
3. **逃生舱设计**：每个里程碑应有"如果核心功能不可用，用户如何降级使用"的预案。

**可蒸馏规则**：
- 每个外部依赖指定超时、熔断、隔离策略
- 里程碑包含降级路径和逃生舱
- Plan 阶段产出生产就绪检查清单

**不可泛化边界**：主要面向分布式服务和在线系统，不适合单机工具或纯客户端应用；部分模式（如 Circuit Breaker）对短生命周期脚本不适用。

---

### 4. Frederick Brooks — The Mythical Man-Month

**核心著作**：*The Mythical Man-Month: Essays on Software Engineering*（Addison-Wesley, 1975 / Anniversary Edition 1995）

**核心智慧**：

| 概念 | 说明 | 对 Carpe Diem 的价值 |
|------|------|---------------------|
| **Brooks's Law（布鲁克斯法则）** | 给延期的项目加人只会让它更晚 | Plan 阶段的里程碑估计和任务分配原则 |
| **The Second-System Effect** | 第二个系统是开发者最危险的系统——倾向于加入所有第一版没加的功能 | 对应 Plan 阶段"非目标"和"版本边界" |
| **Conceptual Integrity（概念完整性）** | 系统的架构应来自少数统一的设计理念，而非委员会设计 | 架构决策的 ADR 应保持一致性标准 |
| **No Silver Bullet** | 没有能大幅提升软件生产力的单一技术突破 | 对 Plan 阶段"价值假设"的现实检验 |
| **The Tar Pit** | 大型系统的复杂性像沥青坑，部分可避免、部分不可避免 | 里程碑划分应识别"不可避免的复杂性"和"可避免的复杂性" |
| **Plan to Throw One Away** | 第一次构建的系统往往需要重写，但重写前的经验不可或缺 | 对 Plan 阶段"里程碑"设计的现实态度 |

**对 Carpe Diem Plan 阶段的启发**：

1. **里程碑粒度控制**：Brooks 说"更多人手不能加速延期项目"，对 Carpe Diem 的启示是——里程碑的大小应以"单人/双人·周"为粒度，而不是依赖"加人加速"的幻觉。
2. **概念完整性检查**：Plan 阶段完成后，应检查架构决策是否来自统一的设计理念，而不是"委员会式"的折中。ADR 之间不应有内部矛盾。
3. **第二系统效应预防**：对于有经验的开发者，Plan 阶段要特别警惕"第二系统效应"——在首版中加入过多功能。明确"首版目标"和"后续版本"的边界。
4. **抽象层成本**：Brooks 指出"没有银弹"，任何抽象层都有成本。Plan 阶段在选择框架、中间件、抽象层时，应评估其带来的复杂度和成本。

**可蒸馏规则**：
- 里程碑以"单人·周"为粒度，不依赖"加人加速"假设
- 检查所有 ADR 是否来自统一的设计理念，避免内部矛盾
- 对"首版"和"后续版本"设置明确边界，防止第二系统效应
- 评估每个抽象层/框架引入的额外复杂度

**不可泛化边界**：Brooks 的观察基于 1960-70 年代的大型 IBM 系统，与现代微服务、SaaS、开源项目有本质差异；"扔掉的第一个版本"不适用于需要快速验证的 MVP 模式；现代模块化编程和 DevOps 已经改变了部分人力与进度的关系。

---

### 5. Martin Fowler — Refactoring

**核心著作**：*Refactoring: Improving the Design of Existing Code*（Addison-Wesley, 1st Edition 1999 / 2nd Edition 2018）

**核心智慧**：

| 概念 | 说明 | 对 Carpe Diem 的价值 |
|------|------|---------------------|
| **Refactoring Catalog（重构目录）** | 200+ 种经过验证的重构手法，每种有动机、手法、示例 | Plan 阶段"测试策略"的基础——重构需要测试保障 |
| **Test-Driven Development** | 先写测试再写代码，测试是重构的安全网 | Plan 阶段"测试和验收"章节的核心策略 |
| **Continuous Design** | 设计不是一次性完成的，而是持续演进的 | Plan 阶段的设计原则：好的设计是"能持续改进的设计" |
| **Code Smell（代码坏味道）** | 22 种常见的代码质量问题信号 | 可用于 Track 阶段的"质量偏差"检测 |
| **Microservices / Monolith First** | 先做单体，再按需拆分微服务 | 架构决策的默认推荐路径 |

**对 Carpe Diem Plan 阶段的启发**：

1. **测试是重构的前提**：Plan 阶段"测试和验收"章节应明确——测试不仅是验收工具，更是重构安全网。没有充分测试覆盖的模块，不应该在计划中列入"后续重构"。
2. **Bad Smell 作为验收标准之一**：可以借鉴 Code Smell 清单，在 Track 阶段作为"代码质量偏差"的检查信号。
3. **Monolith First 原则**：默认推荐单体架构，只在有明确拆分理由时考虑微服务。这应该成为架构决策 ADR 的默认选项。
4. **Continuous Design 作为 Plan 的约束**：Plan 阶段的设计不是"一次性做完"，而是"设计出能够持续演进的架构"。ADR 应记录"未来可能的变化方向"。

**可蒸馏规则**：
- 架构决策默认推荐单体架构，除非有明确拆分理由
- 测试策略覆盖"重构安全网"需求
- 每个 ADR 包含"未来变化方向"说明

**不可泛化边界**：Fowler 的企业软件开发背景偏向长期维护项目，不适用于一次性脚本或原型；重构目录中的手法需要人工判断适用场景，不适合全部自动化。

---

### 6. Simon Brown — C4 Model

**核心著作**：[C4 Model](https://c4model.com/)（官方网站），*Software Architecture for Developers*（Leanpub）

**核心智慧**：

| 概念 | 说明 | 对 Carpe Diem 的价值 |
|------|------|---------------------|
| **C4 四层模型**：Context → Container → Component → Code | 上下文、容器（进程/服务）、组件、代码的逐层细化 | Plan 阶段"架构"章节的天然描述框架 |
| **Abstraction First（先抽象后具体）** | 先画系统上下文图，再逐层深入 | 架构决策的"先大局后细节"原则 |
| **Diagram as Code（代码即图）** | 用 Structurizr DSL 或 PlantUML 描述架构图 | 架构文档可版本化、可审查 |
| **4+1 视图补充** | 逻辑视图、进程视图、开发视图、物理视图、场景视图 | 为复杂系统提供多维度视角 |
| **Level of Detail（细节粒度）** | 每一层只关注该层的细节，不跨层 | 对应 Plan 阶段"逐章确认"的策略 |

**对 Carpe Diem Plan 阶段的启发**：

1. **C4 作为架构描述的默认框架**：Plan 阶段"架构、组件、数据流"章节，应按照 C4 的层次组织：先画系统上下文图（Context），再画容器/服务图（Container），最后画组件图（Component）。代码层（Code）由开发 Agent 在实现阶段处理。
2. **架构图文本化**：推荐使用 PlantUML 或 Mermaid 生成架构图，作为 ADR 的附件。这样架构图可以版本化、Diff 审查、自动生成。
3. **上下文图优先**：在进入架构细节之前，先完成系统上下文图——明确系统边界、外部依赖、用户角色。这对应 Plan 阶段第 1 步"项目定位"和第 3 步"架构"。

**可蒸馏规则**：
- Plan 阶段架构描述按 C4 层次组织：Context → Container → Component
- 系统上下文图优先于容器/组件细节
- 架构图使用文本格式（PlantUML / Mermaid），可版本化和 Diff

**不可泛化边界**：C4 是描述工具，不是设计方法，不回答"应该用什么架构"的问题；四层架构对于小型项目可能过度细化，可以根据项目复杂度跳过 Container 或 Code 层。

---

### 7. Richard Rumelt — Good Strategy/Bad Strategy

**核心著作**：*Good Strategy/Bad Strategy: The Difference and Why It Matters*（Crown Business, 2011）

**核心智慧**（已在[现有研究](2026-08-30-project-design-wisdom-sources.md)中识别）：

| 概念 | 说明 | 对 Carpe Diem 的价值 |
|------|------|---------------------|
| **Strategy Kernel（战略内核）** | 诊断→指导方针→一致行动 | Plan 阶段"摘要与问题"和"里程碑"章节的核心组织原则 |
| **Proximate Objective（近端目标）** | 可达成的、具体的、有时间限制的目标 | 里程碑的"可达性"标准 |
| **Bad Strategy 的四种特征** | 空话、没有真正面对挑战、把目标当战略、糟糕的战略目标 | Plan 阶段的质量检查清单 |

**对 Carpe Diem Plan 阶段的启发**（已在现有研究中识别）：
- 计划首页强制形成：`诊断：核心挑战是什么 → 指导方针：选择什么总体解法 → 一致行动：哪些里程碑共同落实它`
- 每个行动必须能回指诊断
- 加入"不会做什么"，防止目标列表冒充战略

---

### 8. Alistair Cockburn — Hexagonal Architecture

**核心著作**：*Hexagonal Architecture (Ports & Adapters)*，最初在 2005 年提出

**核心智慧**：

| 概念 | 说明 | 对 Carpe Diem 的价值 |
|------|------|---------------------|
| **Ports and Adapters（端口与适配器）** | 核心业务逻辑通过端口接口与外部世界交互，适配器实现具体技术 | Plan 阶段"架构"章节的模块划分原则 |
| **Dependency Inversion（依赖反转）** | 核心层不依赖外部技术，外部技术依赖核心层定义的接口 | 架构决策 ADR 的核心原则 |
| **Testability（可测试性）** | 核心逻辑可以脱离基础设施独立测试 | Plan 阶段"测试和验收"的基础 |

**对 Carpe Diem Plan 阶段的启发**：
- 架构设计中，核心领域逻辑应通过"端口"与外部世界交互，基础设施为"适配器"
- 这一原则直接提升可测试性——核心逻辑可以在不启动数据库、网络等外部服务的情况下测试

---

## 项目案例研究

### 1. Basecamp — Shape Up 流程

**核心机制**：

| 环节 | 说明 | 可蒸馏的机制 |
|------|------|-------------|
| **六周周期** | 固定六周为一个周期，到期不延期 | 里程碑的固定时间约束 |
| **Betting Table** | 高层每周期开始时选择项目 | 交接包中的"下一阶段选择"决策点 |
| **Pitch 标准化** | 每个提案有固定格式（问题、方案、风险、非目标） | Plan 阶段的章节模板 |
| **Cool-Down 期** | 每个周期结束后有 2 周缓冲，用于修复 bug、探索、学习 | 里程碑之间的"缓冲期"安排 |
| **无 Backlog** | 不维护待办列表，每个周期重新选择 | 避免"计划膨胀"的机制 |
| **独立团队** | 每个团队在周期内专注一个项目，不受干扰 | 任务依赖管理 |

**对 Carpe Diem Plan 阶段的启发**：

1. **固定时间周期**：虽然 Carpe Diem 不强制六周，但每个里程碑应声明固定时间预算（appetite），到期不延期——缩范围。
2. **Pitch 标准化模板**：Plan 阶段的每个章节可以借鉴 pitch 格式：`背景 → 方案 → 已知风险 → 非目标 → 决策`。
3. **Cool-Down 机制**：在里程碑之间安排缓冲期，用于修复、优化和为下一阶段做准备。

**对 Carpe Diem Track 阶段的启发**：

1. **周期回顾**：每个周期/里程碑结束时，Track 应输出"投注桌建议"——哪些方向值得继续，哪些应该放弃。
2. **无 Backlog 原则**：不要因为"计划中有很多事项"而认为进度良好。Track 关注的是"当前周期完成的内容"，而不是"计划列表的完成率"。

---

### 2. Linux Kernel — 治理模型

**核心机制**：

| 环节 | 说明 | 可蒸馏的机制 |
|------|------|-------------|
| **Subsystem Maintainer（子系统维护者）** | 每个子系统有专人负责审查和合并代码 | 模块化治理：每个模块有明确的"负责人" |
| **Linus Torvalds 作为最终仲裁者** | 高层冲突时由 Linus 裁决 | 争议升级路径 |
| **Merge Window（合并窗口）** | 每个发布周期有固定的新功能合并窗口期 | 里程碑的"冻结期"机制 |
| **Test Robot (0-Day)** | 自动化测试机器人持续测试所有提交 | 持续集成检查 |
| **Signed-off-by 链** | 每个提交有完整的责任链标识 | 责任追溯机制 |
| **No Regressions 原则** | 新提交不能引入已有的回归 bug | 里程碑的"不退化"要求 |

**对 Carpe Diem Plan 阶段的启发**：

1. **模块化治理**：Plan 阶段应为每个模块指定"负责人"（开发 Agent 或人类），明确模块边界和维护责任。这对应"架构"章节中模块职责的明确。
2. **合并窗口**：在里程碑计划中，设置"功能冻结期"——新功能只能在窗口期合并，之后只做 bug 修复和稳定化。
3. **No Regressions 原则**：每个里程碑的验收标准应包含"不退化现有功能"的要求。这对应"测试和验收"章节的回归测试。

**对 Carpe Diem Track 阶段的启发**：

1. **责任链追溯**：Track 阶段可以检查提交的"责任链"——是否每个变更都有明确的签名和审查记录。
2. **0-Day 式检查**：Track 阶段可以自动运行 CI 检查，识别回归问题——但不修改工作区。

---

### 3. React — RFC 流程

**核心机制**：

| 环节 | 说明 | 可蒸馏的机制 |
|------|------|-------------|
| **RFC 模板**：摘要、动机、详细设计、缺点、替代方案、采用策略、未解决问题 | 标准化的设计文档格式 | ADR 模板的补充——可以加入"未解决问题"和"采用策略" |
| **公开讨论期**：RFC 提交后公开讨论，收集社区反馈 | Plan 阶段的"用户确认"机制 |
| **Lazy Consensus**：默认同意，除非有明确反对 | 加速决策的机制 |
| **Champion 制度**：每个 RFC 有负责人推动 | 每个 ADR 有"决策人" |
| **渐进式采纳**：RFC 批准后，可以分阶段实现 | 里程碑的"渐进式实施" |

**对 Carpe Diem Plan 阶段的启发**：

1. **RFC 风格的 ADR**：Carpe Diem 的 ADR 模板可以借鉴 RFC 模板的"未解决问题"和"采用策略"字段，记录已知的开放问题和实施路径。
2. **Lazy Consensus**：在用户确认机制中，对于低风险决策，可以默认同意（用户不反对即通过），减少决策疲劳。但这需要与 Carpe Diem 的"逐章确认"机制配合。
3. **Champion 制度**：每个 ADR 应指定"决策人"和"实施负责人"，明确责任。

**可蒸馏规则**：
- ADR 模板增加"未解决问题"和"采用策略"字段
- 低风险决策采用 Lazy Consensus 机制

---

### 4. SQLite — 测试哲学

**核心机制**：

| 环节 | 说明 | 可蒸馏的机制 |
|------|------|-------------|
| **100% Branch Coverage**：行覆盖率目标，实际达到 100% MC/DC | 极致的测试标准 | Plan 阶段"测试和验收"的参考目标 |
| **TH3 测试框架**：专有测试框架，生成百万级测试用例 | 自动化测试基础设施 |
| **Fuzz Testing**：使用 AFL、libFuzzer 等工具进行模糊测试 | 安全测试的补充 |
| **Regression Test Suite**：每个 bug 修复先写回归测试 | 测试优先文化 |
| **测试代码量超产品代码 100 倍**：测试代码约 8 万行，产品代码约 15 万行 | 测试投入的参考比例 |
| **Mostly Bug-Free 承诺**：SQLite 的测试哲学目标是"几乎无 bug" | 质量目标设定 |

**对 Carpe Diem Plan 阶段的启发**：

1. **测试优先文化**：Plan 阶段"测试和验收"应明确——测试不是开发的附属品，而是核心开发活动。每个里程碑应包含"测试用例设计和实现"的任务。
2. **回归测试强制**：在 Plan 阶段建立"每个 bug 修复先写回归测试"的规则。
3. **Fuzz Testing 计划**：对于处理外部输入的项目，Plan 阶段应包含模糊测试计划。

**对 Carpe Diem Track 阶段的启发**：

1. **测试覆盖率趋势**：Track 阶段可以跟踪测试覆盖率的变化，作为质量指标。
2. **回归测试通过率**：回归测试通过率是比"代码行数"更可靠的进度指标。

**可蒸馏规则**：
- 每个里程碑包含"测试用例设计和实现"任务
- 每个 bug 修复必须先写回归测试
- 测试代码量应为产品代码的 1-3 倍（参考 SQLite 的极端比例，但根据项目类型调整）

**不可泛化边界**：SQLite 是嵌入式数据库，其测试标准（100% MC/DC）不适合所有项目类型；SQLite 的测试投入（测试代码:产品代码 = 100:1）是极端案例，非嵌入式项目应有不同的比例。

---

### 5. PostgreSQL — 社区治理

**核心机制**：

| 环节 | 说明 | 可蒸馏的机制 |
|------|------|-------------|
| **Core Team（核心团队）**：7 人核心团队，负责总体方向和决策 | 集中决策模型 |
| **Commit Fest（提交节）**：每季度一次的提交周期，集中审查和合并 | 里程碑的"提交审查"机制 |
| **Patch Review 文化**：每个补丁必须经过严格审查才能合并 | 代码审查制度 |
| **RFC 流程**：重大变更先提交 RFC 讨论 | 架构决策的标准化流程 |
| **Backward Compatibility 承诺**：从不破坏向后兼容 | 版本管理的核心原则 |
| **文档即功能**：文档与代码同等重要，patch 必须包含文档更新 | Plan 阶段的"文档即交付物"原则 |

**对 Carpe Diem Plan 阶段的启发**：

1. **Commit Fest 机制**：Plan 阶段的里程碑可以借鉴 Commit Fest 的"集中审查"模式——在里程碑结束时，集中审查和合并所有变更，而不是"边开发边合并"。
2. **文档即功能**：Plan 阶段明确"文档是交付物的一部分"——每个里程碑的验收标准包含"文档更新完成"。
3. **Backward Compatibility 承诺**：对于有用户的库或框架，Plan 阶段应明确向后兼容的承诺级别。

**对 Carpe Diem Track 阶段的启发**：

1. **Patch Review 追踪**：Track 阶段可以跟踪"审查中的变更"和"已合并的变更"的比例，作为开发质量的指标。
2. **文档覆盖率**：Track 可以检查"新增功能是否有对应的文档更新"。

**可蒸馏规则**：
- 每个里程碑验收标准包含"文档更新完成"
- 向后兼容承诺级别在 Plan 阶段明确声明
- 里程碑结束时设置"集中审查"阶段

---

## Plan 阶段智慧蒸馏建议

### 推荐优先级

| 优先级 | 智慧来源 | 蒸馏为 | 说明 |
|--------|---------|--------|------|
| **P0** | Richard Rumelt — Strategy Kernel | 计划生成检查卡 | 确保计划不是"目标清单"，而是"诊断→指导方针→一致行动" |
| **P0** | Ryan Singer — Appetite + Rabbit Holes | 里程碑约束卡 | 每个里程碑有投入上限、可削减范围和已知陷阱 |
| **P0** | Simon Brown — C4 Model | 架构描述框架 | 架构章节按 Context→Container→Component 组织 |
| **P1** | Eric Evans — Bounded Context | 模块划分卡 | 架构模块按 bounded context 划分 |
| **P1** | React RFC — 未解决问题字段 | ADR 模板增强 | ADR 增加"未解决问题"和"采用策略"字段 |
| **P1** | Ryan Singer — Pitch 格式 | 章节模板卡 | 每个规划章节按 pitch 格式呈现 |
| **P2** | Michael Nygard — Stability Patterns | 错误处理卡 | 外部依赖的熔断、超时、隔离策略 |
| **P2** | Frederick Brooks — 概念完整性 | 计划质量检查卡 | 检查 ADR 间是否有内部矛盾 |
| **P2** | Martin Fowler — 测试是重构前提 | 测试策略卡 | 测试不仅是验收，也是重构安全网 |
| **P2** | SQLite — 回归测试强制 | 测试规则卡 | 每个 bug 修复先写回归测试 |
| **P2** | PostgreSQL — 文档即功能 | 交付物卡 | 文档是交付物的一部分 |

### 核心操作序列

基于以上智慧蒸馏，Plan 阶段的核心操作序列建议为：

```
1. 生成战略内核（Rumelt）：
   - 诊断：核心挑战是什么
   - 指导方针：选择什么总体解法
   - 一致行动：哪些里程碑共同落实它

2. 为每个里程碑设定约束（Shape Up）：
   - appetite：固定时间预算
   - must-have / nice-to-have / cuttable 三层范围
   - rabbit holes：已知陷阱
   - no-gos：明确不做的事

3. 架构描述按 C4 层次组织（C4 Model）：
   - 系统上下文图（Context）
   - 容器/服务图（Container）
   - 组件图（Component）
   - 模块按 bounded context 划分（DDD）

4. 每个架构决策生成 ADR（React RFC 增强）：
   - 包含"未解决问题"和"采用策略"字段
   - ADR 间无内部矛盾（Brooks）

5. 测试策略包含（Fowler + SQLite）：
   - 重构安全网覆盖
   - 回归测试强制
   - 模糊测试计划（如适用）

6. 错误处理包含（Nygard）：
   - 外部依赖的熔断、超时、隔离
   - 逃生舱和降级路径

7. 交付物包含（PostgreSQL）：
   - 文档更新
   - 生产就绪检查清单
```

---

## Track 阶段智慧蒸馏建议

### 推荐优先级

| 优先级 | 智慧来源 | 蒸馏为 | 说明 |
|--------|---------|--------|------|
| **P0** | Ryan Singer — Hill Chart | 确定性分级卡 | 区分"仍在弄清怎么做"和"知道怎么做" |
| **P1** | Shape Up — 不把任务完成数当进度 | 进度报告卡 | 报告"哪些已进入下坡"和"上坡还剩哪些未知" |
| **P1** | SQLite — 回归测试通过率 | 质量指标卡 | 用回归测试通过率作为进度指标之一 |
| **P2** | Linux Kernel — 责任链 | 责任追溯卡 | 检查变更的签名和审查记录 |
| **P2** | PostgreSQL — 文档覆盖率 | 文档检查卡 | 检查新增功能是否有文档更新 |
| **P2** | DDD — 领域事件 | 事件匹配卡 | 匹配实际事件 vs 计划事件序列 |

### 核心操作序列

```
1. 读取现有证据（Git/测试/CI/Issue）
2. 对每个里程碑，评定确定性等级（Hill Chart）：
   - 上坡：仍有关键未知，进度不可信
   - 下坡：知道怎么做，进度可信
   - 已完成：有证据证明完成
3. 报告"实际完成" vs "声称完成"
4. 识别计划偏差和范围偏移
5. 给出下一阶段建议
```

---

## 综合推荐行动卡

### 卡1：战略连贯性检查（Plan 阶段）
```
触发条件：Plan 阶段开始，或用户只提供了"目标清单"
来源：Richard Rumelt — Good Strategy/Bad Strategy
动作：
  1. 要求用户或从已有信息提取"核心挑战"
  2. 形成"诊断 → 指导方针 → 一致行动"三要素
  3. 检查每个里程碑是否都能回指诊断
  4. 加入"不会做什么"和"非目标"
停止条件：删除任一里程碑不影响指导方针 → 说明它不是核心里程碑
```

### 卡2：里程碑约束设定（Plan 阶段）
```
触发条件：Plan 阶段进入"里程碑、任务和依赖"章节
来源：Ryan Singer — Shape Up
动作：
  1. 为每个里程碑声明 appetite（固定时间预算）
  2. 分三层：must-have / nice-to-have / cuttable
  3. 识别 rabbit holes（已知陷阱和拖延风险）
  4. 设定 no-gos（明确不做的事）
停止条件：范围能在 appetite 内交付核心结果
超限处理：默认缩范围，不悄悄延长
```

### 卡3：C4 架构描述框架（Plan 阶段）
```
触发条件：Plan 阶段进入"架构、组件、数据流"章节
来源：Simon Brown — C4 Model
动作：
  1. 先画系统上下文图（Context）：系统边界、外部依赖、用户角色
  2. 再画容器/服务图（Container）：进程、服务、数据存储
  3. 最后画组件图（Component）：模块、接口、依赖
  4. 使用文本格式（PlantUML / Mermaid）生成
停止条件：Container 层可覆盖所有 Context 层识别的外部依赖和用户
```

### 卡4：不确定性分级（Track 阶段）
```
触发条件：Track 阶段报告进度
来源：Ryan Singer — Hill Chart
动作：
  1. 对每个里程碑/任务，评定"确定性等级"
  2. 上坡=仍有关键未知，进度不可信
  3. 下坡=知道怎么做，进度可信
  4. 已完成=有证据证明完成
  5. 报告"哪些进入下坡"而非"完成了多少任务"
停止条件：所有里程碑可报告确定性等级
```

### 卡5：测试优先规则（Plan 阶段）
```
触发条件：Plan 阶段进入"测试和验收"章节
来源：SQLite 测试哲学 + Martin Fowler
动作：
  1. 每个里程碑包含"测试用例设计和实现"任务
  2. 建立"每个 bug 修复先写回归测试"规则
  3. 测试策略覆盖"重构安全网需求"
  4. 对于处理外部输入的项目，包含模糊测试计划
停止条件：测试策略覆盖所有关键路径和错误处理路径
```

---

## 研究结论

1. **Plan 阶段最值得优先蒸馏的三大智慧**：Rumelt 的战略连贯性（防止计划变成目标清单）、Shape Up 的 appetite 约束（防止范围膨胀）、C4 模型的架构描述框架（让架构可沟通、可审查）。

2. **Track 阶段最值得优先蒸馏的智慧**：Hill Chart 的不确定性分级（让"到底做完了吗"这个核心问题有更诚实的回答）。

3. **项目案例比人物更可靠**：Linux Kernel 的治理模型、React 的 RFC 流程、SQLite 的测试哲学——这些是多年运行的工程实践，有明确的机制和结果证据，比个人观点更适合转成 Agent 行为。

4. **不直接模拟"大师"风格**：Carpe Diem 的每个阶段都有明确的"主动讲授→Agent 动作→用户决策→状态写入→下一步路由"结构。智慧应以"行为卡"形式嵌入这个结构，而不是让 Agent 扮演某位大师的口吻。

5. **与现有研究一致**：本研究与[之前的项目设计研究](2026-08-30-project-design-wisdom-sources.md)一致，确认了 Rumelt 和 Singer 对 Plan 阶段的价值，并补充了 C4、DDD、Release It!、Brooks、Fowler 和五个项目案例的详细分析。