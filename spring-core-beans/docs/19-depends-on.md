# 19. dependsOn：强制初始化顺序（即使没有显式依赖）

`dependsOn` 是容器提供的一个“强行排序”能力：

- 它解决的是**初始化顺序**问题
- 不是依赖注入（DI）问题

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansDependsOnLabTest.java`

## 1. 现象：两个互不依赖的 bean，也可以有固定初始化顺序

对应测试：

- `SpringCoreBeansDependsOnLabTest.dependsOn_forcesInitializationOrder_evenWithoutDirectDependencies()`

实验里：

- `Second` 并不注入 `First`
- 但 `Second` 的 bean definition 声明了 `dependsOn("first")`

因此容器会：

- 先初始化 `first`
- 再初始化 `second`

## 2. 常见用法（了解即可，别滥用）

你可能会在一些“基础设施”里看到它：

- 需要确保某个初始化逻辑先跑（例如注册某些全局资源）

但一般业务代码不推荐依赖它，因为它会让依赖关系“隐形”。

## 3. 常见坑

- **坑 1：把 dependsOn 当成 DI 手段**
  - dependsOn 不会把 `first` 注入到 `second` 里。

- **坑 2：过度使用导致容器拓扑不透明**
  - 学习阶段可以用它做实验；工程里请谨慎。

## 4. 一句话自检

- 你能解释清楚：dependsOn 解决的是什么问题？（初始化顺序，不是注入）
