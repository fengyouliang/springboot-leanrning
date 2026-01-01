## Context

本仓库的核心原则是“学习者一运行就能得到反馈”：通过 **可运行（tests）+ 可验证（assertions）+ 可观察（OBSERVE/断点）** 的方式建立 Spring 机制心智模型。

`spring-core-beans` 模块目前已经覆盖：

- 定义层/实例层/缓存与循环依赖的核心概念
- 注入阶段（`postProcessProperties`）与基础设施处理器
- 代理/替换阶段（BPP wrapping）与 early reference

但“BeanDefinition 的合并”是很多深挖路径的关键桥梁：它把定义层的元数据（父子定义、属性值、生命周期方法名等）统一成最终参与创建的 `RootBeanDefinition`，并为后续处理器（例如 `MergedBeanDefinitionPostProcessor` 家族）提供稳定输入。

如果学习者没把这条线打通，后续在阅读 `AbstractAutowireCapableBeanFactory` 的创建链路、或者排查注入/生命周期异常时，会频繁陷入“我拿到的 BD 和真正生效的 BD 不一致”的困惑。

## Goals / Non-Goals

### Goals

- 用一个最小可控的 Lab，把 `getMergedLocalBeanDefinition(...)` 与 `MergedBeanDefinitionPostProcessor` 的调用时机跑出来、看得见、能断言。
- 在 docs 中给出“推荐断点 + 固定观察点”，让学习者可以用相同套路深挖其他章节。
- 提供一个轻量的“bean graph 调试”实验，帮助学习者从异常快速回到：候选集合 → 收敛规则 → 最终注入结果。
- 不引入新的外部依赖，保持 `mvn -q test` 全绿且快速。

### Non-Goals

- 不做通用依赖图导出器（例如全量递归图、JSON 导出、循环检测等）。
- 不要求学习者掌握 XML bean definition inheritance；Lab 只使用最小可控方式构造 parent/child 合并场景。
- 不重构现有文档结构；只做增量补齐与“尾部导航”统一。

## Decisions

- **场景构造方式**：优先使用 programmatic `BeanDefinition` 注册（parent + child），以确保“合并”是确定可复现的，不依赖注解配置的隐式行为。
- **容器选择**：优先 `GenericApplicationContext`/`AnnotationConfigApplicationContext`，并在需要注解处理器时显式调用 `AnnotationConfigUtils.registerAnnotationConfigProcessors(...)`，保证实验最小化、可控、可断言。
- **可观察性实现**：
  - merged BD Lab 使用一个自定义 `MergedBeanDefinitionPostProcessor` 记录调用序列与 merged 后的关键字段（property values、init/destroy method name、scope/lazy 等）。
  - 不直接依赖 Spring 内部私有缓存结构；只观察“公开/稳定的行为与扩展点调用顺序”。
- **文档 footer 模板**：固定为 2 行（对应 Lab/Test + 推荐断点），每章最多列 1 个主入口 Lab/Test，断点 1–3 个，避免变成“冗长索引”。
- **异常对照表落点**：放在 `docs/11`（调试与自检）中，作为“统一排障入口”，并在表内链接到相关章节与 Lab。

## Alternatives Considered

- 仅通过文字解释 merged BD：
  - 结论：学习者难以形成闭环（无法用断点验证“merged 发生了”，也无法感知 `MergedBeanDefinitionPostProcessor` 的时机）。
- 使用 XML 配置复现 parent/child：
  - 结论：引入 XML 学习门槛，与本模块的 Java/annotation 主线不一致；且不利于保持示例短小。
- bean graph 工具做成脚本/CLI：
  - 结论：工具化价值高，但会引入更多工程形态与维护成本；本次先用 test-only helper + Lab 验证学习价值，再考虑工具化。

## Risks / Trade-offs

- 批量为所有章节追加 footer 会触及较多文件：
  - 风险：merge 冲突概率上升（尤其与其他 docs 增量 change 并行时）
  - 缓解：在 apply 阶段先落地 footer 模板并尽量机械化应用；必要时分两次提交（先新增章节/表格，再批量 footer）
- merged BD 场景如果过度依赖内部细节，可能随 Spring 6.x 小版本变化：
  - 缓解：只断言稳定的外部行为（如 “merged BD 包含来自 parent 的属性/元数据”）与扩展点调用发生（而非精确内部调用栈/次数）。

## Migration Plan

1) 先新增 merged BD Lab + 对应章节（最核心的新增价值）。
2) 再补 docs/11 的异常对照表，并用该表链接到新增 Lab 与既有章节（形成导航闭环）。
3) 最后批量追加 docs footer，并更新 README 索引，确保整体导航一致。

## Open Questions

- merged BD 章节是否需要放在 `docs/12`（基础设施）之前，以便学习者更早理解“定义合并 → 元数据准备”？
- bean graph 输出是否要同时提供“按类型候选集合”与“按名称候选集合”（`@Resource` 场景）？（默认：先覆盖按类型）
