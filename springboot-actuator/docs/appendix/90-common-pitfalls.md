# 90 - Common Pitfalls（springboot-actuator）

## 常见坑
1. 端点存在但未暴露：只配置了 endpoint，忘了 exposure（或被覆盖）
2. 环境差异：不同 profile/不同配置来源导致“我本地可以，线上不行”
3. 安全边界：暴露端点 ≠ 允许匿名访问

