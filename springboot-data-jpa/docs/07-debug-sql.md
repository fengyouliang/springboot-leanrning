# 07. Debug/观察：怎么把 Hibernate 的 SQL“看清楚”？

学习 JPA 时，“看见 SQL”可以极大降低抽象层带来的不确定性。

## 本模块的默认配置

`springboot-data-jpa/src/main/resources/application.properties` 已经开启：

- `spring.jpa.show-sql=true`

这对学习足够了。

## 进一步的观察（可选）

如果你希望看到更详细的 SQL 与参数（学习用即可），可以考虑在本模块的 `application.properties` 里增加：

- `logging.level.org.hibernate.SQL=DEBUG`
- `logging.level.org.hibernate.orm.jdbc.bind=TRACE`

（注意：这些配置不适合生产环境，学习完建议删除/降级）

## 建议的学习姿势

- 先用 tests 得到确定性结论（断言/可复现）
- 再用 SQL 日志解释“为什么会这样”（机制解释）

