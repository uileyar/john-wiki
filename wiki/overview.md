---
title: "Wiki 综述"
type: synthesis
tags: []
sources: []
last_updated: 2026-05-04
---

# Wiki 综述

本页是跨源综述，会在每次 `/wiki-ingest` 后由 Claude Code 更新，用来沉淀当前 wiki 对重要主题、实体和概念的整体理解。

当前 wiki 的第一个主题是 [[持久化Wiki]]：让 LLM 在摄入时维护一个结构化、互相链接、可演进的 markdown 知识库，而不是在每次查询时从 raw 文档里重新拼装答案。[[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] 将该模式组织为 [[三层架构]]：不可变 `raw/`、LLM 维护的 `wiki/`、约束 agent 行为的 schema 文件。

围绕这套模式，[[Obsidian]] 承担浏览、链接和图谱视图，[[ClaudeCode]] 承担维护、摘要、体检和更新。长期价值来自 [[知识复利]]：source、entity、concept、synthesis、index 和 log 每次都被更新，后续查询可以站在既有结构上继续生长。
