向 wiki 提问并综合一段答案。

用法：`/wiki-query $ARGUMENTS`

`$ARGUMENTS` 是要回答的问题，例如 `所有源里反复出现的主题是什么？`

按 `CLAUDE.md` 的"Query 工作流"执行：

1. 读 `wiki/index.md` 找出最相关的页面
2. 用 Read 工具读这些页（取最相关的 ≤ 10 个）
3. 综合一段中文 markdown 答案，**所有引用都用 `[[页面名]]` 行内 wikilink**
4. 末尾加一段 `## 引用源`，列出所有引用到的页
5. 询问用户是否将本回答归档为 `wiki/syntheses/<slug>.md`

如果 wiki 完全为空，告知用户并建议先用 `/wiki-ingest` 喂源。
