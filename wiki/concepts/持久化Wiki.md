---
title: "持久化 Wiki"
type: concept
tags: [llm-wiki, pkm]
sources: [karpathy-llm-wiki]
last_updated: 2026-05-04
---

# 持久化 Wiki

[[持久化Wiki]] 指由 LLM 持续维护的结构化 markdown 知识库。它不是临时检索层，而是每次摄入、查询和综合都会更新的长期 artifact。

## 与临时 RAG 的区别

- 临时 RAG 在问题发生时检索片段，再现场综合。
- 持久化 wiki 在摄入时就把摘要、实体、概念、矛盾和交叉引用写入文件。
- 查询结果如果有长期价值，会继续沉淀为 synthesis 页面。

## 关联

- [[三层架构]] —— 持久化 wiki 的目录和治理结构。
- [[知识复利]] —— 持久化 wiki 的主要收益。
