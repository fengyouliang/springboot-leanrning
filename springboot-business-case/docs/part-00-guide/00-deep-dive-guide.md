# 00 - Deep Dive Guide（springboot-business-case）

## 推荐学习目标
1. 通过“一个真实业务流”理解基础设施如何协作（controller → service → event → aspect）
2. 学会用 tests 做端到端断言，避免只看日志“感觉对了”
3. 学会定位：异常是在哪个边界被转换/传播/吞掉的

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-business-case test`

