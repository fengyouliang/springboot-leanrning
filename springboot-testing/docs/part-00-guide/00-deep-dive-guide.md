# 00 - Deep Dive Guide（springboot-testing）

## 推荐学习目标
1. 能区分“测试 slice”与“完整 Boot 启动”在 bean 图与自动配置上的差异
2. 能解释 `@MockBean`：它替换的是什么（按类型/按名称）？何时生效？
3. 能用测试把系统行为锁住：断言输出，而不是断言实现细节

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-testing test`

