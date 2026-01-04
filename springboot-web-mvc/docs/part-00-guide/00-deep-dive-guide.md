# 00 - Deep Dive Guide（springboot-web-mvc）

## 推荐学习目标
1. 能说清一次请求在 MVC 中的关键阶段：handler mapping → argument resolve/binding → validation → exception → response
2. 能写出“可复现”的错误塑形与异常处理策略，并用测试断言锁住行为
3. 能解释 Filter/Interceptor 的顺序与影响范围

## 推荐阅读顺序
1. `docs/part-01-web-mvc/01-validation-and-error-shaping.md`
2. `docs/part-01-web-mvc/02-exception-handling.md`
3. `docs/part-01-web-mvc/03-binding-and-converters.md`
4. `docs/part-01-web-mvc/04-interceptor-and-filter-ordering.md`
5. `docs/appendix/90-common-pitfalls.md`
6. `docs/appendix/99-self-check.md`

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-web-mvc test`

