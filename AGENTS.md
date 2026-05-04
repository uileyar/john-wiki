# LLM Wiki — Schema 与工作流约定

这是一个 **Karpathy 风格的个人 wiki**：所有页面由 Codex 维护。直接在 Codex 里打开本仓库，用自然语言对话即可；当用户说“摄入 / 查询 / 健康检查 / lint / 重建图谱”时，按本文工作流直接执行。

> 灵感来源：
> - 理论：Karpathy [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
> - 实现参考：[SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)
>
> 主语言：**中文**。所有 wiki 页面、log 条目、prompt 默认中文撰写；`frontmatter` 字段名（`type/tags/sources/last_updated`）保留英文以兼容 Dataview 与上游工具链。

---

## Codex 命令约定

Codex 环境可能没有真正的 slash command UI；如果用户输入下列 slash 命令，就把它们视为自然语言触发器并执行对应工作流。用户也可以直接用中文描述同一件事。

| 命令 | 用法示例 |
|---|---|
| `/wiki-ingest` | `/wiki-ingest raw/articles/my-article.md` |
| `/wiki-query` | `/wiki-query Karpathy 主张的三层架构是什么？` |
| `/wiki-health` | `/wiki-health`（结构性体检，0 LLM 成本，每次会话开场都跑） |
| `/wiki-lint` | `/wiki-lint`（语义体检，烧 token，每 10–15 次摄入跑一次） |
| `/wiki-graph` | `/wiki-graph`（构建并打开知识图谱） |

也可以用自然语言代替：
- *"帮我把 raw/papers/transformer.pdf 收进来"*
- *"wiki 里关于 RAG 的内容综合一下"*
- *"检查 wiki 有没有孤立页或矛盾"*
- *"重建图谱，看看 RAG 节点连了哪些"*

Codex 会读取本文件作为仓库级操作约定，按下面的工作流执行。

### Codex 执行偏好

- 用户提出明确文件变更时，直接编辑仓库文件；不要只给教程。
- 读取文件优先用 Codex 可用的文件/终端工具；搜索文件优先用 `rg`，不可用时用 PowerShell 原生命令兜底。
- 写文件时遵守当前 Codex 约束：手工编辑优先用 `apply_patch`；不要修改 `raw/` 下已有源文件，除非用户明确要求。
- 运行 Python 工具时在仓库根目录执行，例如 `python tools/health.py`。
- Git 操作前先看 `git status --short --branch`；不要提交被 `.gitignore` 忽略的本地状态文件或生成图谱产物。
- 所有面向用户的 wiki 页面、log 条目和回答默认中文。

---

## 目录结构

```
raw/                 # 不可变源文档 —— 永远不要修改
  articles/          # 网页文章 / 博客
  papers/            # arXiv / 学术 PDF
  books/             # EPUB / 书籍长文
  docs/              # Word / PPT / Excel
  transcripts/       # YouTube / 播客转录
  notes/             # 自己的草稿与零散笔记

wiki/                # Codex 完全拥有的 LLM 维护层
  index.md           # 全部页面的目录 —— 每次 ingest 都更新
  log.md             # 仅追加的时间线
  overview.md        # 跨源综述（活文档）
  sources/           # 每个源一篇摘要页
  entities/          # 人 / 公司 / 项目 / 产品
  concepts/          # 概念 / 框架 / 方法 / 理论
  syntheses/         # 沉淀下来的问答

graph/               # 自动生成的图谱产物（gitignored）
tools/               # 独立 Python 脚本
  health.py          # 结构性检查（确定性，无 LLM 调用）
  lint.py            # 内容质量检查（用 LLM 做语义分析）
  build_graph.py     # 知识图谱生成
  ingest.py / query.py / heal.py / refresh.py
  pdf2md.py / file_to_md.py / youtube2md.py  # 多源转换
```

---

## 页面 frontmatter（统一约定）

```yaml
---
title: "页面标题（中文）"
type: source | entity | concept | synthesis
tags: []
sources: []           # 该页所依据的 source slug 列表
last_updated: 2026-05-04   # ISO 日期 YYYY-MM-DD
---
```

正文用 `[[页面名]]` 维护跨页 wikilinks。

---

## Ingest 工作流

触发：`/wiki-ingest <path>` 或 *"把 …… 收进来"*

**支持格式：** Markdown 直接读；其他格式（`.pdf .docx .pptx .xlsx .html .txt .csv .json .xml .rst .rtf .epub .ipynb .yaml .yml .tsv .wav .mp3`）走 [markitdown](https://github.com/microsoft/markitdown) 自动转 markdown 后再 ingest。YouTube 链接交给 `tools/youtube2md.py`。加 `--no-convert` 跳过转换。

**执行步骤（按序）：**
1. 用 Codex 可用的文件读取工具完整读取源文件（非 markdown 先转换）
2. 读 `wiki/index.md` 与 `wiki/overview.md` 了解当前 wiki 上下文
3. 写 `wiki/sources/<slug>.md`（按下方"源页面模板"）
4. 更新 `wiki/index.md`：在 `## 源` 区段加新条目
5. 更新 `wiki/overview.md`：必要时改写综述
6. 创建/更新涉及的 entity 页（人、公司、项目）
7. 创建/更新涉及的 concept 页（概念、框架）
8. 标注与已有 wiki 内容的矛盾
9. 追加 `wiki/log.md`：`## [YYYY-MM-DD] ingest | <标题>`
10. **后置校验：** 检查所有新写的 `[[wikilinks]]` 是否指向真实页面，确认 index.md 已包含全部新页，最后给一句变更摘要

### 源页面模板（默认）

```markdown
---
title: "源标题（保留原文，可加副标题）"
type: source
tags: []
date: 2026-05-04
source_file: raw/articles/...
---

## 摘要
2–4 句概览。

## 关键论点
- 论点 1
- 论点 2

## 关键引文
> "原文引用" —— 上下文说明

## 关联
- [[实体名]] —— 关系说明
- [[概念名]] —— 关联说明

## 矛盾
- 与 [[其他页]] 在 …… 上有冲突
```

### 领域模板

如果源属于特定领域（日记、会议、论文），用对应模板替代默认源页：

#### 日记模板
```markdown
---
title: "2026-05-04 日记"
type: source
tags: [diary]
date: 2026-05-04
---
## 事件梗概
## 关键决策
## 精力与情绪
## 关联
## 转向与矛盾
```

#### 会议笔记模板
```markdown
---
title: "会议主题"
type: source
tags: [meeting]
date: 2026-05-04
---
## 目标
## 关键讨论
## 已决事项
## 待办（Action Items）
```

#### 论文模板（额外推荐）
```markdown
---
title: "论文标题（保留英文 + 中文副标题）"
type: source
tags: [paper, arxiv]
date: 2026-05-04
source_file: raw/papers/xxxx.pdf
---
## 一句话动机
## 核心方法
## 关键结果
## 局限
## 关联
- [[相关概念]]
- [[相关工作或前作]]
```

---

## Query 工作流

触发：`/wiki-query <问题>` 或 *"wiki 里关于 …… 怎么说？"*

**步骤：**
1. 读 `wiki/index.md` 锁定相关页面
2. 用 Codex 可用的文件读取工具读这些页（≤ 10 个最相关）
3. 综合一段中文回答，**所有引用都用 `[[页面名]]` 行内 wikilink**
4. 末尾加 `## 引用源` 列表
5. 询问用户是否将本回答归档为 `wiki/syntheses/<slug>.md`

如果 wiki 完全为空，直接说"wiki 里还没东西，先用 `/wiki-ingest` 喂点源"。

---

## Lint 工作流

触发：`/wiki-lint` 或 *"检查 wiki 健康"*

**结构性检查（优先用 `rg` / 文件枚举工具）：**
1. **孤立页** —— 没有任何其他页通过 `[[link]]` 链入
2. **死链** —— `[[wikilink]]` 指向不存在的页
3. **缺失实体页** —— 在 ≥ 3 个页面被提到但还没有专属页

**语义检查（读页面、推理）：**
4. **矛盾** —— 跨页冲突的论断
5. **过时摘要** —— 新源已改变了画面但旧摘要没更新
6. **数据缺口** —— wiki 答不上的重要问题，建议要补哪些源

输出结构化的中文 lint 报告，末尾问用户是否保存到 `wiki/lint-report.md`。

追加 `wiki/log.md`：`## [YYYY-MM-DD] lint | wiki 健康检查`

---

## Health 工作流

触发：`/wiki-health` 或 *"健康检查"*

直接运行：`python tools/health.py`（或 `--json` 拿机器可读输出，`--save` 写报告到 `wiki/health-report.md`）

**仅做快速结构完整性检查 —— 0 LLM 调用，每次会话都可以跑：**
- **空/桩文件** —— frontmatter 之外没有内容（限速损坏的痕迹）
- **Index 同步** —— `wiki/index.md` 条目 vs 磁盘上的实际文件
- **Log 覆盖** —— 有源页但 `wiki/log.md` 里没对应 ingest 条目

### Health vs Lint 边界

| 维度 | `health` | `lint` |
|---|---|---|
| **范围** | 结构完整性 | 内容质量 |
| **LLM 调用** | 零 | 有（语义） |
| **成本** | 免费 | Token |
| **频率** | 每次会话开场 | 每 10-15 次 ingest |
| **检查项** | 空文件、index 同步、log 同步 | 孤立页、死链、矛盾、缺口 |
| **工具** | `tools/health.py` | `tools/lint.py` |
| **顺序** | 先（pre-flight） | health 通过后 |

> 先跑 `health`——给空文件做语义 lint 是浪费 token。

---

## Graph 工作流

触发：`/wiki-graph` 或 *"重建图谱"*

跑 `python tools/build_graph.py --open`，做：
- Pass 1：扫所有 `[[wikilinks]]` → 确定性 `EXTRACTED` 边
- Pass 2：推理隐含关系 → `INFERRED` 边带置信度（0.0–1.0），低置信记 `AMBIGUOUS`
- Louvain 社区检测
- 输出 `graph/graph.json` + `graph/graph.html`（vis.js 可交互）

**如果用户没装 Python 环境**，手工生成兜底：
1. 搜索出 wiki/ 下所有 `[[wikilinks]]`
2. 构造 nodes（每页一个，id=相对路径，label=title，type 来自 frontmatter）
3. 构造 edges（每个 wikilink 一条，标 EXTRACTED）
4. 写 `graph/graph.json`（含 `{nodes, edges, built: today}`）
5. 写 `graph/graph.html`（自包含 vis.js 页，按 type 配色，可搜索）

完成后总结：节点数、边数、按类型分布、连通度最高的 hub 节点。

追加 `wiki/log.md`：`## [YYYY-MM-DD] graph | 图谱重建`

---

## 命名规范

- **Source slug**：`kebab-case`，与 raw 源文件名对齐（如 `raw/articles/karpathy-llm-wiki.md` → `wiki/sources/karpathy-llm-wiki.md`）
- **Entity 页**：`TitleCase.md` 或保留原名 —— 英文如 `OpenAI.md`、`SamAltman.md`；中文如 `张三.md`、`字节跳动.md`
- **Concept 页**：`TitleCase.md` 或中文如 `RAG.md`、`涌现能力.md`
- **Source 页**：始终 `kebab-case.md`

---

## Index 格式

```markdown
# Wiki 目录

*由 Codex 在每次 ingest 时维护，请勿手工编辑。*

## 综述
- [Overview](overview.md) —— 跨源活文档

## 源
- [源标题](sources/slug.md) —— 一行摘要

## 实体
- [实体名](entities/EntityName.md) —— 一行描述

## 概念
- [概念名](concepts/ConceptName.md) —— 一行描述

## 综合（Syntheses）
- [分析标题](syntheses/slug.md) —— 回答了什么问题
```

---

## Log 格式

每条以 `## [YYYY-MM-DD] <operation> | <标题>` 开头，便于 grep：

```bash
grep "^## \[" wiki/log.md | tail -10
```

`operation` ∈ `{ ingest, query, health, lint, graph, init }`
