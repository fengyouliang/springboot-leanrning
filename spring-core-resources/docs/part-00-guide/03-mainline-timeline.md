# 主线时间线：Spring Resources

!!! summary
    - 这一模块关注：Resource 抽象如何统一 classpath/file/jar 等不同资源形态，以及你如何可靠地定位与读取资源。
    - 读完你应该能复述：**定位（路径/模式）→ 解析（Resource）→ 校验（exists/handles）→ 读取（编码/流）** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01 顺读 6 章 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`SpringCoreResourcesLabTest`

## 在 Spring 主线中的位置

- 资源读取贯穿启动期与运行期：配置、模板、静态资源、证书、SQL 脚本都可能走到这里。
- 资源问题常见于“本地可以、线上不行”：根因往往是 classpath/jar 与 filesystem 的差异。

## 主线时间线（建议顺读）

1. 先建立抽象：Resource/ResourceLoader 到底解决什么
   - 阅读：[01. Resource 抽象](../part-01-resource-abstraction/01-resource-abstraction.md)
2. 把 classpath 的定位方式讲清楚（相对路径、前缀、语义差异）
   - 阅读：[02. classpath 定位](../part-01-resource-abstraction/02-classpath-locations.md)
3. 通配与模式：classpath* 与 pattern 的边界
   - 阅读：[03. classpath* 与 pattern](../part-01-resource-abstraction/03-classpath-star-and-pattern.md)
4. exists 与 handles：为什么“exists=true 但读不到/不对”
   - 阅读：[04. exists 与 handles](../part-01-resource-abstraction/04-exists-and-handles.md)
5. 读取与编码：如何避免乱码与流泄露
   - 阅读：[05. 读取与编码](../part-01-resource-abstraction/05-reading-and-encoding.md)
6. jar vs filesystem：真正决定行为差异的地方
   - 阅读：[06. jar vs filesystem](../part-01-resource-abstraction/06-jar-vs-filesystem.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
