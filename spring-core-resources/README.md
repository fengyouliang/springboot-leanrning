# spring-core-resources

本模块用于学习 Spring 的 **`Resource` 抽象**。

包含内容：

- 从 classpath 加载资源（`classpath:`）
- 读取资源内容
- 使用 pattern 加载多个资源（`classpath*:` + `**/*.txt`）

## 学习目标

- 理解为什么需要 `Resource`（classpath / file / URL 的统一抽象）
- 学会安全地读取 `Resource` 内容
- 使用 `ResourcePatternResolver` 按模式加载多个资源

## 运行

```bash
mvn -pl spring-core-resources spring-boot:run
```

运行后观察控制台输出：

- `classpath:data/hello.txt` 的内容
- 通过 `classpath*:data/*.txt` 找到的资源列表

## 测试

```bash
mvn -pl spring-core-resources test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：
  - `SpringCoreResourcesLabTest`：classpath/file 资源读取、pattern 扫描、缺失资源错误
  - `SpringCoreResourcesMechanicsLabTest`：`Resource` exists/description、`classpath*:` 行为
- Exercises（默认禁用）：`SpringCoreResourcesExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl spring-core-resources test`。

## 小练习

- 在 `src/main/resources/data/` 下新增一个文件，并确认 pattern 扫描能找到它
- 尝试加载一个不存在的资源，并做更友好的错误处理
- 加载一个 YAML/JSON 资源并解析它

## 参考

- Spring Framework Reference：Resources
