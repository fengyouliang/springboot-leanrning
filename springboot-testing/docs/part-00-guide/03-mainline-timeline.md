# 主线时间线：Spring Boot Testing

!!! summary
    - 这一模块关注：如何用 slice、mock 与集成测试把 Spring 行为“锁住”，让机制理解可以被验证。
    - 读完你应该能复述：**选择测试切片 → 准备依赖（mock/替身）→ 验证行为 → 定位失败** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → 仅 1 章主线 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`GreetingControllerWebMvcLabTest`

## 在 Spring 主线中的位置

- 测试是“把主线变成可重复实验”的方式：它让你能验证“代理/事务/Web 绑定”等机制是否按预期发生。

## 主线时间线（建议顺读）

1. 选择 slice 与 mocking：把测试范围控制在你想验证的边界上
   - 阅读：[01-slice-and-mocking.md](../part-01-testing/01-slice-and-mocking.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
