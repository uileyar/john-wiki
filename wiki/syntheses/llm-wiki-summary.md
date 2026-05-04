---
title: "wiki 里关于 LLM Wiki 的内容综合"
type: synthesis
tags: [llm-wiki, synthesis]
sources: [karpathy-llm-wiki, obsidian-llm-wiki-implementation-guide, markitdown-convert-documents-to-markdown, claude-code-best-practice-workflow-guide]
last_updated: 2026-05-04
---

# wiki 里关于 LLM Wiki 的内容综合

LLM Wiki 在这个 vault 里的核心意思是：不要把知识库只当作“每次提问时临时检索”的 RAG 语料，而是让 LLM 持续维护一个结构化、可链接、会随时间增长的长期 wiki。它的目标是把摘要、概念、实体、矛盾、综述和问答结果都沉淀成文件，让下一次查询站在已有结构上继续生长，而不是从零拼答案。[[持久化Wiki]] [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]]

它的基础结构是 [[三层架构]]：`raw/` 保存不可变源文档，`wiki/` 保存 LLM 维护的 source/entity/concept/synthesis 等页面，`AGENTS.md`/`CLAUDE.md` 这类 schema 文件规定 agent 如何摄入、查询、体检和建图。这个结构把“事实来源”“知识整理层”“工作流规则”分开，减少混乱。[[三层架构]]

在使用方式上，LLM Wiki 的关键动作是 ingest 和 query。ingest 不是简单复制原文，而是把源材料整理成 source 页，并补充关联概念、实体、`overview.md`、`index.md` 和 `log.md`；query 也不只是回答，如果答案有长期价值，就应该归档为 synthesis 页面。这样每次操作都会增加一点长期可复用资产，形成 [[知识复利]]。[[知识复利]]

落地到 Obsidian 时，[[Obsidian]] 负责本地 markdown 浏览、双链和图谱视图；agent 负责维护页面、更新索引、检查结构和重建图谱。[[sources/obsidian-llm-wiki-implementation-guide|Obsidian + LLM Wiki 落地指南]] 也强调这个方向：把 LLM 维护的知识花园落到本地文件系统，而不是停留在一次性问答。[[Obsidian]] [[持久化Wiki]]

多源输入方面，wiki 里已经把 [[多源转Markdown]] 作为 ingest 前置步骤：PDF、Word、Excel、PPT、HTML、音频、YouTube 转录等复杂材料先转成 Markdown，再进入 LLM Wiki。当前工具线索是 [[MarkItDown]]，它服务于“把复杂格式变成 LLM 更容易处理、Obsidian 更容易保存的文本”。[[多源转Markdown]] [[sources/markitdown-convert-documents-to-markdown|一键把 PDF/Word/Excel 全转成 AI 最爱的格式]]

另一个实践重点是 agent 工作流本身。wiki 里吸收了 [[Agent工作流分工]] 的思路：[[Command]] 负责入口，[[Skill]] 负责可复用方法，[[Subagent]] 负责长任务，settings/memory 负责稳定规则和长期背景，[[MCP]] 负责外部工具能力。这些原则被迁移到本 vault 的 [[Codex执行偏好]]：明确任务直接执行、写入受控、先看状态、避免提交本地状态和生成产物。[[sources/claude-code-best-practice-workflow-guide|Claude Code 工作流指南]]

## 引用源

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]]
- [[持久化Wiki]]
- [[三层架构]]
- [[知识复利]]
- [[sources/obsidian-llm-wiki-implementation-guide|Obsidian + LLM Wiki 落地指南]]
- [[多源转Markdown]]
- [[sources/markitdown-convert-documents-to-markdown|一键把 PDF/Word/Excel 全转成 AI 最爱的格式]]
- [[Agent工作流分工]]
