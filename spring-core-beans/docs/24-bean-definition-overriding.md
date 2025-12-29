# 24. BeanDefinition 覆盖（overriding）：同名 bean 是“最后一个赢”还是“直接失败”？

当你注册两个同名 bean 时，会发生什么？

- 有的环境里：**最后一个覆盖前一个**
- 有的环境里：**直接报错**

这不是玄学，是容器的一个开关控制的：

- `DefaultListableBeanFactory#setAllowBeanDefinitionOverriding(...)`

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansBeanDefinitionOverridingLabTest.java`

## 1. allowBeanDefinitionOverriding=true：最后一个 wins

对应测试：

- `SpringCoreBeansBeanDefinitionOverridingLabTest.whenBeanDefinitionOverridingIsAllowed_lastDefinitionWins()`

你会看到：

- 同名 `duplicate` 注册两次
- 最终 `getBean(Marker.class)` 得到的是第二次注册的定义

## 2. allowBeanDefinitionOverriding=false：同名注册 fail-fast

对应测试：

- `SpringCoreBeansBeanDefinitionOverridingLabTest.whenBeanDefinitionOverridingIsDisallowed_registeringSameBeanNameFailsFast()`

你会看到：

- 第二次注册直接抛 `BeanDefinitionOverrideException`
- 甚至还不需要 refresh，注册阶段就失败

## 3. 为什么这个点重要？

因为它会影响你在工程里“怎么理解装配冲突”：

- 如果允许覆盖：你可能会得到“悄悄被覆盖”的行为（难 debug）
- 如果禁止覆盖：你会在启动期得到明确错误（更安全、更可控）

## 4. 常见坑

- **坑 1：把覆盖当成“解决歧义”的手段**
  - 覆盖解决的是“同名冲突”，不是“同类型多实现注入”的歧义。

- **坑 2：不同环境默认值不同**
  - Boot 环境与纯 Spring 容器的默认行为可能不同；不要靠猜。

## 5. 一句话自检

- 你能解释清楚：覆盖开关控制的是“同名 BeanDefinition”冲突，而不是“按类型注入”的选择规则吗？
