---
title: "Karpathy LLM Wiki"
source_url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
date: 2026-04-04
---

# Karpathy LLM Wiki

这是一份用于首次摄入测试的源笔记，来源为 Andrej Karpathy 的 `llm-wiki.md` gist。为避免把外部原文整篇复制进 vault，这里只保留来源链接和可验证的摘要性笔记。

## 摘要笔记

- 核心主张：不要把个人知识库只当作每次问答时临时检索的 RAG 语料，而应让 LLM 逐步维护一个持久、结构化、互相链接的 wiki。
- 架构分为三层：不可变 raw sources、由 LLM 维护的 wiki、约束 agent 行为的 schema 文件。
- 每次 ingest 都应生成或更新 source、entity、concept、overview、index 和 log，让知识在文件系统中复利。
- Obsidian 适合作为这类 wiki 的浏览与图谱界面，LLM agent 则负责维护、摘要、交叉引用和一致性检查。
- 查询不只是回答问题；有价值的回答也应该沉淀为 synthesis 页面，成为后续知识网络的一部分。

## 参考

- Karpathy LLM Wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
