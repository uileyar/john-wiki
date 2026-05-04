构建 wiki 知识图谱并打开。

用法：`/wiki-graph`

首先尝试运行：`python tools/build_graph.py --open`

如果失败（缺依赖），手工构造：

1. 用 Grep 扫 `wiki/` 下所有 `[[wikilinks]]`
2. 构造 nodes 列表：每页一个节点，`id=相对路径`，`label=title`，`type` 从 frontmatter 取
3. 构造 edges 列表：每个 `[[wikilink]]` 一条边，标 `EXTRACTED`
4. 推理隐含关系：通过共现/语义相近补充未被显式 `[[link]]` 的边，标 `INFERRED` 并附置信度（0.0–1.0）；置信度低的标 `AMBIGUOUS`
5. 写 `graph/graph.json`，含 `{nodes, edges, built: 今天的 ISO 日期}`
6. 写 `graph/graph.html`：自包含 vis.js 页（按 type 配色，按 EXTRACTED/INFERRED 区分边色，可搜索可拖拽）

完成后用中文总结：节点数、边数、按类型分布、连通度最高的 hub 节点（前 5）。

追加 `wiki/log.md`：`## [YYYY-MM-DD] graph | 图谱重建`
