# 主线时间线：Spring Boot Actuator

!!! summary
    - 这一模块关注：Actuator 如何把“应用内部状态”以 endpoints 的形式暴露出来（健康检查、指标、信息等）。
    - 读完你应该能复述：**启用 actuator → 配置暴露范围 → 访问 endpoints → 观测与排障** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → 仅 1 章主线 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`BootActuatorLabTest`

## 在 Spring 主线中的位置

- Actuator 是“可观测性入口”：当你要解释系统行为、排查线上问题、做健康探针时，最先想到它。
- 它通常与安全（认证授权）、Web（暴露路径）一起出现，需要边界意识。

## 主线时间线（建议顺读）

1. Actuator 的基本使用与关键配置点
   - 阅读：[01-actuator-basics.md](../part-01-actuator/01-actuator-basics.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
