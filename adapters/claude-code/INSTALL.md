# Claude Code 适配

## 用户级安装

默认目标是 `~/.claude/skills/carpe-diem`：

```bash
python3 scripts/carpe_diem.py install plan --platform claude-code --json > /tmp/carpe-diem-install.json
```

检查计划中的源目录、目标目录、版本、文件和指纹，再一次批准：

```bash
python3 scripts/carpe_diem.py install apply --plan /tmp/carpe-diem-install.json --yes
python3 scripts/carpe_diem.py install verify --target ~/.claude/skills/carpe-diem
```

新开 Claude Code 会话后，用“帮我找到一个值得做的开源项目”触发。若所用版本没有自动加载用户 Skill，明确要求读取 `~/.claude/skills/carpe-diem/SKILL.md`。

个人与项目目录依据 Claude Code 官方的 [Skills 文档](https://code.claude.com/docs/en/slash-commands)。

## 卸载

```bash
python3 scripts/carpe_diem.py install uninstall --target ~/.claude/skills/carpe-diem --yes
```

安装副本被修改后，安全卸载会拒绝删除。
