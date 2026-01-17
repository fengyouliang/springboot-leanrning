# Labs 索引（可跑入口）
<!-- CHAPTER-CARD:START -->
!!! summary "章节学习卡片（五问闭环）"

    - 知识点：Labs 索引（可跑入口）
    - 怎么使用：本页为索引/工具页：按页面提示找到入口（章节/Lab/断点地图），再回到主线章节顺读。
    - 原理：本页不讲机制原理，负责把“入口与路径”整理成可检索的导航。
    - 源码入口：N/A（本页为索引/工具页）
    - 推荐 Lab：N/A
<!-- CHAPTER-CARD:END -->


> 本页由 `scripts/generate-book-labs-index.py` 生成。新增/移动 `*LabTest.java` 后请重新生成。

## 小结与下一章

<!-- BOOKLIKE-V2:SUMMARY:START -->
- 一句话总结：Labs 索引（可跑入口） —— 本页为索引/工具页：按页面提示找到入口（章节/Lab/断点地图），再回到主线章节顺读。
- 回到主线：本页不讲机制原理，负责把“入口与路径”整理成可检索的导航。
- 下一章：建议按模块目录/全书目录继续顺读。
<!-- BOOKLIKE-V2:SUMMARY:END -->

## 怎么用这页

<!-- BOOKLIKE-V2:INTRO:START -->
这一章围绕「Labs 索引（可跑入口）」展开：先把边界说清楚，再沿主线推进到关键分支，最后用可运行入口把结论验证出来。

阅读建议：
- 先看章首的“章节学习卡片/本章要点”，建立预期；
- 建议先带着问题顺读一遍正文，再按证据链回到源码/断点验证。
<!-- BOOKLIKE-V2:INTRO:END -->

## 运行方式速记

- 全仓库：`mvn -q test`
- 单模块：`mvn -q -pl <module> test`
- 单类：`mvn -q -pl <module> -Dtest=<SomeLabTest> test`

## 按模块

### springboot-basics

- 数量：3
- 模块 docs：[`springboot-basics/docs/README.md`](../springboot-basics/docs/README.md)

- [`BootBasicsDefaultLabTest`](../springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDefaultLabTest.java)
  - 运行：`mvn -q -pl springboot-basics -Dtest=BootBasicsDefaultLabTest test`
- [`BootBasicsDevLabTest`](../springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDevLabTest.java)
  - 运行：`mvn -q -pl springboot-basics -Dtest=BootBasicsDevLabTest test`
- [`BootBasicsOverrideLabTest`](../springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsOverrideLabTest.java)
  - 运行：`mvn -q -pl springboot-basics -Dtest=BootBasicsOverrideLabTest test`

### spring-core-beans

- 数量：68
- 模块 docs：[`spring-core-beans/docs/README.md`](../spring-core-beans/docs/README.md)

- [`SpringCoreBeansGenericTypeMatchingPitfallsLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/appendix/SpringCoreBeansGenericTypeMatchingPitfallsLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansGenericTypeMatchingPitfallsLabTest test`
- [`SpringCoreBeansLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part00_guide/SpringCoreBeansLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansLabTest test`
- [`SpringCoreBeansBeanFactoryVsApplicationContextLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansBeanFactoryVsApplicationContextLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBeanFactoryVsApplicationContextLabTest test`
- [`SpringCoreBeansBeanGraphDebugLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansBeanGraphDebugLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBeanGraphDebugLabTest test`
- [`SpringCoreBeansComponentScanLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansComponentScanLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansComponentScanLabTest test`
- [`SpringCoreBeansContainerLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansContainerLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansContainerLabTest test`
- [`SpringCoreBeansImportLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansImportLabTest test`
- [`SpringCoreBeansAutoConfigurationBackoffTimingLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part02_boot_autoconfig/SpringCoreBeansAutoConfigurationBackoffTimingLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAutoConfigurationBackoffTimingLabTest test`
- [`SpringCoreBeansAutoConfigurationImportOrderingLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part02_boot_autoconfig/SpringCoreBeansAutoConfigurationImportOrderingLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAutoConfigurationImportOrderingLabTest test`
- [`SpringCoreBeansAutoConfigurationLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part02_boot_autoconfig/SpringCoreBeansAutoConfigurationLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAutoConfigurationLabTest test`
- [`SpringCoreBeansAutoConfigurationOrderingLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part02_boot_autoconfig/SpringCoreBeansAutoConfigurationOrderingLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAutoConfigurationOrderingLabTest test`
- [`SpringCoreBeansAutoConfigurationOverrideMatrixLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part02_boot_autoconfig/SpringCoreBeansAutoConfigurationOverrideMatrixLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAutoConfigurationOverrideMatrixLabTest test`
- [`SpringCoreBeansBeanDefinitionOriginLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part02_boot_autoconfig/SpringCoreBeansBeanDefinitionOriginLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBeanDefinitionOriginLabTest test`
- [`SpringCoreBeansConditionEvaluationReportLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part02_boot_autoconfig/SpringCoreBeansConditionEvaluationReportLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansConditionEvaluationReportLabTest test`
- [`SpringCoreBeansExceptionNavigationLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part02_boot_autoconfig/SpringCoreBeansExceptionNavigationLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansExceptionNavigationLabTest test`
- [`SpringCoreBeansProfileRegistrationLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part02_boot_autoconfig/SpringCoreBeansProfileRegistrationLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansProfileRegistrationLabTest test`
- [`SpringCoreBeansAwareInfrastructureLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansAwareInfrastructureLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAwareInfrastructureLabTest test`
- [`SpringCoreBeansBeanCreationTraceLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBeanCreationTraceLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBeanCreationTraceLabTest test`
- [`SpringCoreBeansBootstrapInternalsLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBootstrapInternalsLabTest test`
- [`SpringCoreBeansCircularDependencyBoundaryLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansCircularDependencyBoundaryLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansCircularDependencyBoundaryLabTest test`
- [`SpringCoreBeansEarlyReferenceLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansEarlyReferenceLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansEarlyReferenceLabTest test`
- [`SpringCoreBeansLifecycleCallbackOrderLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansLifecycleCallbackOrderLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansLifecycleCallbackOrderLabTest test`
- [`SpringCoreBeansPostProcessorOrderingLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansPostProcessorOrderingLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansPostProcessorOrderingLabTest test`
- [`SpringCoreBeansPreInstantiationLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansPreInstantiationLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansPreInstantiationLabTest test`
- [`SpringCoreBeansPrototypeDestroySemanticsLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansPrototypeDestroySemanticsLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansPrototypeDestroySemanticsLabTest test`
- [`SpringCoreBeansRawInjectionDespiteWrappingLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansRawInjectionDespiteWrappingLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansRawInjectionDespiteWrappingLabTest test`
- [`SpringCoreBeansRegistryPostProcessorLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansRegistryPostProcessorLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansRegistryPostProcessorLabTest test`
- [`SpringCoreBeansStaticBeanFactoryPostProcessorLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansStaticBeanFactoryPostProcessorLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansStaticBeanFactoryPostProcessorLabTest test`
- [`SpringCoreBeansAutowireCandidateSelectionLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansAutowireCandidateSelectionLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAutowireCandidateSelectionLabTest test`
- [`SpringCoreBeansBeanDefinitionOverridingLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansBeanDefinitionOverridingLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBeanDefinitionOverridingLabTest test`
- [`SpringCoreBeansBeanFactoryApiLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansBeanFactoryApiLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBeanFactoryApiLabTest test`
- [`SpringCoreBeansBeanNameAliasLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansBeanNameAliasLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBeanNameAliasLabTest test`
- [`SpringCoreBeansBeansSupportUtilitiesLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansBeansSupportUtilitiesLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBeansSupportUtilitiesLabTest test`
- [`SpringCoreBeansContextHierarchyLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansContextHierarchyLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansContextHierarchyLabTest test`
- [`SpringCoreBeansCustomScopeLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansCustomScopeLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansCustomScopeLabTest test`
- [`SpringCoreBeansDependsOnLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansDependsOnLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansDependsOnLabTest test`
- [`SpringCoreBeansEnvironmentPropertySourceLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansEnvironmentPropertySourceLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansEnvironmentPropertySourceLabTest test`
- [`SpringCoreBeansFactoryBeanDeepDiveLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansFactoryBeanDeepDiveLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansFactoryBeanDeepDiveLabTest test`
- [`SpringCoreBeansFactoryBeanEdgeCasesLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansFactoryBeanEdgeCasesLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansFactoryBeanEdgeCasesLabTest test`
- [`SpringCoreBeansInjectionAmbiguityLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansInjectionAmbiguityLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansInjectionAmbiguityLabTest test`
- [`SpringCoreBeansInjectionPhaseLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansInjectionPhaseLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansInjectionPhaseLabTest test`
- [`SpringCoreBeansJsr330InjectionLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansJsr330InjectionLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansJsr330InjectionLabTest test`
- [`SpringCoreBeansLazyLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansLazyLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansLazyLabTest test`
- [`SpringCoreBeansMergedBeanDefinitionLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansMergedBeanDefinitionLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansMergedBeanDefinitionLabTest test`
- [`SpringCoreBeansOptionalInjectionLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansOptionalInjectionLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansOptionalInjectionLabTest test`
- [`SpringCoreBeansProgrammaticBeanPostProcessorLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansProgrammaticBeanPostProcessorLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansProgrammaticBeanPostProcessorLabTest test`
- [`SpringCoreBeansProgrammaticRegistrationLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansProgrammaticRegistrationLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansProgrammaticRegistrationLabTest test`
- [`SpringCoreBeansProxyingPhaseLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansProxyingPhaseLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansProxyingPhaseLabTest test`
- [`SpringCoreBeansResolvableDependencyLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansResolvableDependencyLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansResolvableDependencyLabTest test`
- [`SpringCoreBeansResourceInjectionLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansResourceInjectionLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansResourceInjectionLabTest test`
- [`SpringCoreBeansSmartInitializingSingletonLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansSmartInitializingSingletonLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansSmartInitializingSingletonLabTest test`
- [`SpringCoreBeansSmartLifecycleLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansSmartLifecycleLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansSmartLifecycleLabTest test`
- [`SpringCoreBeansTypeConversionLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansTypeConversionLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansTypeConversionLabTest test`
- [`SpringCoreBeansValuePlaceholderResolutionLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansValuePlaceholderResolutionLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansValuePlaceholderResolutionLabTest test`
- [`SpringCoreBeansAotFactoriesLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansAotFactoriesLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAotFactoriesLabTest test`
- [`SpringCoreBeansAotRuntimeHintsLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansAotRuntimeHintsLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAotRuntimeHintsLabTest test`
- [`SpringCoreBeansAutowireCapableBeanFactoryLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansAutowireCapableBeanFactoryLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAutowireCapableBeanFactoryLabTest test`
- [`SpringCoreBeansBeanDefinitionValueResolutionLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansBeanDefinitionValueResolutionLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBeanDefinitionValueResolutionLabTest test`
- [`SpringCoreBeansBuiltInFactoryBeansLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansBuiltInFactoryBeansLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansBuiltInFactoryBeansLabTest test`
- [`SpringCoreBeansCustomQualifierLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansCustomQualifierLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansCustomQualifierLabTest test`
- [`SpringCoreBeansGroovyBeanDefinitionReaderLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansGroovyBeanDefinitionReaderLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansGroovyBeanDefinitionReaderLabTest test`
- [`SpringCoreBeansPropertiesBeanDefinitionReaderLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansPropertiesBeanDefinitionReaderLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansPropertiesBeanDefinitionReaderLabTest test`
- [`SpringCoreBeansPropertyEditorLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansPropertyEditorLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansPropertyEditorLabTest test`
- [`SpringCoreBeansReplacedMethodLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansReplacedMethodLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansReplacedMethodLabTest test`
- [`SpringCoreBeansServiceLoaderFactoryBeansLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansServiceLoaderFactoryBeansLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansServiceLoaderFactoryBeansLabTest test`
- [`SpringCoreBeansSpelValueLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansSpelValueLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansSpelValueLabTest test`
- [`SpringCoreBeansXmlBeanDefinitionReaderLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansXmlBeanDefinitionReaderLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansXmlBeanDefinitionReaderLabTest test`
- [`SpringCoreBeansXmlNamespaceExtensionLabTest`](../spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansXmlNamespaceExtensionLabTest.java)
  - 运行：`mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansXmlNamespaceExtensionLabTest test`

### spring-core-aop

- 数量：8
- 模块 docs：[`spring-core-aop/docs/README.md`](../spring-core-aop/docs/README.md)

- [`SpringCoreAopExposeProxyLabTest`](../spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part01_proxy_fundamentals/SpringCoreAopExposeProxyLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop -Dtest=SpringCoreAopExposeProxyLabTest test`
- [`SpringCoreAopLabTest`](../spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part01_proxy_fundamentals/SpringCoreAopLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop -Dtest=SpringCoreAopLabTest test`
- [`SpringCoreAopProxyMechanicsLabTest`](../spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part01_proxy_fundamentals/SpringCoreAopProxyMechanicsLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop -Dtest=SpringCoreAopProxyMechanicsLabTest test`
- [`SpringCoreAopAutoProxyCreatorInternalsLabTest`](../spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part02_autoproxy_and_pointcuts/SpringCoreAopAutoProxyCreatorInternalsLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop -Dtest=SpringCoreAopAutoProxyCreatorInternalsLabTest test`
- [`SpringCoreAopPointcutExpressionsLabTest`](../spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part02_autoproxy_and_pointcuts/SpringCoreAopPointcutExpressionsLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop -Dtest=SpringCoreAopPointcutExpressionsLabTest test`
- [`SpringCoreAopMultiProxyStackingLabTest`](../spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part03_proxy_stacking/SpringCoreAopMultiProxyStackingLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop -Dtest=SpringCoreAopMultiProxyStackingLabTest test`
- [`SpringCoreAopProceedNestingLabTest`](../spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part03_proxy_stacking/SpringCoreAopProceedNestingLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop -Dtest=SpringCoreAopProceedNestingLabTest test`
- [`SpringCoreAopRealWorldStackingLabTest`](../spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/part03_proxy_stacking/SpringCoreAopRealWorldStackingLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop -Dtest=SpringCoreAopRealWorldStackingLabTest test`

### spring-core-aop-weaving

- 数量：2
- 模块 docs：[`spring-core-aop-weaving/docs/README.md`](../spring-core-aop-weaving/docs/README.md)

- [`AspectjLtwLabTest`](../spring-core-aop-weaving/src/test/java/com/learning/springboot/springcoreaopweaving/part02_ltw_fundamentals/AspectjLtwLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop-weaving -Dtest=AspectjLtwLabTest test`
- [`AspectjCtwLabTest`](../spring-core-aop-weaving/src/test/java/com/learning/springboot/springcoreaopweaving/part03_ctw_fundamentals/AspectjCtwLabTest.java)
  - 运行：`mvn -q -pl spring-core-aop-weaving -Dtest=AspectjCtwLabTest test`

### spring-core-tx

- 数量：4
- 模块 docs：[`spring-core-tx/docs/README.md`](../spring-core-tx/docs/README.md)

- [`SpringCoreTxSelfInvocationPitfallLabTest`](../spring-core-tx/src/test/java/com/learning/springboot/springcoretx/appendix/SpringCoreTxSelfInvocationPitfallLabTest.java)
  - 运行：`mvn -q -pl spring-core-tx -Dtest=SpringCoreTxSelfInvocationPitfallLabTest test`
- [`SpringCoreTxLabTest`](../spring-core-tx/src/test/java/com/learning/springboot/springcoretx/part01_transaction_basics/SpringCoreTxLabTest.java)
  - 运行：`mvn -q -pl spring-core-tx -Dtest=SpringCoreTxLabTest test`
- [`SpringCoreTxPropagationMatrixLabTest`](../spring-core-tx/src/test/java/com/learning/springboot/springcoretx/part01_transaction_basics/SpringCoreTxPropagationMatrixLabTest.java)
  - 运行：`mvn -q -pl spring-core-tx -Dtest=SpringCoreTxPropagationMatrixLabTest test`
- [`SpringCoreTxRollbackRulesLabTest`](../spring-core-tx/src/test/java/com/learning/springboot/springcoretx/part01_transaction_basics/SpringCoreTxRollbackRulesLabTest.java)
  - 运行：`mvn -q -pl spring-core-tx -Dtest=SpringCoreTxRollbackRulesLabTest test`

### springboot-web-mvc

- 数量：20
- 模块 docs：[`springboot-web-mvc/docs/README.md`](../springboot-web-mvc/docs/README.md)

- [`BootWebMvcBindingDeepDiveLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcBindingDeepDiveLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcBindingDeepDiveLabTest test`
- [`BootWebMvcLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcLabTest test`
- [`BootWebMvcSpringBootLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcSpringBootLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcSpringBootLabTest test`
- [`BootWebMvcErrorViewLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcErrorViewLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcErrorViewLabTest test`
- [`BootWebMvcViewLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcViewLabTest test`
- [`BootWebMvcViewSpringBootLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewSpringBootLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcViewSpringBootLabTest test`
- [`BootWebMvcExceptionResolverChainLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcExceptionResolverChainLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcExceptionResolverChainLabTest test`
- [`BootWebMvcInternalsLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcInternalsLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcInternalsLabTest test`
- [`BootWebMvcMessageConverterTraceLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcMessageConverterTraceLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcMessageConverterTraceLabTest test`
- [`BootWebMvcTraceLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part03_internals/BootWebMvcTraceLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcTraceLabTest test`
- [`BootWebMvcContractJacksonLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part04_contract/BootWebMvcContractJacksonLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcContractJacksonLabTest test`
- [`BootWebMvcProblemDetailLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part04_contract/BootWebMvcProblemDetailLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcProblemDetailLabTest test`
- [`BootWebMvcRealWorldHttpLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part05_real_world/BootWebMvcRealWorldHttpLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcRealWorldHttpLabTest test`
- [`BootWebMvcAsyncSseLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part06_async_sse/BootWebMvcAsyncSseLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcAsyncSseLabTest test`
- [`BootWebMvcTestingDebuggingLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part07_testing/BootWebMvcTestingDebuggingLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcTestingDebuggingLabTest test`
- [`BootWebMvcObservabilityLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part08_security_observability/BootWebMvcObservabilityLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcObservabilityLabTest test`
- [`BootWebMvcSecurityLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part08_security_observability/BootWebMvcSecurityLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcSecurityLabTest test`
- [`BootWebMvcSecurityVsMvcExceptionBoundaryLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part08_security_observability/BootWebMvcSecurityVsMvcExceptionBoundaryLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcSecurityVsMvcExceptionBoundaryLabTest test`
- [`BootWebMvcAdviceOrderLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part09_advice_order/BootWebMvcAdviceOrderLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcAdviceOrderLabTest test`
- [`BootWebMvcAdviceMatchingLabTest`](../springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part10_advice_matching/BootWebMvcAdviceMatchingLabTest.java)
  - 运行：`mvn -q -pl springboot-web-mvc -Dtest=BootWebMvcAdviceMatchingLabTest test`

### springboot-security

- 数量：3
- 模块 docs：[`springboot-security/docs/README.md`](../springboot-security/docs/README.md)

- [`BootSecurityDevProfileLabTest`](../springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityDevProfileLabTest.java)
  - 运行：`mvn -q -pl springboot-security -Dtest=BootSecurityDevProfileLabTest test`
- [`BootSecurityLabTest`](../springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityLabTest.java)
  - 运行：`mvn -q -pl springboot-security -Dtest=BootSecurityLabTest test`
- [`BootSecurityMultiFilterChainOrderLabTest`](../springboot-security/src/test/java/com/learning/springboot/bootsecurity/part01_security/BootSecurityMultiFilterChainOrderLabTest.java)
  - 运行：`mvn -q -pl springboot-security -Dtest=BootSecurityMultiFilterChainOrderLabTest test`

### springboot-data-jpa

- 数量：3
- 模块 docs：[`springboot-data-jpa/docs/README.md`](../springboot-data-jpa/docs/README.md)

- [`BootDataJpaDebugSqlLabTest`](../springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part01_data_jpa/BootDataJpaDebugSqlLabTest.java)
  - 运行：`mvn -q -pl springboot-data-jpa -Dtest=BootDataJpaDebugSqlLabTest test`
- [`BootDataJpaLabTest`](../springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part01_data_jpa/BootDataJpaLabTest.java)
  - 运行：`mvn -q -pl springboot-data-jpa -Dtest=BootDataJpaLabTest test`
- [`BootDataJpaMergeAndDetachLabTest`](../springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part01_data_jpa/BootDataJpaMergeAndDetachLabTest.java)
  - 运行：`mvn -q -pl springboot-data-jpa -Dtest=BootDataJpaMergeAndDetachLabTest test`

### springboot-cache

- 数量：2
- 模块 docs：[`springboot-cache/docs/README.md`](../springboot-cache/docs/README.md)

- [`BootCacheLabTest`](../springboot-cache/src/test/java/com/learning/springboot/bootcache/part01_cache/BootCacheLabTest.java)
  - 运行：`mvn -q -pl springboot-cache -Dtest=BootCacheLabTest test`
- [`BootCacheSpelKeyLabTest`](../springboot-cache/src/test/java/com/learning/springboot/bootcache/part01_cache/BootCacheSpelKeyLabTest.java)
  - 运行：`mvn -q -pl springboot-cache -Dtest=BootCacheSpelKeyLabTest test`

### springboot-async-scheduling

- 数量：2
- 模块 docs：[`springboot-async-scheduling/docs/README.md`](../springboot-async-scheduling/docs/README.md)

- [`BootAsyncSchedulingLabTest`](../springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part01_async_scheduling/BootAsyncSchedulingLabTest.java)
  - 运行：`mvn -q -pl springboot-async-scheduling -Dtest=BootAsyncSchedulingLabTest test`
- [`BootAsyncSchedulingSchedulingLabTest`](../springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part01_async_scheduling/BootAsyncSchedulingSchedulingLabTest.java)
  - 运行：`mvn -q -pl springboot-async-scheduling -Dtest=BootAsyncSchedulingSchedulingLabTest test`

### spring-core-events

- 数量：5
- 模块 docs：[`spring-core-events/docs/README.md`](../spring-core-events/docs/README.md)

- [`SpringCoreEventsLabTest`](../spring-core-events/src/test/java/com/learning/springboot/springcoreevents/part01_event_basics/SpringCoreEventsLabTest.java)
  - 运行：`mvn -q -pl spring-core-events -Dtest=SpringCoreEventsLabTest test`
- [`SpringCoreEventsListenerFilteringLabTest`](../spring-core-events/src/test/java/com/learning/springboot/springcoreevents/part01_event_basics/SpringCoreEventsListenerFilteringLabTest.java)
  - 运行：`mvn -q -pl spring-core-events -Dtest=SpringCoreEventsListenerFilteringLabTest test`
- [`SpringCoreEventsMechanicsLabTest`](../spring-core-events/src/test/java/com/learning/springboot/springcoreevents/part01_event_basics/SpringCoreEventsMechanicsLabTest.java)
  - 运行：`mvn -q -pl spring-core-events -Dtest=SpringCoreEventsMechanicsLabTest test`
- [`SpringCoreEventsAsyncMulticasterLabTest`](../spring-core-events/src/test/java/com/learning/springboot/springcoreevents/part02_async_and_transactional/SpringCoreEventsAsyncMulticasterLabTest.java)
  - 运行：`mvn -q -pl spring-core-events -Dtest=SpringCoreEventsAsyncMulticasterLabTest test`
- [`SpringCoreEventsTransactionalEventLabTest`](../spring-core-events/src/test/java/com/learning/springboot/springcoreevents/part02_async_and_transactional/SpringCoreEventsTransactionalEventLabTest.java)
  - 运行：`mvn -q -pl spring-core-events -Dtest=SpringCoreEventsTransactionalEventLabTest test`

### spring-core-resources

- 数量：2
- 模块 docs：[`spring-core-resources/docs/README.md`](../spring-core-resources/docs/README.md)

- [`SpringCoreResourcesLabTest`](../spring-core-resources/src/test/java/com/learning/springboot/springcoreresources/part01_resource_abstraction/SpringCoreResourcesLabTest.java)
  - 运行：`mvn -q -pl spring-core-resources -Dtest=SpringCoreResourcesLabTest test`
- [`SpringCoreResourcesMechanicsLabTest`](../spring-core-resources/src/test/java/com/learning/springboot/springcoreresources/part01_resource_abstraction/SpringCoreResourcesMechanicsLabTest.java)
  - 运行：`mvn -q -pl spring-core-resources -Dtest=SpringCoreResourcesMechanicsLabTest test`

### spring-core-profiles

- 数量：2
- 模块 docs：[`spring-core-profiles/docs/README.md`](../spring-core-profiles/docs/README.md)

- [`SpringCoreProfilesLabTest`](../spring-core-profiles/src/test/java/com/learning/springboot/springcoreprofiles/part01_profiles/SpringCoreProfilesLabTest.java)
  - 运行：`mvn -q -pl spring-core-profiles -Dtest=SpringCoreProfilesLabTest test`
- [`SpringCoreProfilesProfilePrecedenceLabTest`](../spring-core-profiles/src/test/java/com/learning/springboot/springcoreprofiles/part01_profiles/SpringCoreProfilesProfilePrecedenceLabTest.java)
  - 运行：`mvn -q -pl spring-core-profiles -Dtest=SpringCoreProfilesProfilePrecedenceLabTest test`

### spring-core-validation

- 数量：2
- 模块 docs：[`spring-core-validation/docs/README.md`](../spring-core-validation/docs/README.md)

- [`SpringCoreValidationLabTest`](../spring-core-validation/src/test/java/com/learning/springboot/springcorevalidation/part01_validation_core/SpringCoreValidationLabTest.java)
  - 运行：`mvn -q -pl spring-core-validation -Dtest=SpringCoreValidationLabTest test`
- [`SpringCoreValidationMechanicsLabTest`](../spring-core-validation/src/test/java/com/learning/springboot/springcorevalidation/part01_validation_core/SpringCoreValidationMechanicsLabTest.java)
  - 运行：`mvn -q -pl spring-core-validation -Dtest=SpringCoreValidationMechanicsLabTest test`

### springboot-actuator

- 数量：2
- 模块 docs：[`springboot-actuator/docs/README.md`](../springboot-actuator/docs/README.md)

- [`BootActuatorExposureOverrideLabTest`](../springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part01_actuator/BootActuatorExposureOverrideLabTest.java)
  - 运行：`mvn -q -pl springboot-actuator -Dtest=BootActuatorExposureOverrideLabTest test`
- [`BootActuatorLabTest`](../springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part01_actuator/BootActuatorLabTest.java)
  - 运行：`mvn -q -pl springboot-actuator -Dtest=BootActuatorLabTest test`

### springboot-web-client

- 数量：3
- 模块 docs：[`springboot-web-client/docs/README.md`](../springboot-web-client/docs/README.md)

- [`BootWebClientRestClientLabTest`](../springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientRestClientLabTest.java)
  - 运行：`mvn -q -pl springboot-web-client -Dtest=BootWebClientRestClientLabTest test`
- [`BootWebClientWebClientFilterOrderLabTest`](../springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientWebClientFilterOrderLabTest.java)
  - 运行：`mvn -q -pl springboot-web-client -Dtest=BootWebClientWebClientFilterOrderLabTest test`
- [`BootWebClientWebClientLabTest`](../springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientWebClientLabTest.java)
  - 运行：`mvn -q -pl springboot-web-client -Dtest=BootWebClientWebClientLabTest test`

### springboot-testing

- 数量：3
- 模块 docs：[`springboot-testing/docs/README.md`](../springboot-testing/docs/README.md)

- [`BootTestingMockBeanLabTest`](../springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/BootTestingMockBeanLabTest.java)
  - 运行：`mvn -q -pl springboot-testing -Dtest=BootTestingMockBeanLabTest test`
- [`GreetingControllerSpringBootLabTest`](../springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerSpringBootLabTest.java)
  - 运行：`mvn -q -pl springboot-testing -Dtest=GreetingControllerSpringBootLabTest test`
- [`GreetingControllerWebMvcLabTest`](../springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerWebMvcLabTest.java)
  - 运行：`mvn -q -pl springboot-testing -Dtest=GreetingControllerWebMvcLabTest test`

### springboot-business-case

- 数量：2
- 模块 docs：[`springboot-business-case/docs/README.md`](../springboot-business-case/docs/README.md)

- [`BootBusinessCaseLabTest`](../springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/part01_business_case/BootBusinessCaseLabTest.java)
  - 运行：`mvn -q -pl springboot-business-case -Dtest=BootBusinessCaseLabTest test`
- [`BootBusinessCaseServiceLabTest`](../springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/part01_business_case/BootBusinessCaseServiceLabTest.java)
  - 运行：`mvn -q -pl springboot-business-case -Dtest=BootBusinessCaseServiceLabTest test`
