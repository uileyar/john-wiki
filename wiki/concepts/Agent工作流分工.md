---
title: "Agent 工作流分工"
type: concept
tags: [workflow, agent]
sources: [claude-code-best-practice-workflow-guide]
last_updated: 2026-05-04
---

# Agent 工作流分工

[[Agent工作流分工]] 指把 agent 使用过程拆成清晰层级：入口触发、可复用方法、独立执行上下文、稳定规则、长期记忆和外部工具。它的目标是让 agent 从“能聊”变成“能稳定跑流程”。

## 分层

- [[Command]]：固定入口和触发词。
- [[Skill]]：沉淀可复用方法、步骤和判断标准。
- [[Subagent]]：处理长任务、重任务或需要独立上下文的任务。
- settings：存放稳定全局规则。
- memory：存放持续性背景和长期记忆。
- [[MCP]]：接入外部工具、数据源和系统能力。

## 关联

- [[ClaudeCode]] —— 该概念在源文中面向的工具。
- [[Codex执行偏好]] —— 本 vault 将类似分工迁移到 Codex 操作约定中。
