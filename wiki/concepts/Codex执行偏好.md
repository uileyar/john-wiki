---
title: "Codex 执行偏好"
type: concept
tags: [codex, workflow]
sources: [claude-code-effortlevel-medium, claude-code-best-practice-workflow-guide]
last_updated: 2026-05-04
---

# Codex 执行偏好

[[Codex执行偏好]] 是本 vault 在 `AGENTS.md` 中为 Codex 固化的操作习惯：明确任务直接执行，先读仓库上下文，写文件用受控编辑方式，运行工具在仓库根目录，git 操作前先看状态，并避免把本地状态文件或生成产物提交进去。

## 来源关系

- [[effortLevel]] 提醒要关心 agent 的配置与推理强度。
- [[Agent工作流分工]] 提醒要把入口、复用方法、长任务、稳定规则和外部工具分层。

## 关联

- [[Command]] —— Codex 将 slash 命令视为自然语言触发器。
- [[Skill]] —— 可复用方法应进入明确规则或技能。
