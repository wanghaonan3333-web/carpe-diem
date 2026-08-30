# Carpe Diem 项目设计经验蒸馏：高信任来源研究

研究日期：2026-08-30  
研究范围：只使用方法作者、作者所在官方机构、出版社，以及 Anthropic / Claude、OpenAI 官方页面。  
研究目的：判断哪些项目设计经验能被改写成 Carpe Diem 的 Agent 行为，而不是把书摘、名人观点或厂商宣传堆进提示词。

## 结论先行

可以从书籍、人物和大模型官网文章中学习，但应把它们放在 Carpe Diem 现有生命周期之下，作为“按情境调用的方法卡”，而不是再造一套大而全的方法论。

最值得先加入的四个行为是：

1. Discover 用真实经历和现有替代行为定义“用户想取得的进展”，不从人群标签或功能愿望开始。
2. Validate 把方向拆成价值、可用性、可行性、业务/生态可持续性四类风险，优先验证后果最严重且最不确定的一项。
3. Plan 必须把核心挑战、总体解法和相互一致的行动连起来，并明确时间投入上限、非目标和高风险陷阱。
4. Track 不把“做了多少任务”当进度；同时跟踪可验证结果、仍未解决的不确定性、真实用户反馈及其对应的规则或测试。

这些来源不应被蒸馏成“模拟某位大师说话”。更可靠的形式是：`何时触发 → Agent 做什么 → 需要什么证据 → 产出什么 → 何时停止 → 哪些边界不能跨越`。

## 研究方法与证据等级

- 本文保留 12 个一手来源：5 篇 Anthropic/OpenAI 官方案例或方法文章，7 组作者/书籍方法。
- “原始主张”只写来源实际支持的内容；“可蒸馏规则”是本文针对 Carpe Diem 的推导，不冒充原作者原话。
- 厂商内部案例属于说明性案例，不等于独立实验；其效果数字只能在该案例语境中引用。
- 书中方法可以转为问题顺序、状态字段、门槛和检查项，但不能大段复制原文、图表或受版权保护的完整模板。

## 用户所举 Anthropic 原文核对

用户给出的标题 **“How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep”** 与官方页面标题完全一致，无标题差异。页面发布于 2026-08-24，作者 Adam Ward，身份为 Anthropic 营销团队成员。[Claude 官方原文](https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep)

原文的关键过程不是“用 Claude 自动发周报”，而是：从本人已熟悉的手工流程开始；先写一个期望输出示例；先用单一事实来源；在 10 人小组中试点；把每条真实反馈写成显式规则；每次运行先检查数据表头；对指令和输出做版本与归档。

对 Carpe Diem 最有价值的蒸馏是：

- Discover 优先寻找用户已经反复手工完成、且用户自己知道“什么算好”的工作。
- Validate 要求一个“期望结果样例”、一个小范围试点、一个反馈责任人和一个明确错误预算。
- 每条新增规则必须能回指到真实错误、用户反馈或数据变化，不因想象中的风险无限增长。
- Track 保留版本、证据和变更原因；遇到数据结构变化时先重新识别字段，不依赖位置假设。

不可泛化边界：这是 Anthropic 自家员工使用自家产品的单一内部案例；“活动报名翻倍”是案例自述，没有对照组，不能写成采用该流程后的普遍收益。其 BigQuery、CRM、Slack、MCP 和组织授权条件也不能假定普通用户具备。原文后期允许系统不等待人工批准发送消息，不适用于 Carpe Diem 当前的渐进授权、只读 Track 和不主动对外发送边界。

## Anthropic / OpenAI 官方文章：适合蒸馏的 5 个来源

### 1. Adam Ward：Anthropic field marketer 周报案例

- 来源：[Claude 官方博客，2026-08-24](https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep)
- 原始主张：从熟悉的手工流程、期望输出样例和单一事实来源开始；小组试点中的错误与反馈被转换成显式规则；指令和输出被版本化、归档后再扩大使用范围。
- 适用阶段：Discover、Validate、Track。
- 可蒸馏规则：优先发现“重复发生 + 已有人工基线 + 用户能判断好坏”的机会；为验证方案生成一份目标样例；把反馈保存为 `observation → rule/test → version`；扩大范围前检查试点门槛。
- 不可泛化边界：单一厂商内部案例；业务指标非受控实验；不能从“自动发送成功”推出所有外部动作都可取消人工确认。

### 2. Anthropic：Building effective agents

- 来源：[Anthropic Engineering，2024-12-19](https://www.anthropic.com/engineering/building-effective-agents)
- 原始主张：应从最简单可行方案开始，只在效果证据支持时增加复杂度；预定义 workflow 与动态 agent 应区分；Agent 运行应从环境获取真实反馈，并设置人类检查点、停止条件、沙箱测试和清晰工具说明。页面也明确提示其 2024 年工具生态描述已有变化。
- 适用阶段：Plan、Track。
- 可蒸馏规则：Plan 先问“确定性脚本、单轮提示或固定工作流是否足够”；只有任务步骤无法预先定义且收益可衡量时才建议更高自治；为每个自动化计划写明 ground truth、检查点、停止条件和失败交接。
- 不可泛化边界：这是一篇 Agent 架构文章，不是通用产品发现框架；文中模式是可组合选择，不是必须全部实现的成熟度阶梯；旧工具细节需要重新核对。

### 3. Anthropic：Demystifying evals for AI agents

- 来源：[Anthropic Engineering，2026-01-09](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- 原始主张：Agent eval 应明确任务、试验、grader、trace 和最终环境 outcome；早期 eval 可迫使团队具体定义成功，规模化后要结合自动化评估、生产监控、用户反馈、人工 trace 审阅与系统性人工评估；最接近用户和需求的人应参与定义成功。
- 适用阶段：Validate、Plan、Track。
- 可蒸馏规则：验收标准必须测最终状态而不只看 Agent 的自述；高变异任务要允许多次试验；Track 将真实失败沉淀为回归案例，但同时记录 grader 是否可能错；主观质量要保留人工校准。
- 不可泛化边界：主要讨论 AI Agent 产品；小型非 AI 项目不一定需要 eval 基础设施；自动分数不能代替查看具体失败与用户结果。

### 4. OpenAI：创意团队把概念转成原型

- 来源：[OpenAI on OpenAI，2026-07-16](https://openai.com/index/codex-collaborator-creative-team/)
- 原始主张：Chad Nelson 先提供品牌、产品、目标、语气、草图、故事板和风格指南等项目上下文，再使用 Codex 扩大想法空间并快速制作可交互原型；在案例中，50 个方向由人类筛成 10 个，强调人类判断仍居中心。
- 适用阶段：Discover、Validate。
- 可蒸馏规则：发散前先形成“项目上下文包”；候选必须在同一约束下生成才可比较；Agent 可以扩大选项与快速原型，但方向选择由用户依据明确标准完成。
- 不可泛化边界：OpenAI 内部说明性案例，没有证明“候选更多必然更好”；50→10 是案例数字，不应固化进 Skill；快速原型不等于需求、可行性或可维护性已验证。

### 5. OpenAI：Building self-improving tax agents with Codex

- 来源：[OpenAI，2026](https://openai.com/index/building-self-improving-tax-agents-with-codex/)
- 原始主张：该系统以从业者反馈、完整生产 trace 和定制 eval 构成改进闭环；只有重复差异被专家复核并归类为可行动问题后，才变成有成功条件的边界化工程任务；含糊案例回到产品团队，工程师仍负责架构、产品决策与发布。
- 适用阶段：Validate、Track。
- 可蒸馏规则：Track 应把 `用户纠正 → 证据链 → 重复模式 → 验证案例 → 有界下一步` 分层，避免把一次抱怨直接升级为路线图；“已修复”需同时有目标验证与回归证据；证据含糊时保留人工判断。
- 不可泛化边界：税务是高专业、高结构化审核场景；案例指标来自厂商和合作方，不能外推；Carpe Diem 只生成进度判断与交接建议，不能借“自我改进”名义自动修改用户项目。

## 人物与书籍方法：适合转成 Agent 行为的 7 组来源

### 1. Clayton Christensen 等：Jobs to Be Done / Competing Against Luck

- 来源：[Clayton Christensen Institute：Jobs to Be Done Theory](https://www.christenseninstitute.org/theory/jobs-to-be-done/)
- 原始主张：理解选择要研究人在特定情境下想取得的进展，以及促使其做出或放弃决定的功能、社会和情绪力量；产品被用户“雇来”完成一项工作，而不是仅凭人口属性被购买。
- 适用阶段：Discover。
- 可蒸馏规则：Agent 不先问“你想做什么功能”，而询问最近一次真实事件：当时发生了什么、用户原来怎么解决、什么推动改变、什么阻碍改变、若不解决会怎样；机会陈述必须包含 `情境 + 期望进展 + 现有替代 + 阻力/代价`。
- 停止条件：至少有一个来自真实故事而非抽象意见的机会，且能解释为何现有替代仍被使用。
- 不可泛化边界：JTBD 是解释选择的透镜，不负责市场规模、技术可行性或商业模式验证；不能把一句“Job statement”当证据。

### 2. Teresa Torres：Continuous Discovery Habits / Opportunity Solution Tree

- 来源：[Product Talk：Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/)
- 原始主张：树将期望结果、用户机会、候选方案和假设测试连起来；作者要求先有目标用户和值主张理论、明确 outcome，并做 3–4 次基于故事的用户访谈，明确提醒不要凭空编造机会；之后比较多个方案并测试高风险假设。
- 适用阶段：Discover、Validate。
- 可蒸馏规则：把“机会”和“方案”分字段保存；没有故事证据的机会标为推断；为同一机会保留多个方案；从跨方案的最危险假设开始验证，而不是逐个把方案做完整。
- 停止条件：选择方向时能画出 `outcome → opportunity → solution → assumption/test` 的证据链，并记录被淘汰分支原因。
- 不可泛化边界：3–4 次访谈是作者对开始画树的输入门槛，不代表统计饱和或市场验证完成；Opportunity Solution Tree 是团队思考工具，不应变成必须填满的文档官僚流程。

### 3. Marty Cagan：INSPIRED / Four Big Risks

- 来源：[Silicon Valley Product Group：The Four Big Risks](https://www.svpg.com/four-big-risks/)
- 原始主张：产品风险至少包括价值、可用性、可行性和业务可持续性；应尽早处理大风险、由产品/设计/工程协作，并聚焦问题结果而非功能清单。
- 适用阶段：Validate、Plan。
- 可蒸馏规则：为每个方向建立四格风险表，每格记录 `假设、已有证据、严重度、出错后果、最小验证`；按“不确定性 × 后果”选择下一项验证；开源项目把业务可持续性改写为维护、分发、许可、生态兼容和长期投入。
- 停止条件：不存在仍被标为高后果、但没有验证动作或明确接受理由的风险。
- 不可泛化边界：角色分工与商业产品背景不能原样套给独立开发者；四类风险是检查视角，不保证覆盖安全、伦理或系统性风险。

### 4. Eric Ries：The Lean Startup

- 来源：[The Lean Startup 官方方法页](https://theleanstartup.com/principles)
- 原始主张：不确定环境中的进展单位是 validated learning；Build–Measure–Learn 将想法变为实验，使用可行动指标判断继续还是转向；MVP 的目的在于尽快开始学习。
- 适用阶段：Validate、Track。
- 可蒸馏规则：每个验证动作必须写成 `可证伪假设 → 最小实验 → 行为/结果指标 → 事前阈值 → PASS/PIVOT/REJECT`；Track 报告新增了什么学习，而不只报告产出了多少文件或功能。
- 停止条件：实验结果能改变一个明确决策；若无论结果如何都不会改变方向，则不值得做该实验。
- 不可泛化边界：MVP 不等于低质量发布，也不能绕过安全、隐私和高风险领域的专业审核；Build–Measure–Learn 不能把访谈、原型和使用意向错误包装成已验证收入。

### 5. Jake Knapp、John Zeratsky、Braden Kowitz：Sprint

- 来源：[Simon & Schuster 官方书页：Sprint](https://www.simonandschuster.com/books/Sprint/Jake-Knapp/9781501121746)；[Google Design Sprint Kit](https://designsprintkit.withgoogle.com/)
- 原始主张：Design Sprint 用小团队在有限时间内从问题走到原型和用户测试，以较低投入在完整建设前观察真实反应；Google 的版本包含 Understand、Define、Sketch、Decide、Prototype、Validate 六阶段，并强调按目标调整方法。
- 适用阶段：Validate。
- 可蒸馏规则：当方向有关键体验假设时，只制作足够触发真实反应的表面；先写出原型要回答的问题和用户测试脚本，再决定原型范围；测试后记录观察到的行为，不只记录受访者偏好。
- 停止条件：关键假设得到支持、反证或明确仍未知；不能因原型“看起来可用”直接进入完整开发。
- 不可泛化边界：Google FAQ 明确指出缺少用户研究时应先研究、方向与功能已明确时可能不需要 Sprint；五天/六阶段是可调整形式，不应成为每个项目的固定仪式。

### 6. Richard Rumelt：Good Strategy/Bad Strategy

- 来源：[Penguin Random House 官方书页](https://www.penguinrandomhouse.com/books/208668/good-strategy-bad-strategy-by-richard-rumelt/9780307886255/)；[Richard Rumelt 官方站](https://www.richardrumelt.com/books)
- 原始主张：好战略是针对阻碍进展的关键挑战所作的具体、连贯回应；书中以“kernel”和近端目标等概念区分战略与口号、愿景和财务目标。
- 适用阶段：Plan。
- 可蒸馏规则：计划首页强制形成 `诊断：核心挑战是什么 → 指导方针：选择什么总体解法 → 一致行动：哪些里程碑共同落实它`；每个行动必须能回指诊断；加入“不会做什么”，防止目标列表冒充战略。
- 停止条件：若删去某项任务不影响指导方针，它可能不是核心里程碑；若行动彼此冲突或只对应愿景词汇，计划不能批准。
- 不可泛化边界：战略 kernel 不能替代架构、测试、安全和里程碑细节；诊断是待证假设而非权威结论；竞争战略案例也不必强套给公益或个人开源项目。

### 7. Ryan Singer：Shape Up

- 来源：[Basecamp 官方在线书：Shape Up](https://basecamp.com/shapeup)；[Set Boundaries](https://basecamp.com/shapeup/1.2-chapter-03)；[Show Progress](https://basecamp.com/shapeup/3.4-chapter-13)
- 原始主张：先用 appetite 约束设计，采用固定时间、可变范围；pitch 连接问题、投入上限、方案、风险陷阱和非目标；Hill Chart 区分“仍在弄清怎么做”的上坡不确定性与“知道怎么做”的下坡执行，不以任务数量掩盖未知。
- 适用阶段：Plan、Track。
- 可蒸馏规则：Plan 为每个里程碑加入 `appetite、必须项、可削减项、rabbit holes、no-gos`；Track 同时报告交付证据与最大未知，把长期不动的范围拆小或重新定义；优先攻克最危险的不确定性。
- 停止条件：范围能在明确投入上限内交付核心结果；超限时默认缩范围或重新 Plan，而不是悄悄延长。
- 不可泛化边界：六周周期、betting table、无 backlog 等是 Basecamp 的组织实践，不应整套照搬；Hill Chart 的主观位置不能替代 Carpe Diem 现有的 Git、测试、CI、Issue 等客观证据。

## 推荐的 Skill 蒸馏结构

### 1. Carpe Diem 生命周期继续做控制平面

不要把 JTBD、Lean、Sprint、Shape Up 等并列成用户必须选择的流派。`Discover → Validate → Plan → Handoff → Track` 仍是唯一主线，方法只在满足触发条件时提供一小段额外行为。

建议每次最多加载 1–2 张方法卡。例如：

- Discover 缺少真实问题证据：加载 JTBD 故事卡。
- Discover 有很多需求但混入方案：加载 Opportunity Solution Tree 区分卡。
- Validate 不知道验证什么：加载 Four Big Risks 风险卡。
- Validate 有关键体验假设：加载 Sprint 原型卡。
- Plan 只有目标和功能清单：加载 Rumelt 战略连贯性卡。
- Plan 范围过大或 Track 隐藏未知：加载 Shape Up 边界/不确定性卡。
- AI 项目需要质量闭环：加载 Anthropic eval / OpenAI trace 卡。

### 2. 方法卡应是行为合同，不是知识摘抄

推荐字段：

```yaml
id: jtbd-recent-story
stage: discover
applies_when: 只有抽象需求、人物画像或功能愿望，缺少真实事件
agent_actions:
  - 询问最近一次发生问题的具体情境
  - 识别现有替代、推动力、阻力和后果
evidence_required:
  - 至少一个第一人称真实故事或可核对观察
output:
  - 情境 + 期望进展 + 现有替代 + 未满足原因
stop_when:
  - 机会可以被具体证据支持或推翻
do_not:
  - 不根据人口标签杜撰需求
source: https://www.christenseninstitute.org/theory/jobs-to-be-done/
reviewed_at: 2026-08-30
```

这样的结构让方法影响 Agent 的提问顺序、证据门槛和输出格式，同时不会让主对话变成读书课。

### 3. 需要新增“来源—规则—证据”账本

每条经验规则至少记录：

- 来源所有者、页面或书籍、版本/发布日期、复核日期；
- 原始主张的简短释义；
- Carpe Diem 的推导规则；
- 触发阶段、适用条件和停止条件；
- 不适用条件及与渐进授权、只读 Track 的冲突；
- 来自真实使用的支持证据、反例和后续修订。

这样能避免“某篇文章很酷，所以加入 Skill”的随意积累。来源只是候选，只有当规则能改善真实会话或测试时才进入默认路径。

### 4. 版权与可信度边界

- 只保留抽象行为、短释义和链接，不复制完整章节、图表、访谈脚本或出版社模板。
- 不把 “Marty Cagan 会怎么说” 或 “像 Steve Jobs 一样思考” 写入角色设定；人物名称用于来源追溯，不用于权威压服用户。
- 厂商案例的数字要附带“内部自述、无独立对照”等证据等级。
- 博客文章会变更，应记录 `reviewed_at`；涉及产品接口、权限和工具能力时必须实时重查。
- 方法之间冲突时不强行融合：例如 Shape Up 的固定时间可变范围、Sprint 的限时原型和 Carpe Diem 的逐章确认可以互补，但不能因此取消用户确认或安全门槛。

## 建议的最小落地批次

第一批只加入四张卡，并用对话测试验证，不急着收录全部来源：

1. `discover/jtbd-recent-story`：防止从抽象兴趣直接生成项目。
2. `validate/four-risks`：把验证工作指向最大的不确定性和后果。
3. `plan/strategy-coherence`：防止愿景、功能清单和任务列表冒充计划。
4. `track/unknown-vs-done`：在现有证据分级旁补充“最大未知”，但不引入主观百分比。

建议为每张卡准备至少三类测试：应触发、不得触发、与现有安全/授权边界冲突时的降级行为。确认它们确实减少追问、提高证据质量或降低返工后，再加入 Opportunity Solution Tree、Sprint 原型和 AI eval/trace 卡。

## 最终判断

Carpe Diem 最适合成为“会根据项目当前风险调用少量设计智慧的项目导师”，而不是一本塞满框架的百科全书。

用户举出的 Anthropic 文章非常适合作为首个案例卡，因为它完整展示了 `真实手工痛点 → 可描述的好结果 → 小范围试点 → 反馈变规则 → 版本与归档 → 谨慎扩大`。但真正可以长期复用的不是其中的 Claude Code、BigQuery 或周报场景，而是这条证据驱动的行为链，以及它不能越过授权、人工判断和领域边界的条件。
