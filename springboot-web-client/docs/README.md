# springboot-web-client 文档

本模块聚焦 Spring Boot 里的客户端调用：`RestClient` 与 `WebClient` 的使用方式、错误处理、超时重试，以及可测试性。

## Start Here
- 导读：[part-00-guide/00-deep-dive-guide.md](part-00-guide/00-deep-dive-guide.md)

## Part 01 - Web Client（主线机制）
- 01 RestClient 基础：[part-01-web-client/01-restclient-basics.md](part-01-web-client/01-restclient-basics.md)
- 02 WebClient 基础：[part-01-web-client/02-webclient-basics.md](part-01-web-client/02-webclient-basics.md)
- 03 错误处理：[part-01-web-client/03-error-handling.md](part-01-web-client/03-error-handling.md)
- 04 超时与重试：[part-01-web-client/04-timeout-and-retry.md](part-01-web-client/04-timeout-and-retry.md)
- 05 使用 MockWebServer 测试：[part-01-web-client/05-testing-with-mockwebserver.md](part-01-web-client/05-testing-with-mockwebserver.md)

## Appendix
- 常见坑：[appendix/90-common-pitfalls.md](appendix/90-common-pitfalls.md)
- 自测题：[appendix/99-self-check.md](appendix/99-self-check.md)

## Labs & Exercises（最小可复现入口）
- RestClient Lab：`springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientRestClientLabTest.java`
- WebClient Lab：`springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientWebClientLabTest.java`
- Exercises：`springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part00_guide/BootWebClientExerciseTest.java`
