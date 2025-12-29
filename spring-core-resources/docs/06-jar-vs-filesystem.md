# 06. jar vs filesystem：为什么在 IDE 里 OK，打包后就不行？

这是资源读取最经典的学习坑：

- IDE 运行：资源在 `target/classes`，看起来像文件夹
- 打包运行：资源在 jar 内部，不再是“文件系统路径”

因此这些做法容易出问题：

- `resource.getFile()`（classpath 资源在 jar 内时通常会失败）
- `new File("classpath:...")`（根本不是文件路径）

## 在本模块的练习入口

看 `SpringCoreResourcesExerciseTest#exercise_jarVsFilesystem`：

- 目标：写一个实验对比 jar 与 filesystem 的差异
- 并把观察结果记录到 README/docs（学习用）

## 学习建议

学习阶段建议坚持使用：

- `Resource#getInputStream()`（最通用）
- `ResourcePatternResolver`（pattern 扫描）

等你把机制吃透后，再讨论“什么时候可以用 File 优化”。

