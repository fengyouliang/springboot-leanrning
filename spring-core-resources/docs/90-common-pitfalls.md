# 90. 常见坑清单（建议反复对照）

## 坑 1：把 classpath 资源当成 File

- 现象：本地 OK，打包后失败
- 建议：优先 `getInputStream()`，不要依赖 `getFile()`

## 坑 2：以为 `getResource(...)` 会在不存在时返回 null

- 事实：它返回 handle，需要 `exists()` 判断（见 [docs/04](04-exists-and-handles.md)）

## 坑 3：pattern 扫描结果顺序不稳定导致 tests 抖动

- 建议：排序后再断言（本模块 service 已经这么做）

## 坑 4：忽略编码导致内容乱码

- 建议：读取文本时显式使用 UTF-8（见 [docs/05](05-reading-and-encoding.md)）

## 坑 5：错误处理太粗糙

- 建议：区分“资源不存在”与“资源不可读”（Exercise 里会练）

