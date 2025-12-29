# 02. classpath 路径：`classpath:data/x` vs `classpath:/data/x` 有什么区别？

学习阶段最容易踩的坑之一是 classpath 路径写法不一致：

- 有的人写 `classpath:data/hello.txt`
- 有的人写 `classpath:/data/hello.txt`

## 在本模块如何验证

看 `SpringCoreResourcesLabTest`：

- `readsClasspathResourceContent`：`classpath:data/hello.txt`
- `supportsLeadingSlashInClasspathLocation`：`classpath:/data/hello.txt`

两者都能读到 `Hello from classpath`。

## 你应该得到的结论

- 学习阶段你可以把它们当作等价写法（在常见 classpath 场景下）
- 更重要的是：别把 classpath 资源当作 `File` 路径使用（尤其是打包成 jar 后）

