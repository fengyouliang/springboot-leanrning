# 03. `classpath*:` 与 pattern：为什么它能“扫到多个资源”？

当你想一次性加载多个资源时，会用到两件事：

- `ResourcePatternResolver`
- `classpath*:` + 通配符（pattern）

## 在本模块如何验证

看 `SpringCoreResourcesMechanicsLabTest#classpathStarPatternLoadsResourcesFromClasspath`

- pattern：`classpath*:data/*.txt`
- 断言能找到 `hello.txt` 与 `info.txt`

看 `SpringCoreResourcesLabTest#patternResultsContainExpectedFilenames`：

- `ResourceReadingService#listResourceLocations(...)` 会返回 `Resource#getDescription()`
- 并排序，保证断言稳定

## 学习建议：避免“顺序不稳定”误判机制

pattern 扫描返回的资源数组顺序不一定稳定（与 classpath 顺序、jar 顺序有关）。

本模块的做法值得复用：

- 把结果映射成可读的 description
- 排序后再断言

## 一句话总结

`classpath*:` 的价值在于：

> 它面向的是“classpath 上的所有匹配资源”，而不是某一个具体位置。

