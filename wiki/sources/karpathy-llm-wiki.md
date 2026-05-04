---
title: "Karpathy LLM Wiki"
type: source
tags: [article, llm-wiki]
sources: []
date: 2026-04-04
last_updated: 2026-05-04
source_file: raw/articles/karpathy-llm-wiki.md
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---

## 摘要

[[AndrejKarpathy]] 提出的 [[持久化Wiki]] 模式，把个人知识库从“查询时临时检索”转向“摄入时持续编译”。它要求 agent 读取不可变源文档，维护结构化的 markdown wiki，并通过 [[三层架构]]、`index.md` 与 `log.md` 让知识随每次摄入和查询逐步复利。

## 关键论点

- 纯查询时 RAG 容易让 LLM 在每次问题中重新发现、拼接和综合知识，缺少长期积累。
- [[持久化Wiki]] 把综合、交叉引用、矛盾标注和实体/概念整理提前沉淀到文件中。
- [[三层架构]] 将 `raw/` 作为不可变真相来源，`wiki/` 作为 LLM 维护层，`CLAUDE.md`/`AGENTS.md` 作为工作流 schema。
- [[Obsidian]] 适合承担浏览、链接跳转和图谱视图；[[ClaudeCode]] 这类 agent 适合承担维护、摘要、更新和体检。
- 好的 query 结果也应被归档为 synthesis，让问答本身继续增强知识网络。

## 关键引文

> 原文强调 wiki 是持久、复利的 artifact；本页只保留摘要性转述，完整上下文见 source_url。

## 关联

- [[三层架构]] —— 该模式的基础结构：raw、wiki、schema。
- [[持久化Wiki]] —— 与临时 RAG 相对的核心知识管理范式。
- [[知识复利]] —— 每次 ingest/query 都应增加长期可复用资产。
- [[Obsidian]] —— 作为 markdown wiki 的浏览和图谱界面。
- [[ClaudeCode]] —— 作为维护 wiki 的 agent 环境之一。

## 矛盾

- 暂未发现与现有 wiki 内容冲突的论断。
