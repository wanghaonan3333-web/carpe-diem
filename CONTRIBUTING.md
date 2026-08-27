# 贡献指南

感谢你帮助 Carpe Diem 更会带人开始项目，而不是只会生成点子。

## 最有价值的贡献

- 可复现的引导失败案例，例如连续盘问、无证据原创声明、方向收敛失败或越界开发。
- Codex、Claude Code、Cursor、OpenClaw 的实际发现与触发证据。
- 能改善用户真实决定的方法、反例和测试。
- 状态安全、隐私、计划质量和只读证据采集方面的修复。

## 开始之前

1. 搜索已有 Issue，避免重复。
2. 行为改变先用 Issue 讲清用户问题、建议变化和如何验证。
3. 保持一个 Pull Request 只解决一个明确问题。
4. 不提交真实个人画像、项目 `.carpe-diem/` 状态、凭据或绝对个人路径。

## 本地检查

需要 Python 3.10+，不需要第三方依赖：

```bash
python3 -m compileall -q scripts tests
python3 -m unittest discover -s tests -v
python3 scripts/carpe_diem.py doctor --source . --json
git diff --check
```

行为变更应先增加失败测试，再实现最小修复。引导文案变更应同时提供正例、反例或可评分的演练证据。

## 产品边界

贡献不得把 Carpe Diem 变成自带模型的应用、业务代码执行器或后台监督服务。若你认为边界应改变，请先提交设计讨论，而不是直接扩大权限。
