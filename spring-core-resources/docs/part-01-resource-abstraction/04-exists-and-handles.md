# 04. `getResource(...)` 的返回值：为什么它会“返回一个不存在的资源句柄”？

很多人第一次看到下面的现象会困惑：

> `resolver.getResource("classpath:data/missing.txt")` 也会返回一个 Resource 对象。

这并不是 bug，这是设计。

## 在本模块如何验证

看 `SpringCoreResourcesMechanicsLabTest#getResourceReturnsAHandle_evenIfTheResourceDoesNotExist`

- `getResource(...)` 返回一个 handle（句柄）
- 你需要用 `resource.exists()` 判断它是否真实存在

## 为什么要这样设计？

因为 Resource 的目标是统一抽象：

- “如何定位资源” 与 “资源是否存在” 是两件事
- 句柄可以携带描述信息，方便 debug（见 [docs/05](05-reading-and-encoding.md)）

## 学习建议

当你需要更友好的错误处理时：

- 先显式 `exists()` 判断
- 再决定抛出什么异常/提示（Exercise 里会让你练）

