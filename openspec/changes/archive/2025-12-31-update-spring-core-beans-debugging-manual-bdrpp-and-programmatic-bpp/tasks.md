## 1. Docs：补齐“调试手册块”（call chain + watch list + 反例）

- [x] 1.1 更新 `spring-core-beans/docs/13-bdrpp-definition-registration.md`
  - [x] 追加 `## 源码最短路径（call chain）`
  - [x] 追加 `## 固定观察点（watch list）`
  - [x] 追加 `## 反例（counterexample）`（必须给最小可跑入口）
  - [x] 强化交叉链接：与 `docs/14`（顺序）、`docs/25`（手工注册绕过机制）、`docs/02`（注册入口）形成可跳转闭环

- [x] 1.2 更新 `spring-core-beans/docs/25-programmatic-bpp-registration.md`
  - [x] 追加 `## 源码最短路径（call chain）`
  - [x] 追加 `## 固定观察点（watch list）`
  - [x] 追加 `## 反例（counterexample）`（复用现有必现用例：programmatic BPP 不按 `Ordered`）
  - [x] 在 watch list 里固定输出“最终顺序来源”：`beanFactory.getBeanPostProcessors()`

## 2. Tests：为 docs/13 的反例补齐最小可跑入口（仅当需要）

- [x] 2.1 （可选）新增 1 个 test method：在 BDRPP/BFPP 阶段调用 `getBean()` 触发过早实例化，断言目标 BPP 未被应用（或应用时机反直觉）
  - [x] 位置：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansRegistryPostProcessorLabTest.java`
  - [x] 要求：默认启用、断言稳定、仅少量 `OBSERVE:` 输出，不对日志做断言

## 3. Validation

- [x] 3.1 运行模块测试：`mvn -q -pl spring-core-beans test`
- [x] 3.2 校验提案：`openspec validate update-spring-core-beans-debugging-manual-bdrpp-and-programmatic-bpp --strict`
