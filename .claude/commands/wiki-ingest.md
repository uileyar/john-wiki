把一份源文档摄入 wiki。

用法：`/wiki-ingest $ARGUMENTS`

`$ARGUMENTS` 应该是 `raw/` 下的文件路径，例如 `raw/articles/my-article.md`。

如果是非 markdown 格式（PDF、Word、PPT、Excel、HTML、EPUB、ipynb 等），先用 `python tools/file_to_md.py <path>` 或 `markitdown` 转成 markdown。YouTube 链接用 `python tools/youtube2md.py <url>` 拉转录。

严格按 `CLAUDE.md` 的"Ingest 工作流"执行：

1. 用 Read 工具读完源文件（必要时先转换）
2. 读 `wiki/index.md` 与 `wiki/overview.md` 了解当前上下文
3. 写 `wiki/sources/<slug>.md`（用 CLAUDE.md 里对应的页面模板：默认源 / 日记 / 会议 / 论文 任选其一）
4. 更新 `wiki/index.md`：在 `## 源` 段加新条目
5. 必要时更新 `wiki/overview.md`
6. 创建/更新涉及的 entity 页（`wiki/entities/`）—— 人、公司、项目、产品
7. 创建/更新涉及的 concept 页（`wiki/concepts/`）—— 概念、框架
8. 标注与已有 wiki 的矛盾
9. 追加 `wiki/log.md`：`## [YYYY-MM-DD] ingest | <标题>`

完成所有写入后，用一段中文总结：新增了什么、哪些页被创建/更新、发现了哪些矛盾。
