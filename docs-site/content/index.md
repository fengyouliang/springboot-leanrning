# Spring Boot Learning：主线之书

这个站点把仓库里的多模块 `docs/` 聚合成一个可搜索的静态站点，并且把“跨模块主线”整理成一套 **Book-only** 的书籍目录。

---

## Start Here（推荐入口）

- 书的目录与阅读方法：[主线之书 · 目录](book/index.md)
- 直接开始跑与读：[第 0 章：Start Here](book/00-start-here.md)

---

## 先跑起来（最小闭环）

```bash
mvn -q test
```

只跑单模块（更快）：

```bash
mvn -q -pl <module> test
```

---

## 模块 docs（素材库/索引）

侧边栏不再展示“模块 → 章节”的全量目录；模块 docs 仍然存在，并可通过书内链接与搜索访问。

- 模块入口总览：[modules/index.md](modules/index.md)
