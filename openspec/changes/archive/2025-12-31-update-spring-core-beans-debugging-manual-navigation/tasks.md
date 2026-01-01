## 1. Docs：为关键章节补齐“调试手册块”

- [x] 1.1 更新 `spring-core-beans/docs/03-dependency-injection-resolution.md`
  - [x] 增量补齐三段固定结构：`call chain` / `watch list` / `反例`
  - [x] 把 `doResolveDependency` 的收敛规则写成“调试手册”（从断点如何收敛到结论）
  - [x] 强化与 `docs/33`、`docs/20` 的交叉链接（候选收敛 vs resolvableDependencies）

- [x] 1.2 更新 `spring-core-beans/docs/19-depends-on.md`
  - [x] 写透 `dependentBeanMap` / `dependenciesForBeanMap` 的记录机制（dependsOn + 真实注入依赖）
  - [x] 写透销毁顺序与依赖关系表的关系（先销毁 dependent 再销毁 dependency）
  - [x] 保留并兼容既有三段模板标题（源码锚点/断点闭环/排障分流），在此基础上追加“调试手册块”

- [x] 1.3 更新 `spring-core-beans/docs/35-merged-bean-definition.md`
  - [x] 补一段“merged 在 createBean 链路中的精确位置”（到 `applyMergedBeanDefinitionPostProcessors` 的位置）
  - [x] 增量补齐三段固定结构：`call chain` / `watch list` / `反例`

## 2. Docs：扩充异常导航表（报错即导航）

- [x] 2.1 更新 `spring-core-beans/docs/11-debugging-and-observability.md` 的“异常 → 断点入口”表
  - [x] 新增：`NoUniqueBeanDefinitionException` / `BeanCreationException` / `BeanDefinitionStoreException`
  - [x] 为表中每条异常补齐“最小可跑 Lab/Test”入口（尽量精确到方法）

## 3. Tests：补齐异常最小复现入口（仅当缺失）

- [x] 3.1 新增最小 `UnsatisfiedDependencyException` 复现用例（启用，断言异常类型稳定）
- [x] 3.2 新增最小 `BeanDefinitionStoreException` 复现用例（启用，断言异常类型稳定）

## 4. Validation

- [x] 4.1 运行模块测试：`mvn -q -pl spring-core-beans test`
- [x] 4.2 重新校验提案：`openspec validate update-spring-core-beans-debugging-manual-navigation --strict`
