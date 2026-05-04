---
title: "Karpathy 提倡的三层结构是什么？"
type: synthesis
tags: [llm-wiki, architecture]
sources: [karpathy-llm-wiki]
last_updated: 2026-05-04
---

# Karpathy 提倡的三层结构是什么？

Karpathy 的 LLM Wiki 模式可以理解为 [[三层架构]]：底层是不可变的 `raw/` 源文档，中间是由 LLM 持续维护的 `wiki/` 结构化页面，顶层是 `CLAUDE.md`/`AGENTS.md` 这样的 schema 与工作流约定。这个结构的重点不是把文件临时塞给模型检索，而是让每次摄入都更新 [[持久化Wiki]]，把摘要、实体、概念、矛盾和交叉引用写进长期文件。[[sources/karpathy-llm-wiki|Karpathy LLM Wiki]]

这三层分别承担不同责任：`raw/` 是事实来源，原则上不被改写；`wiki/` 是可演进的知识层，由 source、entity、concept、synthesis、overview、index 和 log 组成；schema 层规定 agent 如何命名、读取、写入、查询、体检和建图。这样，后续 query 可以站在已有结构上继续综合，形成 [[知识复利]]。[[三层架构]]

## 引用源

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]]
- [[三层架构]]
- [[持久化Wiki]]
- [[知识复利]]
