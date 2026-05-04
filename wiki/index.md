# Wiki 目录

*由 Codex 在每次 ingest 时维护，请勿手工编辑。*

## 综述
- [Overview](overview.md) —— 跨源活文档

## 源
- [一键把 PDF/Word/Excel 全转成 AI 最爱的格式](sources/markitdown-convert-documents-to-markdown.md) —— 介绍 MarkItDown 与多源转 Markdown
- [claude-code-best-practice：Claude Code 工作流指南](sources/claude-code-best-practice-workflow-guide.md) —— 梳理 command、skill、subagent、settings、memory、MCP 的分工
- [Obsidian + LLM Wiki 落地指南](sources/obsidian-llm-wiki-implementation-guide.md) —— 补充 Obsidian + LLM Wiki 的落地实践线索
- [Claude Code Pro/Max 默认 effortLevel 是 medium](sources/claude-code-effortlevel-medium.md) —— 提醒检查 Claude Code 推理强度配置
- [Karpathy LLM Wiki](sources/karpathy-llm-wiki.md) —— 提出 raw/wiki/schema 三层结构和持久化 LLM Wiki 范式

## 实体
- [MarkItDown](entities/MarkItDown.md) —— 多格式转 Markdown 工具
- [Andrej Karpathy](entities/AndrejKarpathy.md) —— LLM Wiki 模式的提出者
- [Obsidian](entities/Obsidian.md) —— 本 vault 的 markdown 浏览和图谱环境
- [Claude Code](entities/ClaudeCode.md) —— 维护 wiki 的 agent 工作环境

## 概念
- [Codex 执行偏好](concepts/Codex执行偏好.md) —— 本 vault 中面向 Codex 的操作纪律
- [多源转 Markdown](concepts/多源转Markdown.md) —— 非 markdown 文件进入 ingest 前的转换步骤
- [MCP](concepts/MCP.md) —— agent 接入外部工具、数据源和系统能力的方式
- [Subagent](concepts/Subagent.md) —— 长任务或独立上下文任务的执行分担层
- [Skill](concepts/Skill.md) —— 可复用方法、步骤和判断标准的沉淀层
- [Command](concepts/Command.md) —— 固定入口与流程触发层
- [Agent 工作流分工](concepts/Agent工作流分工.md) —— 将 agent 能力拆成入口、复用、执行、配置、记忆和工具层
- [effortLevel](concepts/effortLevel.md) —— 影响 Claude Code 推理强度的配置概念
- [三层架构](concepts/三层架构.md) —— raw、wiki、schema 的组织模型
- [持久化 Wiki](concepts/持久化Wiki.md) —— 与临时 RAG 相对的长期知识 artifact
- [知识复利](concepts/知识复利.md) —— ingest/query/lint 持续积累的收益
- [Wikilinks](concepts/wikilinks.md) —— Obsidian 风格的双向链接语法

## 综合（Syntheses）
- [wiki 里关于 LLM Wiki 的内容综合](syntheses/llm-wiki-summary.md) —— 综合当前 wiki 对 LLM Wiki 的理念、架构、落地和工作流理解
- [Karpathy 提倡的三层结构是什么？](syntheses/karpathy-three-layer-architecture.md) —— 首个 query 归档，解释 raw/wiki/schema 三层结构
