# 00 - Deep Dive Guide（springboot-security）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**00 - Deep Dive Guide（springboot-security）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootSecurityDevProfileLabTest` / `BootSecurityLabTest`
- 建议命令：`mvn -pl springboot-security test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-security test`

## 对应 Lab（可运行）

- `BootSecurityLabTest`
- `BootSecurityDevProfileLabTest`
- `BootSecurityExerciseTest`

## F. 常见坑与边界

## 推荐学习目标
1. 能按“Filter Chain → Authentication → Authorization”讲清主线
2. 能解释 CSRF 的威胁模型与默认行为
3. 能解释方法级安全为何依赖代理，以及常见的自调用绕过陷阱
4. 能解释 JWT 无状态方案的边界：认证与授权分别在哪里发生

## 推荐阅读顺序
1. [01-basic-auth-and-authorization](../part-01-security/01-basic-auth-and-authorization.md)
2. [02-csrf](../part-01-security/02-csrf.md)
3. [04-filter-chain-and-order](../part-01-security/04-filter-chain-and-order.md)
4. [03-method-security-and-proxy](../part-01-security/03-method-security-and-proxy.md)
5. [05-jwt-stateless](../part-01-security/05-jwt-stateless.md)
6. [90-common-pitfalls](../appendix/90-common-pitfalls.md)
7. [99-self-check](../appendix/99-self-check.md)

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootSecurityDevProfileLabTest` / `BootSecurityLabTest`
- Exercise：`BootSecurityExerciseTest`

上一章：[Docs TOC](../README.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-security/01-basic-auth-and-authorization.md](../part-01-security/01-basic-auth-and-authorization.md)

<!-- BOOKIFY:END -->
