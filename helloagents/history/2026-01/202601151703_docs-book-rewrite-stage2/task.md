# Task List：全模块文档书籍化重写（Stage 2：主线时间线重排）

Directory: `helloagents/plan/202601151703_docs-book-rewrite-stage2/`

---

## 1. 全局写作规范与站点入口
- [√] 1.1 新增书籍式写作指南：`docs-site/content/book-style.md`（提示框/叙事结构/重排原则）
- [√] 1.2 更新站点导航增加“写作指南”入口：`docs-site/mkdocs.yml`（模板）

## 2. 全部模块：新增时间线章节 + 重排目录
- [√] 2.1 `springboot-basics`：新增时间线章节：`springboot-basics/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.2 `springboot-basics`：重排书籍目录：`springboot-basics/docs/README.md`
- [√] 2.3 `spring-core-beans`：新增时间线章节：`spring-core-beans/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.4 `spring-core-beans`：重排书籍目录：`spring-core-beans/docs/README.md`
- [√] 2.5 `spring-core-aop`：新增时间线章节：`spring-core-aop/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.6 `spring-core-aop`：重排书籍目录：`spring-core-aop/docs/README.md`
- [√] 2.7 `spring-core-tx`：新增时间线章节：`spring-core-tx/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.8 `spring-core-tx`：重排书籍目录：`spring-core-tx/docs/README.md`
- [√] 2.9 `springboot-web-mvc`：新增时间线章节：`springboot-web-mvc/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.10 `springboot-web-mvc`：重排书籍目录：`springboot-web-mvc/docs/README.md`
- [√] 2.11 `spring-core-aop-weaving`：新增时间线章节：`spring-core-aop-weaving/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.12 `spring-core-aop-weaving`：重排书籍目录：`spring-core-aop-weaving/docs/README.md`
- [√] 2.13 `spring-core-events`：新增时间线章节：`spring-core-events/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.14 `spring-core-events`：重排书籍目录：`spring-core-events/docs/README.md`
- [√] 2.15 `spring-core-profiles`：新增时间线章节：`spring-core-profiles/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.16 `spring-core-profiles`：重排书籍目录：`spring-core-profiles/docs/README.md`
- [√] 2.17 `spring-core-resources`：新增时间线章节：`spring-core-resources/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.18 `spring-core-resources`：重排书籍目录：`spring-core-resources/docs/README.md`
- [√] 2.19 `spring-core-validation`：新增时间线章节：`spring-core-validation/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.20 `spring-core-validation`：重排书籍目录：`spring-core-validation/docs/README.md`
- [√] 2.21 `springboot-actuator`：新增时间线章节：`springboot-actuator/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.22 `springboot-actuator`：重排书籍目录：`springboot-actuator/docs/README.md`
- [√] 2.23 `springboot-async-scheduling`：新增时间线章节：`springboot-async-scheduling/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.24 `springboot-async-scheduling`：重排书籍目录：`springboot-async-scheduling/docs/README.md`
- [√] 2.25 `springboot-business-case`：新增时间线章节：`springboot-business-case/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.26 `springboot-business-case`：重排书籍目录：`springboot-business-case/docs/README.md`
- [√] 2.27 `springboot-cache`：新增时间线章节：`springboot-cache/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.28 `springboot-cache`：重排书籍目录：`springboot-cache/docs/README.md`
- [√] 2.29 `springboot-data-jpa`：新增时间线章节：`springboot-data-jpa/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.30 `springboot-data-jpa`：重排书籍目录：`springboot-data-jpa/docs/README.md`
- [√] 2.31 `springboot-security`：新增时间线章节：`springboot-security/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.32 `springboot-security`：重排书籍目录：`springboot-security/docs/README.md`
- [√] 2.33 `springboot-testing`：新增时间线章节：`springboot-testing/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.34 `springboot-testing`：重排书籍目录：`springboot-testing/docs/README.md`
- [√] 2.35 `springboot-web-client`：新增时间线章节：`springboot-web-client/docs/part-00-guide/03-mainline-timeline.md`
- [√] 2.36 `springboot-web-client`：重排书籍目录：`springboot-web-client/docs/README.md`

## 3. 合并/拆章与叙事重写（先做试点，再推广）
- [√] 3.1 试点：重写并合并主线章节（Beans Part01 选 2 章合并为 1 章）：`spring-core-beans/docs/part-01-ioc-container/01-bean-mental-model.md`
- [√] 3.2 试点：保留旧入口 redirect：`spring-core-beans/docs/part-01-ioc-container/02-bean-registration.md`
- [√] 3.3 试点：重写并合并主线章节（Web MVC Internals 选 2 章合并为 1 章）：`springboot-web-mvc/docs/part-03-web-mvc-internals/01-dispatcherservlet-call-chain.md`
- [√] 3.4 试点：保留旧入口 redirect：`springboot-web-mvc/docs/part-03-web-mvc-internals/02-argument-resolver-and-binder.md`

## 4. Security Check
- [√] 4.1 安全自检：确认不引入 secrets/token；确认脚本不包含高风险命令（rm -rf / prod 连接等）

## 5. Knowledge Base Update
- [√] 5.1 更新知识库入口说明：`helloagents/wiki/overview.md`（说明书籍化主线时间线与阅读方式）
- [√] 5.2 更新变更记录：`helloagents/CHANGELOG.md`

## 6. Verification
- [√] 6.1 运行 `bash scripts/check-docs.sh`
- [√] 6.2 运行 `bash scripts/docs-site-build.sh`（strict）
