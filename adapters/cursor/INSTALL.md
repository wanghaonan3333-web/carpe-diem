# Cursor 适配

## 用户级安装

默认目标是 `~/.cursor/skills/carpe-diem`：

```bash
python3 scripts/carpe_diem.py install plan --platform cursor --json > /tmp/carpe-diem-install.json
python3 scripts/carpe_diem.py install apply --plan /tmp/carpe-diem-install.json --yes
python3 scripts/carpe_diem.py install verify --target ~/.cursor/skills/carpe-diem
```

必须在执行 `apply` 前审阅计划。打开新的 Cursor Agent 对话，用“我有 Coding Agent，但不知道做什么”触发。

项目级使用时，可在 `install plan` 中通过 `--target /absolute/project/.cursor/skills/carpe-diem` 指定目标。部分 Cursor 版本也识别项目内 `.agents/skills/`；本仓库默认选择 Cursor 自身目录，以便安装结果明确且可验证。

这些发现目录依据 Cursor 官方的 [Agent Skills 文档](https://cursor.com/docs/skills)。

## 卸载

```bash
python3 scripts/carpe_diem.py install uninstall --target ~/.cursor/skills/carpe-diem --yes
```
