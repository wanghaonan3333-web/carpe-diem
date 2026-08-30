# Carpe Diem 项目设计智慧卡集成计划

- 日期：2026-08-30
- 依据：`docs/research/2026-08-30-project-design-wisdom-sources.md`
- 目标：把高信任项目设计经验蒸馏为按阶段触发、证据驱动、可离线测试的 Agent 行为卡，同时保持 Carpe Diem 的渐进加载、渐进授权和只读 Track 边界。
- 计划性质：v0.2 候选功能的独立实施计划；不包含多 Agent 协作、后台采集或业务代码开发。

## 1. 当前基线与前置条件

当前工作区包含尚未提交的 v0.1.1 改动，以及未跟踪的 `references/wisdom/`、项目类型模板和其他 v0.2 文档。实施本计划前必须先完成一次只读盘点，不能把这些文件当作已经批准或已经发布的产品能力。

实施前置条件：

1. 保存当前 `git status --short` 和相关 diff，明确哪些改动属于 v0.1.1，哪些属于智慧库候选。
2. 不覆盖、不删除现有 `references/wisdom/` 文件；先分类，再决定保留为来源笔记、改写为方法卡或移出运行时清单。
3. 先解决当前 `SKILL.md`、`SKILL.en.md`、阶段文件之间已经存在的合同差异，再接入新方法卡。
4. `manifest.json` 中任何新增字段必须有平台 schema 或发布工具验证证据；未验证字段不得作为本计划的依赖。
5. 所有实现继续使用 Python 标准库和现有 `unittest` 测试体系。

## 2. 产品设计约束

### 2.1 唯一主线

`Discover -> Validate -> Plan -> Handoff -> Track` 继续作为唯一控制平面。JTBD、Opportunity Solution Tree、Four Risks、Shape Up 等不是并列工作流，也不要求用户选择流派。

### 2.2 方法卡的职责

每张方法卡只解决一个阶段内的具体判断问题：

- 何时触发；
- Agent 要完成哪些动作；
- 最低证据是什么；
- 产出什么结构化结论；
- 何时停止；
- 哪些情况下不适用。

方法卡不模拟人物语气，不展示大段书摘，不把厂商案例数字当作普遍收益。

### 2.3 渐进加载

只有当前阶段出现对应缺口时才加载方法卡，每轮最多加载一张。阶段文件直接指向自己的方法卡，避免在 `SKILL.md` 中维护不断增长的主题路由表。

### 2.4 证据等级

来源账本使用四级证据：

1. `primary-method`：作者或官方机构发布的原始方法；
2. `first-party-practice`：团队第一方实践；
3. `official-capability`：产品官方能力与限制；
4. `vendor-case`：厂商成功案例，只能生成待验证假设。

每条厂商指标必须标记为案例自述，并记录是否有对照、样本范围和不可泛化条件。

## 3. 目标文件树

```text
references/
└── wisdom/
    ├── README.md
    ├── source-ledger.md
    ├── method-cards/
    │   ├── discover-real-friction.md
    │   ├── validate-riskiest-assumption.md
    │   ├── plan-strategy-coherence.md
    │   └── track-outcome-and-unknowns.md
    ├── real-world-patterns/        # 现有候选来源笔记，不直接作为默认运行时规则
    └── project-archetypes/         # 不在本计划中接入
tests/
├── fixtures/
│   ├── wisdom-positive.md
│   └── wisdom-negative.md
└── test_wisdom.py
```

现有研究文件 `docs/research/2026-08-30-project-design-wisdom-sources.md` 保持为研究证据，不加入安装运行时快照。

## 4. 方法卡统一合同

每张卡采用 Markdown 正文加固定字段，避免引入新的运行时解析依赖：

```markdown
# <名称>

- id: <稳定 ID>
- stage: <discover|validate|plan|track>
- applies_when: <可观察触发条件>
- source_ids: <来源账本 ID 列表>

## Agent 动作

按顺序列出 2–5 个动作。

## 最低证据

列出进入结论所需证据。

## 产出合同

定义必须交付的字段或判断。

## 停止条件

定义何时完成或降级。

## 不适用与边界

说明何时不应使用，以及与授权、只读 Track 的关系。
```

合同要求：

- `applies_when` 必须描述当前对话中可观察的缺口，不能只写项目类型；
- 动作必须改变 Agent 的提问、证据或输出，不能只是解释理论；
- 停止条件必须可检查；
- 每张卡至少包含一个不适用条件；
- 来源 ID 必须在 `source-ledger.md` 中存在；
- 同一规则只在一个文件中定义，阶段文件仅保存触发指针。

## 5. 首批四张方法卡

### 5.1 Discover：`discover-real-friction`

来源组合：Clayton Christensen / Bob Moesta 的 JTBD、Paul Graham 的真实摩擦与窄而深的首批用户原则。

触发条件：当前只有兴趣、人物标签、技术名或功能愿望，没有一次真实发生的问题经历。

Agent 动作：

1. 请用户回忆最近一次问题发生的具体情境，一次只问一个合并问题。
2. 提炼当时的触发、期望进展、现有替代、阻力、代价和不解决的后果。
3. 区分真实观察与 Agent 推断。
4. 判断是否存在少量但当前需求强烈的首批用户。

产出合同：`情境 + 期望进展 + 现有替代 + 未满足原因 + 首批用户`。

停止条件：至少形成一个能够被进一步支持或推翻的机会陈述；没有真实故事时保持候选状态，不进入 Validate。

### 5.2 Validate：`validate-riskiest-assumption`

来源组合：Marty Cagan 的 Four Big Risks、Rob Fitzpatrick 的 The Mom Test、Adam Ward 的 Anthropic 小范围试点案例、David Bland / Alexander Osterwalder 的实验设计。

触发条件：方向已经明确，但验证工作仍是泛泛地“做调研”或“看看有没有人需要”。

Agent 动作：

1. 将风险分为价值、可用性、可行性、维护/分发可持续性。
2. 按“不确定性 × 出错后果”选择唯一的下一项风险。
3. 优先询问过去行为、现有投入和真实替代，不把赞美或使用意向当证据。
4. 若项目来自熟悉的手工流程，要求目标输出样例、单一事实源、小范围试点、反馈责任人和错误预算。
5. 将实验写成可证伪假设、最小动作、事前阈值和 `PASS/PIVOT/REJECT`。

产出合同：四格风险表和一个下一步实验，不生成完整功能清单。

停止条件：实验结果无论成功或失败都会改变一个明确决定；否则重新选择风险。

### 5.3 Plan：`plan-strategy-coherence`

来源组合：Richard Rumelt 的战略 kernel、Ryan Singer 的 appetite、rabbit holes 和 no-gos。

触发条件：计划只有愿景、功能清单或任务列表，无法解释为什么这些行动共同解决同一个关键问题。

Agent 动作：

1. 写出核心挑战诊断，并标记其证据和未知项。
2. 提出一条总体指导方针，而不是多个口号。
3. 检查所有里程碑是否共同落实指导方针。
4. 为第一个里程碑定义投入上限、必须项、可削减项、rabbit holes 和 no-gos。
5. 删除不能回指核心挑战、或与其他行动冲突的任务。

产出合同：`诊断 -> 指导方针 -> 一致行动`，附第一个里程碑的范围边界。

停止条件：计划能在明确投入上限内交付核心结果，且不存在无主的高风险陷阱。

### 5.4 Track：`track-outcome-and-unknowns`

来源组合：Shape Up 的不确定性表达、Anthropic eval 方法、Adam Ward 的反馈变规则、OpenAI 的 trace 驱动改进案例。

触发条件：进度主要按任务数量、文件数量或主观百分比描述，没有结果证据或最大未知项。

Agent 动作：

1. 分开记录“有证据完成”“声称完成”“仍未知”。
2. 对照计划说明产生了什么用户可观察结果。
3. 标出当前最大未知，以及它阻碍哪个里程碑判断。
4. 只在重复差异经过证据复核后，将其提炼为下一阶段规则或回归测试建议。
5. 保留 `观察 -> 证据 -> 规则/测试建议 -> 版本` 链路。

产出合同：结果证据、最大未知、计划偏差和一个有界下一步。

停止条件：用户能据此选择继续、调整、暂停或完成；Carpe Diem 仍不运行未知测试、不修改源码。

## 6. 实施里程碑

### M0：盘点与去重

任务：

1. 记录当前工作树和 v0.1.1 改动范围。
2. 为现有 `references/wisdom/` 文件建立清单，逐项标记：`source-note`、`method-card-candidate`、`project-archetype` 或 `out-of-scope`。
3. 找出未经来源支持的“已验证”“最佳实践”等强断言，改写方案必须进入后续任务，不在盘点阶段直接修改。
4. 确认四张首批卡与现有阶段文件不存在语义重复。

完成标准：每个现有智慧库文件都有归类和处置建议，没有删除或覆盖用户文件。

### M1：先建立失败测试

新增 `tests/test_wisdom.py`，覆盖：

1. 四张方法卡存在且 ID 唯一；
2. 每张卡包含固定章节和单一合法阶段；
3. 所有 `source_ids` 都能在来源账本中找到；
4. 每个阶段文件只指向对应方法卡；
5. `SKILL.md` 不复制方法卡正文；
6. manifest 收录运行时方法卡和来源账本，但不收录研究草稿；
7. 卡片中不包含绝对本地路径、长篇原文或未经标注的厂商效果数字。

先运行测试并确认因目标文件或指针缺失而失败。

验证：

```bash
python3 -m unittest tests.test_wisdom -v
```

完成标准：失败原因只对应本计划尚未实现的合同，不暴露无关基线故障。

### M2：建立来源账本与四张方法卡

任务：

1. 将研究文件中的一手来源登记到 `references/wisdom/source-ledger.md`。
2. 每条来源记录所有者、标题、URL、发布日期、证据等级、复核日期和不可泛化边界。
3. 按第 5 节合同创建四张方法卡。
4. 重写 `references/wisdom/README.md` 为轻量路由索引，明确现有 `real-world-patterns/` 仅是候选来源笔记。
5. 不复制书籍章节、图表、完整模板或大段原文。

完成标准：四张卡均可脱离来源文章独立指导 Agent 行为，同时每条推导都可回溯到来源账本。

### M3：接入阶段文件

只修改四个阶段文件：

- `references/stages/discover.md`
- `references/stages/validate.md`
- `references/stages/plan.md`
- `references/stages/track.md`

每个阶段增加一个简短条件指针：只有观察到对应缺口时才读取该阶段卡；卡片完成后返回原阶段的 `next_recommended`。

不得：

- 在 `SKILL.md` 中添加按 AI、CLI、Web 等项目类型自动加载的长路由表；
- 一次加载整个 `references/wisdom/`；
- 因方法卡取消用户确认、扩大读取权限或改变 Track 只读边界。

完成标准：每条运行路径最多加载一张方法卡，未满足触发条件时现有行为不变。

### M4：对话行为测试

新增正反 fixture：

正例至少覆盖：

1. 只有“我想做 AI 项目”时触发真实摩擦卡；
2. 已有方向但不知道验证什么时触发最危险假设卡；
3. 功能清单冒充计划时触发战略连贯性卡；
4. 用“完成 80%”描述进度时触发结果与未知卡。

反例至少覆盖：

1. 用户已经提供真实故事时不重复盘问；
2. 已有明确验证实验时不强制重做四格风险表；
3. 计划已经连贯且范围清楚时不插入方法论讲解；
4. Track 证据不足时标记未知，不运行测试或读取未授权来源；
5. 厂商案例不能成为自动外发、后台运行或取消批准的依据。

完成标准：测试验证触发、不得触发和安全降级三类行为，而不只检查关键词存在。

### M5：安装快照与完整验证

任务：

1. 将四张卡、README 和来源账本加入 `manifest.json` 文件清单。
2. 更新结构测试，确保安装快照包含运行时必需文件。
3. 在临时目标目录完成 `plan -> apply -> verify -> uninstall`。
4. 检查安装包不包含研究草稿、AgentTeams 临时状态或本地评审文件。
5. 使用隔离会话完成四个阶段各一轮触发演练，记录实际加载的文件和输出结果。

验证：

```bash
python3 -m compileall -q scripts tests
python3 -m unittest discover -s tests -v
python3 scripts/carpe_diem.py doctor --source . --json
git diff --check
```

完成标准：

- 全量自动测试通过；
- `doctor` 有效；
- 临时安装快照验证成功且卸载不删除修改过的快照；
- 四张卡均完成一次正向触发和一次不得触发演练；
- Track 没有产生业务代码、Git 写入或未授权读取。

## 7. 后续来源蒸馏流程

新增来源不直接进入默认路径，必须经过：

```text
发现来源
-> 核对第一方原文
-> 登记证据等级与日期
-> 提炼一个原始主张
-> 转成一个可观察行为规则
-> 写应触发/不得触发/安全降级测试
-> 在真实会话中验证
-> 才能加入默认方法卡
```

一个来源如果只能产生格言、人物模仿、工具宣传或无法检查的建议，保留在研究笔记中，不进入运行时 Skill。

## 8. 本计划明确不做

- 不建立自动爬取 Anthropic、OpenAI 或其他网站的后台任务；
- 不建立“每个项目类型自动加载一套模板”的运行时路由；
- 不加入多 Agent 团队、任务队列、邮箱或 HTML 看板；
- 不改变个人画像或项目状态 schema；
- 不引入 Pydantic、数据库、向量检索或新的模型依赖；
- 不把 Carpe Diem 变成开发 Agent；
- 不自动发送消息、修改 Issue、运行项目测试或创建 Git 提交；
- 不在本计划中发布 GitHub 或 ClawHub 版本。

## 9. 建议提交顺序

实施获批后，建议按可独立验证的边界提交：

1. `test: define project design wisdom contracts`
2. `feat: add evidence-backed project design method cards`
3. `feat: route stage-specific project design wisdom`
4. `test: cover wisdom triggers and safety fallbacks`
5. `chore: package project design wisdom runtime files`

提交不是本计划执行的一部分；只有用户明确授权并且对应验证全部通过后才能创建。

## 10. 最终完成判定

只有同时满足以下条件，项目设计智慧卡集成才算完成：

- 四张方法卡符合统一合同并可回溯到来源账本；
- 每个阶段只在明确缺口下加载对应卡片；
- 已有方法足够时不增加额外提问或框架负担；
- 每张卡都有应触发、不得触发和安全降级测试；
- 厂商案例明确标注证据边界；
- `SKILL.md` 保持薄入口，不复制方法正文；
- 全量测试、编译、`doctor`、安装快照和 diff 检查通过；
- 渐进授权、正式计划确认和只读 Track 边界没有被削弱；
- 现有未提交文件没有被意外覆盖、删除或纳入发布包。
