# 00 - Deep Dive Guide（springboot-web-client）

## 推荐学习目标
1. 能区分 RestClient 与 WebClient 的适用场景与线程模型
2. 能写出可控的错误处理（不要让调用方被底层异常细节污染）
3. 能把超时/重试与幂等性/雪崩风险关联起来思考
4. 能用 MockWebServer 写出“可复现”的客户端测试

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-web-client test`

