# Task List: Spring Boot 模块教学化规范推广（对齐 spring-core 标准）

Directory: `helloagents/plan/202601062024_springboot_modules_teaching_rollout/`

---

## 0. 执行前基线（现状确认）
- [√] 0.1 统计 `springboot-*/docs/README.md` 的“章节 Markdown 链接”解析结果（预计当前多数模块章节数为 0），verify why.md#requirement-docs-index-and-numbering
- [√] 0.2 统计 `springboot-*` 模块 `*LabTest.java` 数量，标识需要补齐到 `min-labs=2` 的模块清单，verify why.md#requirement-minimum-labs-per-module
- [√] 0.3 记录当前 `scripts/check-docs.sh` 的覆盖范围（现状不覆盖 springboot），作为推广前基线，verify why.md#requirement-teaching-coverage-gate

## 1. scripts（自检闸门扩展到 springboot-*）
- [√] 1.1 扩展 `scripts/check-md-relative-links.py` 默认扫描范围：从仅 `spring-core-*/docs` 扩展为 `spring-core-*/docs` + `springboot-*/docs`，并保持可传入 docs 目录/单个 md 文件的能力，verify why.md#requirement-docs-link-integrity
- [√] 1.2 扩展 `scripts/check-teaching-coverage.py` 支持 springboot：扫描所有包含 `docs/README.md` 的模块；以 README 的 Markdown 链接清单为 SSOT；逐章要求“可跑入口”存在；并对所有模块执行 `min-labs=2` 闸门，verify why.md#requirement-teaching-coverage-gate
- [√] 1.3 更新 `scripts/check-docs.sh`：作为全量闸门覆盖 spring-core + springboot（断链检查 + 教学覆盖检查），verify why.md#requirement-teaching-coverage-gate

## 2. springboot-basics（目录页 SSOT + guide/appendix 入口块）
- [√] 2.1 改造 `springboot-basics/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 2.2 补齐 `springboot-basics/docs/part-00-guide/00-deep-dive-guide.md` 的 `### 对应 Lab/Test（可运行）`（至少 1 个 `BootBasics*LabTest` 的真实路径），verify why.md#requirement-chapter-lab-closure
- [√] 2.3 补齐 `springboot-basics/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 2.4 补齐 `springboot-basics/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 2.5 模块自检：`python3 scripts/check-md-relative-links.py springboot-basics/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-basics` 通过，verify why.md#requirement-docs-link-integrity
- [√] 2.6 模块回归：`mvn -pl springboot-basics test`，verify why.md#requirement-chapter-lab-closure

## 3. springboot-web-mvc（目录页 SSOT + guide/appendix 入口块）
- [√] 3.1 改造 `springboot-web-mvc/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 3.2 补齐 `springboot-web-mvc/docs/part-00-guide/00-deep-dive-guide.md` 的 `### 对应 Lab/Test（可运行）`（至少 1 个 `BootWebMvc*LabTest` 的真实路径），verify why.md#requirement-chapter-lab-closure
- [√] 3.3 补齐 `springboot-web-mvc/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 3.4 补齐 `springboot-web-mvc/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 3.5 模块自检：`python3 scripts/check-md-relative-links.py springboot-web-mvc/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-web-mvc` 通过，verify why.md#requirement-docs-link-integrity
- [√] 3.6 模块回归：`mvn -pl springboot-web-mvc test`，verify why.md#requirement-chapter-lab-closure

## 4. springboot-data-jpa（目录页 SSOT + 缺口章节入口 + min-labs=2）
- [√] 4.1 改造 `springboot-data-jpa/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 4.2 补齐 `springboot-data-jpa/docs/part-00-guide/00-deep-dive-guide.md` 的可跑入口块（引用现有 `BootDataJpaLabTest`），verify why.md#requirement-chapter-lab-closure
- [√] 4.3 补齐 `springboot-data-jpa/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 4.4 补齐 `springboot-data-jpa/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 4.5 修复缺口：为 `springboot-data-jpa/docs/part-01-data-jpa/07-debug-sql.md` 增加 `### 对应 Lab/Test（可运行）`，并引用将新增的 debug/trace 相关 Lab，verify why.md#requirement-chapter-lab-closure
- [√] 4.6 新增 1 个 Lab：`springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part01_data_jpa/BootDataJpaDebugSqlLabTest.java`（或等价命名），覆盖“可观测性/SQL 输出/flush 触发点”等可稳定断言场景，使模块 `min-labs=2`，verify why.md#requirement-minimum-labs-per-module
- [√] 4.7 模块自检：`python3 scripts/check-md-relative-links.py springboot-data-jpa/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-data-jpa` 通过，verify why.md#requirement-docs-link-integrity
- [√] 4.8 模块回归：`mvn -pl springboot-data-jpa test`，verify why.md#requirement-chapter-lab-closure

## 5. springboot-actuator（目录页 SSOT + guide/appendix 入口块）
- [√] 5.1 改造 `springboot-actuator/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 5.2 补齐 `springboot-actuator/docs/part-00-guide/00-deep-dive-guide.md` 的可跑入口块（引用现有 `BootActuator*LabTest`），verify why.md#requirement-chapter-lab-closure
- [√] 5.3 补齐 `springboot-actuator/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 5.4 补齐 `springboot-actuator/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 5.5 模块自检：`python3 scripts/check-md-relative-links.py springboot-actuator/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-actuator` 通过，verify why.md#requirement-docs-link-integrity
- [√] 5.6 模块回归：`mvn -pl springboot-actuator test`，verify why.md#requirement-chapter-lab-closure

## 6. springboot-testing（目录页 SSOT + guide/appendix 入口块）
- [√] 6.1 改造 `springboot-testing/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 6.2 补齐 `springboot-testing/docs/part-00-guide/00-deep-dive-guide.md` 的可跑入口块（引用现有 `*LabTest`），verify why.md#requirement-chapter-lab-closure
- [√] 6.3 补齐 `springboot-testing/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 6.4 补齐 `springboot-testing/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 6.5 模块自检：`python3 scripts/check-md-relative-links.py springboot-testing/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-testing` 通过，verify why.md#requirement-docs-link-integrity
- [√] 6.6 模块回归：`mvn -pl springboot-testing test`，verify why.md#requirement-chapter-lab-closure

## 7. springboot-business-case（目录页 SSOT + guide/appendix 入口块 + min-labs=2）
- [√] 7.1 改造 `springboot-business-case/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 7.2 补齐 `springboot-business-case/docs/part-00-guide/00-deep-dive-guide.md` 的可跑入口块（引用现有 `BootBusinessCaseLabTest`），verify why.md#requirement-chapter-lab-closure
- [√] 7.3 补齐 `springboot-business-case/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 7.4 补齐 `springboot-business-case/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 7.5 新增 1 个 Lab：`springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/part01_business_case/BootBusinessCaseServiceLabTest.java`，聚焦 service 层事务 + 事件语义的可断言闭环，使模块 `min-labs=2`，verify why.md#requirement-minimum-labs-per-module
- [√] 7.6 模块自检：`python3 scripts/check-md-relative-links.py springboot-business-case/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-business-case` 通过，verify why.md#requirement-docs-link-integrity
- [√] 7.7 模块回归：`mvn -pl springboot-business-case test`，verify why.md#requirement-chapter-lab-closure

## 8. springboot-security（目录页 SSOT + guide/appendix 入口块 + min-labs=2）
- [√] 8.1 改造 `springboot-security/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 8.2 补齐 `springboot-security/docs/part-00-guide/00-deep-dive-guide.md` 的可跑入口块（引用现有 `BootSecurityLabTest`），verify why.md#requirement-chapter-lab-closure
- [√] 8.3 补齐 `springboot-security/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 8.4 补齐 `springboot-security/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 8.5 新增 1 个 Lab：`springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityDevProfileLabTest.java`，聚焦 dev profile 下的 JWT dev token 端点（可稳定断言），使模块 `min-labs=2`，verify why.md#requirement-minimum-labs-per-module
- [√] 8.6 模块自检：`python3 scripts/check-md-relative-links.py springboot-security/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-security` 通过，verify why.md#requirement-docs-link-integrity
- [√] 8.7 模块回归：`mvn -pl springboot-security test`，verify why.md#requirement-chapter-lab-closure

## 9. springboot-web-client（目录页 SSOT + guide/appendix 入口块）
- [√] 9.1 改造 `springboot-web-client/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 9.2 补齐 `springboot-web-client/docs/part-00-guide/00-deep-dive-guide.md` 的可跑入口块（引用现有 `BootWebClient*LabTest`），verify why.md#requirement-chapter-lab-closure
- [√] 9.3 补齐 `springboot-web-client/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 9.4 补齐 `springboot-web-client/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 9.5 模块自检：`python3 scripts/check-md-relative-links.py springboot-web-client/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-web-client` 通过，verify why.md#requirement-docs-link-integrity
- [√] 9.6 模块回归：`mvn -pl springboot-web-client test`，verify why.md#requirement-chapter-lab-closure

## 10. springboot-async-scheduling（目录页 SSOT + guide/appendix 入口块 + min-labs=2）
- [√] 10.1 改造 `springboot-async-scheduling/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 10.2 补齐 `springboot-async-scheduling/docs/part-00-guide/00-deep-dive-guide.md` 的可跑入口块（引用现有 `BootAsyncSchedulingLabTest`），verify why.md#requirement-chapter-lab-closure
- [√] 10.3 补齐 `springboot-async-scheduling/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 10.4 补齐 `springboot-async-scheduling/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 10.5 新增 1 个 Lab：`springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part01_async_scheduling/BootAsyncSchedulingSchedulingLabTest.java`，聚焦 `@Scheduled` + `@EnableScheduling` 的可断言闭环，使模块 `min-labs=2`，verify why.md#requirement-minimum-labs-per-module
- [√] 10.6 模块自检：`python3 scripts/check-md-relative-links.py springboot-async-scheduling/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-async-scheduling` 通过，verify why.md#requirement-docs-link-integrity
- [√] 10.7 模块回归：`mvn -pl springboot-async-scheduling test`，verify why.md#requirement-chapter-lab-closure

## 11. springboot-cache（目录页 SSOT + guide/appendix 入口块 + min-labs=2）
- [√] 11.1 改造 `springboot-cache/docs/README.md`：将 Start Here/章节清单/Appendix 的路径从反引号改为 Markdown 链接，verify why.md#requirement-docs-index-and-numbering
- [√] 11.2 补齐 `springboot-cache/docs/part-00-guide/00-deep-dive-guide.md` 的可跑入口块（引用现有 `BootCacheLabTest`），verify why.md#requirement-chapter-lab-closure
- [√] 11.3 补齐 `springboot-cache/docs/appendix/90-common-pitfalls.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 11.4 补齐 `springboot-cache/docs/appendix/99-self-check.md` 的可跑入口块，verify why.md#requirement-chapter-lab-closure
- [√] 11.5 新增 1 个 Lab：`springboot-cache/src/test/java/com/learning/springboot/bootcache/part01_cache/BootCacheSpelKeyLabTest.java`，聚焦 SpEL key 的可断言闭环，使模块 `min-labs=2`，verify why.md#requirement-minimum-labs-per-module
- [√] 11.6 模块自检：`python3 scripts/check-md-relative-links.py springboot-cache/docs` + `python3 scripts/check-teaching-coverage.py --min-labs 2 --module springboot-cache` 通过，verify why.md#requirement-docs-link-integrity
- [√] 11.7 模块回归：`mvn -pl springboot-cache test`，verify why.md#requirement-chapter-lab-closure

## 12. 知识库同步（helloagents）
- [√] 12.1 更新 `helloagents/wiki/modules/springboot-*.md` 的 Change History：记录本次推广（目录页 SSOT + 入口块 + Labs 补齐 + 自检闸门），verify why.md#requirement-knowledge-base-sync
- [√] 12.2 更新 `helloagents/CHANGELOG.md` 与 `helloagents/history/index.md`（新增本次方案包条目），verify why.md#requirement-knowledge-base-sync

## 13. Security Check
- [√] 13.1 执行安全自检（G9）：无生产环境操作、无密钥明文、无破坏性命令；新增测试不依赖外部服务；若遇 Maven 403 仅按标准化方式处理且不提交本机缓存，verify why.md#requirement-knowledge-base-sync

## 14. Testing（最终验收）
- [√] 14.1 全量闸门：`bash scripts/check-docs.sh`（覆盖 spring-core + springboot），verify why.md#requirement-teaching-coverage-gate
- [√] 14.2 分模块回归：`mvn -pl springboot-basics test` … `springboot-cache`（全部通过），verify why.md#requirement-chapter-lab-closure

## 15. 方案包归档（强制）
- [√] 15.1 执行完成后：将方案包迁移到 `helloagents/history/YYYY-MM/202601062024_springboot_modules_teaching_rollout/` 并更新 `helloagents/history/index.md`，verify why.md#requirement-knowledge-base-sync
