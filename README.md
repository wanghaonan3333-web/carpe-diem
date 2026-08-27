# Carpe Diem

> 手握 Coding Agent，却不知道什么值得做？

Carpe Diem 是一个开源 Agent Skill。它在 Codex、Claude Code、Cursor、OpenClaw 等宿主 Agent 里扮演“项目点火导师 + 共同创始人”，帮助开发者或创作者发现、验证并规划一个值得开始的开源项目。

它不自带模型，也不是随机点子生成器。它使用你当前 Agent 的推理和搜索能力，用本地文件保存经你确认的上下文；正式实施计划批准后，它停止开发职责，只在你再次调用时依据只读证据跟进项目。

## 它解决什么

Carpe Diem 把“我不知道做什么”分成四个阶段：

1. **Discover**：从真实摩擦、能力、兴趣和未完成资产中找机会，而不是抛出一百个随机点子。
2. **Validate**：调查竞品、替代方案和需求证据；没有证据时不会宣称“别人没做过”。
3. **Plan**：逐段打磨完整项目实施计划和开发交接包。
4. **Track**：开发开始后只读观察 Git、已有测试或 CI 证据，记录进度、偏差和下一步。

## 一段典型对话

```text
你：我有 Coding Agent，但不知道该做什么。

Carpe Diem：先不用逼自己想一个“伟大点子”。真正值得做的方向，通常藏在
你反复遇到的摩擦、已经具备却没被产品化的能力，以及技术变化刚带来的新空档里。
我会先根据这段对话形成机会地图；如果信息不足，再由你决定是否开放一个本地目录
或 GitHub 范围。未经授权我不会读取。我们先从你最近反复想让 Agent 替你解决、
但每次仍要手工收尾的一件事开始。
```

它会先讲清判断和理由，只在猜错会造成返工的真实岔路口请你做一个决定。

## 安装

要求 Python 3.10+；只使用标准库。先克隆或下载本仓库，然后在仓库根目录运行：

```bash
python3 scripts/carpe_diem.py install detect
python3 scripts/carpe_diem.py install plan --platform codex --json > /tmp/carpe-diem-install.json
```

阅读计划中的安装目标、版本、文件清单和指纹。确认无误后一次批准：

```bash
python3 scripts/carpe_diem.py install apply --plan /tmp/carpe-diem-install.json --yes
python3 scripts/carpe_diem.py install verify --target ~/.codex/skills/carpe-diem
```

其他宿主只需把 `--platform codex` 改为 `claude-code`、`cursor` 或 `openclaw`。平台细节见：

- [Codex](adapters/codex/INSTALL.md)
- [Claude Code](adapters/claude-code/INSTALL.md)
- [Cursor](adapters/cursor/INSTALL.md)
- [OpenClaw](adapters/openclaw/INSTALL.md)

安装器不会覆盖已有目录。卸载也只会删除带有效安装回执、且安装后未被修改的快照。

## 使用

在新的 Agent 对话里自然表达即可，例如：

- “我想做一个开源项目，但完全没有头绪。”
- “我有三个方向，帮我判断哪个更值得做。”
- “继续完善上次的项目计划。”
- “对照计划看看这个项目现在进展如何。”

你可以随时打断、质疑或要求查证。Carpe Diem 会回答后回到原来的主线。

## 数据与隐私

Carpe Diem 使用双层本地记忆：

- 个人画像：`~/.carpe-diem/profiles/me.json`
- 项目状态：项目目录内 `.carpe-diem/`

长期画像只保存你确认过的摘要事实。推断先以候选形式展示，批准后才写入。读取本地目录、GitHub、笔记、Issue 或 CI 前，Skill 必须说明目的、目标和只读范围并获得授权。便携导出会移除绝对本地路径。

建议把项目内 `.carpe-diem/` 保持为本地状态；Carpe Diem 不会替你修改 `.gitignore`。

## 明确边界

Carpe Diem 可以研究、判断、规划、生成交接包和跟进证据。它不会：

- 编写或修改项目业务代码；
- 修复 Bug 或代替开发 Agent 执行计划；
- 自动提交、推送或修改 Issue；
- 未经批准读取额外上下文；
- 自带模型、后台服务或模型 API Key。

## 当前兼容性

四个平台共用同一份 Skill 方法和状态协议。v0.1 已自动验证 Skill 结构、确定性脚本和四种安装目标；宿主实际发现与对话表现需按版本分别烟雾测试。仓库内的[内测记录](docs/internal-testing.md)会明确区分“已验证”和“待验证”，不会把可行推断写成已支持事实。

## 本地验证

```bash
python3 -m compileall -q scripts tests
python3 -m unittest discover -s tests -v
python3 scripts/carpe_diem.py doctor --source . --json
git diff --check
```

## 贡献

欢迎提交真实的引导失败案例、跨 Agent 兼容性证据和更清晰的方法改进。开始前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

## License

[Apache License 2.0](LICENSE)
