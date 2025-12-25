# springboot-actuator

本模块用于学习 Spring Boot Actuator 的基础用法：

- 暴露常用 Actuator 端点（例如 `/actuator/health`）
- 编写一个自定义 `HealthIndicator`

## 学习目标

- 理解 Actuator 是什么、默认有哪些端点
- 学会通过配置暴露端点与显示 health 详情
- 自己实现一个健康检查指标并出现在 `/actuator/health` 里

## 运行

```bash
mvn -pl springboot-actuator spring-boot:run
```

默认端口：`8082`

### 快速验证

```bash
curl http://localhost:8082/actuator/health
```

你应该能看到 `components.learning`（或类似字段）出现在 health 输出中。

## 测试

```bash
mvn -pl springboot-actuator test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：
  - `BootActuatorLabTest`：health/info 的默认行为、custom health indicator
  - `BootActuatorExposureOverrideLabTest`：通过 properties 改变 endpoint exposure 并验证效果
- Exercises（默认禁用）：`BootActuatorExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl springboot-actuator test`。

## 小练习

- 把自定义健康检查改成：当某个配置项关闭时返回 `DOWN`
- 只在 `dev` profile 下显示 health details（提示：生产环境不建议默认暴露 details）

## 参考

- Spring Boot Actuator
