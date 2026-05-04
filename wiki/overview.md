---
title: "Wiki 综述"
type: synthesis
tags: []
sources: [karpathy-llm-wiki, claude-code-effortlevel-medium, obsidian-llm-wiki-implementation-guide, claude-code-best-practice-workflow-guide, markitdown-convert-documents-to-markdown]
last_updated: 2026-05-04
---

# Wiki 综述

本页是跨源综述，会在每次 `/wiki-ingest` 后由 Codex 更新，用来沉淀当前 wiki 对重要主题、实体和概念的整体理解。

当前 wiki 的第一个主题是 [[持久化Wiki]]：让 LLM 在摄入时维护一个结构化、互相链接、可演进的 markdown 知识库，而不是在每次查询时从 raw 文档里重新拼装答案。[[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] 将该模式组织为 [[三层架构]]：不可变 `raw/`、LLM 维护的 `wiki/`、约束 agent 行为的 schema 文件。

围绕这套模式，[[Obsidian]] 承担浏览、链接和图谱视图，[[ClaudeCode]] 承担维护、摘要、体检和更新。长期价值来自 [[知识复利]]：source、entity、concept、synthesis、index 和 log 每次都被更新，后续查询可以站在既有结构上继续生长。

新增的几篇 raw 源把这个模式向实际操作推进了一步：[[sources/obsidian-llm-wiki-implementation-guide|Obsidian + LLM Wiki 落地指南]] 指向本地知识库的落地实践；[[sources/markitdown-convert-documents-to-markdown|一键把 PDF/Word/Excel 全转成 AI 最爱的格式]] 把 [[MarkItDown]] 和 [[多源转Markdown]] 纳入摄入前处理；[[sources/claude-code-best-practice-workflow-guide|Claude Code 工作流指南]] 则把 [[Agent工作流分工]] 拆成 [[Command]]、[[Skill]]、[[Subagent]]、settings、memory 和 [[MCP]]。

这些源也给 Codex 入口带来一个实践方向：保留 [[ClaudeCode]] 生态中“分层、可复用、可检查”的经验，同时在 `AGENTS.md` 中转写为 [[Codex执行偏好]]。对于 [[effortLevel]] 这类具体配置，当前 wiki 只把它作为待核验提醒，不把短帖经验当作官方事实。
