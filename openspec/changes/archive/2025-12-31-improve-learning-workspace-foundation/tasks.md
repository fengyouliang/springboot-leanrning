## 1. 学习体验（导航 + 一致性）
- [x] 1.1 新增仓库级学习进度入口：`docs/progress.md`（中文）
- [x] 1.2 更新根 `README.md`：增加进度入口链接 + “Debug 工具箱”统一入口

## 2. 模块文档一致性：`springboot-basics`
- [x] 2.1 新增 `springboot-basics/docs/` 最小章节集（中文，按 `01-*.md` 编号）
- [x] 2.2 更新 `springboot-basics/README.md`：补充 docs 推荐阅读顺序 + 概念→测试/代码映射入口

## 3. 模块文档一致性：`springboot-web-mvc`
- [x] 3.1 新增 `springboot-web-mvc/docs/` 最小章节集（中文，按 `01-*.md` 编号）
- [x] 3.2 更新 `springboot-web-mvc/README.md`：补充 docs 推荐阅读顺序 + 概念→测试/代码映射入口

## 4. 工程底座（可复现 + 护栏）
- [x] 4.1 新增 `.editorconfig`（统一缩进/换行符/编码）
- [x] 4.2 在根 `pom.xml` 加入 Maven Enforcer（Java 17、Maven 版本下限）
- [x] 4.3 新增 GitHub Actions CI：默认跑 `mvn -q test`（JDK 17）
- [x] 4.4 新增 `scripts/`：封装 `test-all`、`test-module`、`run-module` 等常用命令（保持轻量）

## 5. Validation
- [x] 5.1 全仓库测试：`mvn -q test`
- [x] 5.2 抽查：`mvn -q -pl springboot-basics test`、`mvn -q -pl springboot-web-mvc test`
