# 第 170 章：90 - Common Pitfalls（springboot-actuator）
<!-- CHAPTER-CARD:START -->
!!! summary "章节学习卡片（五问闭环）"

    - 知识点：Common Pitfalls（springboot-actuator）
    - 怎么使用：建议先跑本章推荐 Lab，把现象固化为断言，再对照正文理解机制；真实项目里常用方式：通过 Actuator endpoints 暴露健康检查/信息/指标；用 exposure 控制可见范围，并在生产环境结合鉴权与安全边界。
    - 原理：引入 Actuator → 端点注册与 discover → exposure 决定暴露 → Web 层映射为 HTTP 端点 → 结合安全策略与可观测信号使用。
    - 源码入口：`org.springframework.boot.actuate.autoconfigure.endpoint.web.WebEndpointAutoConfiguration` / `org.springframework.boot.actuate.endpoint.annotation.Endpoint` / `org.springframework.boot.actuate.autoconfigure.endpoint.web.WebEndpointProperties`
    - 推荐 Lab：`BootActuatorExposureOverrideLabTest`
<!-- CHAPTER-CARD:END -->

<!-- GLOBAL-BOOK-NAV:START -->
上一章：[第 169 章：01 - Actuator 基础与暴露](../part-01-actuator/169-01-actuator-basics.md) ｜ 全书目录：[Book TOC](/book/) ｜ 下一章：[第 171 章：99 - Self Check（springboot-actuator）](171-99-self-check.md)
<!-- GLOBAL-BOOK-NAV:END -->

## 导读

- 本章主题：**90 - Common Pitfalls（springboot-actuator）**
- 阅读方式建议：先看“本章要点”，再沿主线阅读；需要时穿插源码/断点，最后跑通实验闭环。

!!! summary "本章要点"

    - 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
    - 如果只看一眼：请先跑一次本章的最小实验，再回到主线对照阅读。


!!! example "本章配套实验（先跑再读）"

    - Lab：`BootActuatorExposureOverrideLabTest` / `BootActuatorLabTest`

## 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootActuatorExposureOverrideLabTest` / `BootActuatorLabTest`
- 建议命令：`mvn -pl springboot-actuator test`（或在 IDE 直接运行上面的测试类）

## 常见坑与边界


## 常见坑
1. 端点存在但未暴露：只配置了 endpoint，忘了 exposure（或被覆盖）
2. 环境差异：不同 profile/不同配置来源导致“我本地可以，线上不行”
3. 安全边界：暴露端点 ≠ 允许匿名访问

## 对应 Lab（可运行）

- `BootActuatorLabTest`
- `BootActuatorExposureOverrideLabTest`

## 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootActuatorExposureOverrideLabTest` / `BootActuatorLabTest`

上一章：[part-01-actuator/01-actuator-basics.md](../part-01-actuator/169-01-actuator-basics.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/99-self-check.md](171-99-self-check.md)

<!-- BOOKIFY:END -->
