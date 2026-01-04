# 00 - Deep Dive Guide（springboot-actuator）

## 推荐学习目标
1. 能描述“端点是否存在”与“端点是否暴露”是两件事
2. 能用最小配置复现 exposure 覆盖/退让，并用测试锁住行为
3. 能定位 Actuator 相关排障的第一现场：`/actuator`、条件报告、日志与配置来源

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-actuator test`

