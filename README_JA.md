# skills-tracker

> GitHub に新しく作られる 'skills' リポジトリをリアルタイムで追跡し、AI エージェントスキルエコシステムのトレンドをキャプチャ

[English](./README.md) · [中文](./README_CN.md) · **日本語** · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md)

[![Stars](https://img.shields.io/github/stars/linny006/skills-tracker?style=for-the-badge&logo=github)](https://github.com/linny006/skills-tracker/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/skills-tracker?style=for-the-badge)](https://github.com/linny006/skills-tracker/commits)

---

15 分ごとに GitHub をスキャンして 'skills' という名前の新しいリポジトリを監視し、スター数・言語の内訳・メタデータを記録するライブトラッカーです。この自動更新データセットを使えば、開発者・投資家・研究者が AI エージェントスキルエコシステムの命名トレンドをフェードアウトする前にいち早く把握できます。

このリストは GitHub Actions の cron によって**15 分ごとに自動更新**されます。各コミットはアップストリームデータソースの実際の変化（新規追加・期限切れ削除）を反映しているので、表示内容は常に最新です。

---

15 分ごとに GitHub Action が `tracker.py` を実行します。このスクリプトは以下を行います：

1. `GitHub Search API` から最新の状態を取得。
2. `data/items.json`（前回のスナップショット）と差分を比較。
3. `<!-- TRACKER_TABLE_* -->` マーカー間のテーブルを書き換え。
4. 変更があれば `feat: +N added, -M removed (timestamp)` をコミット。

外部サービス不要。有料 API 不要。公開データソースと無料の GitHub Action だけで動きます。

---

## 📋 Live data

ライブデータは英語版 README をご覧ください

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
