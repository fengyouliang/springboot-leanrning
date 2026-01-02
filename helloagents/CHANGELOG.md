# Changelog

本文件记录本仓库的重要变更，格式参考 Keep a Changelog，版本号遵循语义化版本（SemVer）。

## [Unreleased]

### Changed
- `spring-core-beans`：补齐模块 README 学习路线（Start Here/入门→进阶→深挖/refresh 主线一页纸/运行态观察点），新增“注入歧义最小复现”Lab + 对应 Exercise，并增强 `BeansDemoRunner` 的 `BEANS:` 结构化输出；同时同步根 README 与 progress 打卡入口。
- `spring-core-beans`：把“新增面试点”按主题嵌入到 docs/01、03、05、16、31、33 的正文对应小节，并补齐可断言复现入口（新增 BeanFactory vs ApplicationContext / Aware 基础设施 / 泛型匹配坑 Labs；扩展 proxy 章节增加 CGLIB vs JDK 对照与 BPP 定位闭环）。
- `spring-core-beans`：深化 Boot 自动装配章节（docs/10）：补齐 `matchIfMissing` 三态语义与自动配置顺序依赖（after/before）最小复现 Lab，并在 docs/11 与 README 的索引表同步入口。
- 深化 `spring-core-beans` 核心章节：扩写 docs/03、05、06、07、08、09、16、17、23、29、31，并扩展 docs/90（常见坑）与 docs/99（自测题），补齐源码级决策树/断点闭环/排障速查与 Lab 映射。
- 深化 `spring-core-aop` 核心章节：新增 docs/00（深挖指南）与 docs/99（自测题），扩写 docs/01-06、docs/90（常见坑），补齐源码断点入口/观察点与排障闭环。
- 二次深化 `spring-core-aop`：新增 docs/07-09（AutoProxyCreator 主线 / pointcut 表达式系统 / 多代理叠加与顺序），并新增 4 组 Labs 覆盖 BPP 主线、proceed 嵌套、this vs target、以及多 advisor vs 套娃 proxy 的可断言闭环；同时在 `spring-core-beans` 的 BPP/代理/顺序章节补齐 AutoProxyCreator 承接与跨模块链接。
- 三次深化 `spring-core-aop`：新增 docs/10（真实叠加 Debug Playbook）与集成 Lab（Tx/Cache/Method Security），把“多代理叠加”落到真实基础设施断点与可断言语义，并更新 README/深挖指南/多代理章节导航。
