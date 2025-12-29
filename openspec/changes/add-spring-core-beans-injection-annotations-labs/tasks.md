## 1. Labs（默认启用，`mvn -q test` 全绿）

- [x] 1.1 新增 `SpringCoreBeansResourceInjectionLabTest`
  - [x] 使用小容器（优先 `GenericApplicationContext` + `AnnotationConfigUtils.registerAnnotationConfigProcessors`）
  - [x] 覆盖至少 2 个可断言现象：
    - [x] 未注册 annotation processors 时：`@Resource` 不生效（依赖为 `null` 或未注入）
    - [x] 注册 processors 后：`@Resource` 默认按字段名/指定 name 进行解析，即使同类型存在多个候选也能稳定注入
  - [x] 输出少量 `OBSERVE:` 提示（不对日志做断言）

- [x] 1.2 新增 `SpringCoreBeansAutowireCandidateSelectionLabTest`
  - [x] 覆盖并固化 3 个最常见结论：
    - [x] `@Order` 影响集合注入顺序，但 **不能** 解决单依赖注入歧义（仍应失败）
    - [x] `@Priority` 可参与单依赖候选选择（无 `@Primary/@Qualifier` 时）
    - [x] `@Primary` 的优先级高于 `@Priority`（同一注入点的选择规则对照）
  - [x] 增加一个集合注入示例（`List<T>` 或 `ObjectProvider<T>.orderedStream()`）来验证顺序语义

- [x] 1.3 新增 `SpringCoreBeansValuePlaceholderResolutionLabTest`
  - [x] 通过 `Environment`/`PropertySource` 注入 property（例如 `MapPropertySource`）形成可控场景
  - [x] 覆盖并固化 2 类行为：
    - [x] 默认 embedded value resolver 解析 `${...}`：存在 property 时能解析；缺失时行为为“非严格”（不强制失败）
    - [x] 注册 `PropertySourcesPlaceholderConfigurer` 后：把行为改为“严格/缺失即失败”（用断言固定）
  - [x] 避免依赖 Boot；只使用 Spring Core 容器能力

## 2. 文档（中文章节，1:1 对应新增 Labs）

- [x] 2.1 新增 `spring-core-beans/docs/` 章节：`@Resource` 注入（name-based resolution）
  - [x] 链接到对应 `*LabTest` 路径
  - [x] 描述可观察现象（what to observe）
  - [x] 解释机制（与 `CommonAnnotationBeanPostProcessor` 的关系）
  - [x] Debug 建议与常见坑

- [x] 2.2 新增章节：候选选择 vs 顺序（`@Primary` / `@Priority` / `@Order`）
  - [x] 给出“单依赖选择规则”与“集合注入排序规则”的对照表
  - [x] 链接到对应 `*LabTest` 与 `docs/03`（DI 解析）形成闭环

- [x] 2.3 新增章节：`@Value` 占位符解析与 strict/non-strict
  - [x] 解释 embedded value resolver 的来源（容器 refresh 阶段）
  - [x] 对照 `PropertySourcesPlaceholderConfigurer`（BFPP）如何改变语义
  - [x] 提供“缺失 property 时为什么没报错/报错”的可解释路径

## 3. README 导航增强（让学习路径更“可跟”）

- [x] 3.1 更新 `spring-core-beans/README.md` 推荐阅读顺序：加入新增章节
- [x] 3.2 更新 `spring-core-beans/README.md` Labs 索引表：加入新增 `*LabTest`
- [x] 3.3 增加一段“按容器阶段/注入机制划分的概念地图”
  - [x] 至少覆盖：DI 解析（docs/03）、注入阶段（docs/30）、`@Resource`、候选选择/排序、`@Value` 占位符解析

## 4. Validation

- [x] 4.1 运行模块测试：`mvn -q -pl spring-core-beans test`
- [ ] 4.2（可选）运行全仓库测试：`mvn -q test`
