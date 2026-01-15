# 主线时间线：AOP Weaving（织入：LTW/CTW）

!!! summary
    - 这一模块关注：当“代理”无法覆盖需求时，织入（weaving）如何在类加载期/编译期把横切逻辑写进字节码。
    - 读完你应该能复述：**代理 vs 织入 → 选择 LTW/CTW → 选 Join Point → 验证生效** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → 依次顺读 4 章 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`AspectjLtwLabTest`

## 在 Spring 主线中的位置

- 织入更贴近“字节码层”：它绕开了部分代理的边界（例如 final/构造期等），但引入了工程化复杂度（agent、编译、类加载）。
- 在大多数业务场景，代理足够；只有在需要更强覆盖面时才考虑 weaving。

## 主线时间线（建议顺读）

1. 先明确：代理解决什么、织入解决什么（以及成本）
   - 阅读：[01. 代理 vs 织入](../part-01-mental-model/01-proxy-vs-weaving.md)
2. 选择 LTW（Load-Time Weaving）：类加载期织入怎么落地
   - 阅读：[02. LTW 基础](../part-02-ltw/02-ltw-basics.md)
3. 选择 CTW（Compile-Time Weaving）：编译期织入怎么落地
   - 阅读：[03. CTW 基础](../part-03-ctw/03-ctw-basics.md)
4. 把 Join Point 这本“菜谱”掌握住：知道能织到哪里
   - 阅读：[04. Join Point 菜谱](../part-04-join-points/04-join-point-cookbook.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
