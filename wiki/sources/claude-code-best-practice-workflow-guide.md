---
title: "claude-code-best-practice：Claude Code 工作流指南"
type: source
tags: [article, claude-code, workflow]
sources: []
date: 2026-04-19
last_updated: 2026-05-04
source_file: raw/articles/claude-code-best-practice：Claude Code 工作流指南.md
source_url: https://mp.weixin.qq.com/s/X-r1cLYRGZk0aXkW9SVk4w
---

## 摘要

这篇文章介绍 `shanraisshan/claude-code-best-practice`，重点不是基础命令，而是 [[ClaudeCode]] 的 [[Agent工作流分工]]。它把能力拆成 [[Command]]、[[Skill]]、[[Subagent]]、settings、memory 与 [[MCP]]，强调真实项目中需要把入口、复用方法、长任务、稳定规则和外部工具分别放到合适层级。

## 关键论点

- [[ClaudeCode]] 真正难点往往不是“会不会用”，而是上下文、职责和流程是否失控。
- [[Command]] 适合固定入口和触发词，[[Skill]] 适合沉淀可复用方法，[[Subagent]] 适合长任务或独立上下文任务。
- settings 更适合放稳定全局规则，memory 更适合长期背景，[[MCP]] 更适合接外部工具和数据源。
- 最短闭环是挑一个重复任务，固定 command，沉淀 skill，把重执行切给 subagent，再把稳定规则和外部能力纳入长期流程。

## 关键引文

> "这不是教你几条 Claude Code 小技巧的仓库，而是教你怎么把 Claude Code 组织成一套可复用、可协作、可持续迭代的工作流。"

## 关联

- [[ClaudeCode]] —— 被组织成工作流的工具。
- [[Agent工作流分工]] —— 文章核心主题。
- [[Command]]、[[Skill]]、[[Subagent]]、[[MCP]] —— 工作流分层中的关键能力。
- [[Codex执行偏好]] —— 本 vault 中可迁移到 Codex 的操作纪律。

## 矛盾

- 该源面向 Claude Code；迁移到 Codex 时，具体机制不一定一一对应，但“入口、方法、长任务、稳定规则、外部工具分层”的原则可复用。
