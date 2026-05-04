对 wiki 做结构性体检（0 LLM 成本，每次会话开场都可以跑）。

用法：`/wiki-health`

直接运行：`python tools/health.py`

如果用户加了 `--save`，跑 `python tools/health.py --save` 把报告写到 `wiki/health-report.md`。
如果用户要机器可读输出，跑 `python tools/health.py --json`。

如果 Python 环境未就绪（命令报错），手工兜底（用 Glob / Read）：
1. **空/桩文件** —— 列出 `wiki/**/*.md` 中正文（去掉 frontmatter 后）少于 50 字符的页
2. **Index 同步** —— 列出 `wiki/index.md` 里有但磁盘上没有的条目，反之亦然
3. **Log 覆盖** —— 列出 `wiki/sources/*.md` 中没有对应 `## [YYYY-MM-DD] ingest | <title>` 行的源页

用一段紧凑的中文报告输出三类问题的数量与样例。**不写 log**（health 是预检，不污染时间线）。
