# 05. 读取资源：InputStream、编码与“可观察性”

资源读取看起来简单，但学习阶段建议你建立两个习惯：

1) 始终明确编码（尤其文本）  
2) 把错误转换成“更好理解的异常/提示”

## 在本模块如何验证“读取方式”

看 `SpringCoreResourcesMechanicsLabTest#classpathResourceCanBeReadAsBytes`：

- `resource.getInputStream()`
- 读 bytes
- 用 `StandardCharsets.UTF_8` 构建字符串

看 `ResourceReadingService#readClasspathText`：

- 把 `IOException` 包成 `UncheckedIOException`（学习阶段更容易写 tests）

## Debug/观察建议

`Resource#getDescription()` 很有用：

- 它能告诉你这个 resource 是从哪里来的
- 在 classpath/jar 相关问题里，description 往往比 path 更可信

验证入口：`SpringCoreResourcesMechanicsLabTest#resourceDescriptionsHelpWithDebugging`

