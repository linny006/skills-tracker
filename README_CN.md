# skills-tracker

> 实时追踪 GitHub 上所有新建的 'skills' 仓库，捕捉 AI 智能体技能生态的趋势动向

[English](./README.md) · **中文** · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md)

[![Stars](https://img.shields.io/github/stars/linny006/skills-tracker?style=for-the-badge&logo=github)](https://github.com/linny006/skills-tracker/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/skills-tracker?style=for-the-badge)](https://github.com/linny006/skills-tracker/commits)

---

一个实时追踪器，每 15 分钟扫描一次 GitHub，监控新建的 'skills' 仓库，记录 Star 数、编程语言分布及元数据。这个自动更新的数据集帮助开发者、投资人和研究者在 AI 智能体技能生态的命名趋势消退之前，提前发现规律。

本列表由 GitHub Actions 定时任务**每 15 分钟自动更新一次**。每次提交都反映上游数据源的真实变化——新增条目、移除过期条目——你看到的内容始终是最新的。

---

每 15 分钟，GitHub Action 会运行 `tracker.py`，该脚本会：

1. 从 `GitHub Search API` 拉取最新状态。
2. 与 `data/items.json`（上一次快照）做差异对比。
3. 在 `<!-- TRACKER_TABLE_* -->` 标记之间重写上方的表格。
4. 如有变化，提交 `feat: +N added, -M removed (timestamp)`。

无需外部服务，无需付费 API，只用公开数据源和免费的 GitHub Action。

---

## 📋 Live data

实时数据请查看英文版 README

---

## 🔗 Related live trackers

- [trending-claude-skills](https://github.com/linny006/trending-claude-skills) — What's shipping in Claude Skills this week (`topic:claude-skills`)
- [mcp-servers-live](https://github.com/linny006/mcp-servers-live) — Live index of newest MCP servers (`topic:mcp-server`)
- [cursor-rules-live](https://github.com/linny006/cursor-rules-live) — Newest Cursor rules and .cursorrules patterns (`topic:cursor-rules`)
- [claude-code-plugin-tracker](https://github.com/linny006/claude-code-plugin-tracker) — Claude Code plugins and hook configs (`topic:claude-code`)
- [llm-agents-radar](https://github.com/linny006/llm-agents-radar) — Newest LLM agent frameworks (`topic:llm-agent`)
- [rag-radar](https://github.com/linny006/rag-radar) — Newest RAG implementations and tools (`topic:rag`)
- [llm-eval-tracker](https://github.com/linny006/llm-eval-tracker) — Newest LLM evaluation tools and benchmarks (`topic:llm-eval`)
- [agent-framework-radar](https://github.com/linny006/agent-framework-radar) — Newest agent frameworks shipping on GitHub (`topic:agent-framework`)
- [vector-db-live](https://github.com/linny006/vector-db-live) — Newest vector DB projects and integrations (`topic:vector-database`)
- [llmops-radar](https://github.com/linny006/llmops-radar) — Newest LLMOps tooling (observability, deployment) (`topic:llmops`)
- [prompt-tools-live](https://github.com/linny006/prompt-tools-live) — Newest prompt-engineering tools and prompt repos (`topic:prompt-engineering`)
- [agent-eval-harness](https://github.com/linny006/agent-eval-harness) — Live benchmark of AI coding agents (`topic:llm-eval`)
- [awesome-agent-skills](https://github.com/linny006/awesome-agent-skills) — Curated auto-updated awesome-list of AI agent skills (`topic:agent-skills`)

---

## 📜 License

MIT — see `LICENSE`.
