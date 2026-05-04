# Wiki Log

仅追加的 wiki 操作时间线，由 Claude Code 维护。

格式：`## [YYYY-MM-DD] <operation> | <title>`

查看最近记录：

```bash
grep "^## \[" wiki/log.md | tail -10
```

---

## [2026-05-04] query | wiki 里关于 llm wiki 的内容综合一下

基于当前 LLM Wiki 相关 source、concept 与 overview 页面综合回答，并归档为 `wiki/syntheses/llm-wiki-summary.md`。

## [2026-05-04] ingest | raw/articles 新增源文件

摄入 4 个新增 raw 源：Claude Code effortLevel 短帖、Obsidian + LLM Wiki 落地指南、Claude Code 工作流指南、MarkItDown 转换文章。新增 source 页面 4 个，补充 MarkItDown 实体与 effortLevel、Agent 工作流分工、Command、Skill、Subagent、MCP、多源转 Markdown、Codex 执行偏好等概念页，并更新 index、overview 与 ClaudeCode 实体页。

## [2026-05-04] ingest | Claude Code Pro/Max 默认 effortLevel 是 medium

新增 source：`wiki/sources/claude-code-effortlevel-medium.md`。关键论点：Claude Code 的 effortLevel 档位值得作为配置检查项，但短帖说法需要后续官方来源验证。

## [2026-05-04] ingest | Obsidian + LLM Wiki 落地指南

新增 source：`wiki/sources/obsidian-llm-wiki-implementation-guide.md`。关键论点：Obsidian 可以作为持久化 LLM Wiki 的本地浏览、编辑与图谱界面。

## [2026-05-04] ingest | claude-code-best-practice：Claude Code 工作流指南

新增 source：`wiki/sources/claude-code-best-practice-workflow-guide.md`。关键论点：agent 工作流应拆分为 command、skill、subagent、settings、memory 和 MCP 等层次。

## [2026-05-04] ingest | 一键把 PDF/Word/Excel 全转成 AI 最爱的格式

新增 source：`wiki/sources/markitdown-convert-documents-to-markdown.md`。关键论点：MarkItDown 可以把多种文档格式转换为 Markdown，作为 LLM Wiki ingest 的前置转换步骤。

## [2026-05-04] query | Karpathy 提倡的三层结构是什么？

基于首次摄入内容生成并归档 synthesis：`wiki/syntheses/karpathy-three-layer-architecture.md`。

## [2026-05-04] ingest | Karpathy LLM Wiki

新增首次摄入测试源，创建 source、entity 与 concept 页面，并更新 index 与 overview。关键论点：LLM Wiki 应把知识维护为持久、结构化、互相链接的 artifact，而不是每次查询临时重新检索。

## [2026-05-04] init | 仓库初始化

初始化 Karpathy 风格 LLM Wiki 的目录骨架、schema 与工具链。

## [2026-05-04] graph | Knowledge graph rebuilt

9 nodes, 24 edges (24 extracted, 0 inferred).

## [2026-05-04] graph | Knowledge graph rebuilt

9 nodes, 24 edges (24 extracted, 0 inferred).

## [2026-05-04] graph | Knowledge graph rebuilt

10 nodes, 28 edges (28 extracted, 0 inferred).

## [2026-05-04] graph | Knowledge graph rebuilt

23 nodes, 76 edges (76 extracted, 0 inferred).
