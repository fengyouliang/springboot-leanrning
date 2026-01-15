# 主线时间线：Spring Profiles

!!! summary
    - 这一模块关注：Profile 如何影响 Bean 的装配选择，以及它与配置源/环境变量的配合方式。
    - 读完你应该能复述：**激活 profiles → 条件匹配 → Bean 是否注册** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → 仅 1 章主线 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`SpringCoreProfilesLabTest`

## 在 Spring 主线中的位置

- Profile 是“选择器”：它决定哪一组 Bean 定义会进入容器。
- 当你遇到“本地/测试/生产行为不一致”，优先回到这里确认 profiles 的激活与匹配。

## 主线时间线（建议顺读）

1. Profile 的激活方式与 Bean 选择规则
   - 阅读：[01-profile-activation-and-bean-selection.md](../part-01-profiles/01-profile-activation-and-bean-selection.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
