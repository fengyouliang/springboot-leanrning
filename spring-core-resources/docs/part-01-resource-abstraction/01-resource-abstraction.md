# 01. `Resource` 抽象：为什么 Spring 不让你直接用 `File`？

Spring 的 `Resource` 抽象解决的是一个常见问题：

> 同样一段读取逻辑，既可能读 classpath 文件，也可能读本地文件，也可能读 URL。

如果你只用 `File`：

- classpath 资源在 jar 包里时根本不是“文件路径”
- 你会在开发环境 OK、打包后崩溃（典型学习陷阱）

## 本模块的最小闭环

`ResourceReadingService` 做了两件事：

- `readClasspathText(location)`：读取单个资源内容
- `listResourceLocations(pattern)`：用 pattern 扫描多个资源并返回 description 列表

对应 tests：

- `SpringCoreResourcesLabTest#readsClasspathResourceContent`
- `SpringCoreResourcesLabTest#loadsMultipleResourcesWithPattern`

## 一句话总结

`Resource` 的学习价值在于：

> 你写的是“读取资源”的逻辑，而不是“读取某种存储形态”的逻辑。

