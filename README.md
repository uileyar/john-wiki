# john-wiki

这是一个 Karpathy 风格的个人 LLM Wiki，运行在 Obsidian vault 中。它的目标不是每次问答临时做 RAG，而是把源文档、问答和综合判断持续沉淀成可链接、可演进的 wiki 页面。

## 三层结构

```text
raw/        不可变源文档：文章、论文、会议、书籍、转录、草稿
wiki/       LLM 维护层：source/entity/concept/synthesis 页面
AGENTS.md   Codex 使用的 schema、命名规范和工作流约定
```

Obsidian 负责浏览、搜索和图谱视图；Codex 负责摄入、查询、体检和图谱生成。正文和 prompt 默认中文，frontmatter 字段名保留英文以兼容 Dataview 与上游工具。`CLAUDE.md` 与 `GEMINI.md` 作为其他 agent CLI 的兼容入口保留。

## 快速命令

| 命令 | 用途 |
|---|---|
| `/wiki-health` | 结构性体检，0 LLM 调用 |
| `/wiki-ingest raw/articles/example.md` | 摄入一份源文档 |
| `/wiki-query RAG 和持久化 wiki 有什么区别？` | 从已有 wiki 综合回答 |
| `/wiki-lint` | 语义体检：死链、孤立页、矛盾、缺口 |
| `/wiki-graph` | 重建 `graph/graph.json` 与交互图谱 |

自然语言也可以触发同样流程，例如“帮我把 `raw/papers/transformer.pdf` 收进来”。

## 日常工作流

1. 把不可变源放到 `raw/` 下对应目录。
2. 在 Codex 里运行 `/wiki-health` 或直接说“健康检查”做预检。
3. 运行 `/wiki-ingest raw/...` 生成 source 页，并更新 index、overview、entity、concept 和 log。
4. 用 `/wiki-query ...` 综合已有内容；值得保留的回答归档到 `wiki/syntheses/`。
5. 每摄入 10-15 个源后运行 `/wiki-lint`，需要图谱时运行 `/wiki-graph`。

## Python 环境

推荐使用虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python tools\health.py
```

非 markdown 文件会通过 `markitdown` 转换；PDF 可用 `pymupdf4llm` 做高保真转换；YouTube 链接可先用：

```powershell
python tools\youtube2md.py "https://www.youtube.com/watch?v=..."
```

## Obsidian 可选增强

- Dataview：按 `type/tags/sources/last_updated` 查询页面。
- Templater：把 source、diary、meeting 模板做成快捷模板。
- Obsidian Web Clipper：默认保存路径设为 `raw/articles/`。

## 参考

- [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)
- [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)
