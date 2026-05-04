---
title: "Command"
type: concept
tags: [workflow, agent]
sources: [claude-code-best-practice-workflow-guide]
last_updated: 2026-05-04
---

# Command

[[Command]] 是 agent 工作流中的入口层，适合承载触发词和固定流程包装。对于本 vault，`/wiki-ingest`、`/wiki-query`、`/wiki-health`、`/wiki-lint` 和 `/wiki-graph` 都属于 command 思路。

## 关联

- [[Agent工作流分工]] —— command 是入口层。
- [[Skill]] —— command 可以调用或依赖可复用方法。
