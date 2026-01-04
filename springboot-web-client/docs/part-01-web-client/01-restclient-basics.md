# 01：RestClient（同步）最小闭环

本章用最小示例跑通 RestClient：发请求、解析 JSON、断言请求路径/headers。

## 实验入口

- `springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientRestClientLabTest.java`
  - `restClientGetsGreeting`
  - `restClientSendsExpectedPathAndHeaders`
  - `restClientCanPostJsonBody`

## 你应该观察到什么

- RestClient 是阻塞式（blocking）调用：直接返回 `GreetingResponse`
- MockWebServer 能让你断言“请求到底发了什么”（path/header/body），比手工抓包更可控

