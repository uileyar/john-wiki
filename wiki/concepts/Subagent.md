---
title: "Subagent"
type: concept
tags: [workflow, agent]
sources: [claude-code-best-practice-workflow-guide]
last_updated: 2026-05-04
---

# Subagent

[[Subagent]] 是 agent 工作流中的执行分担层，适合处理长任务、重任务或需要独立上下文的任务。它的价值是让主会话保留判断和调度能力，而不是把所有复杂执行都塞进同一个上下文。

## 关联

- [[Agent工作流分工]] —— subagent 是长任务执行层。
- [[Skill]] —— subagent 可以按 skill 中的方法执行具体任务。
