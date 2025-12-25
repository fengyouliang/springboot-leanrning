# springboot-data-jpa

本模块用于学习 Spring Data JPA 的入门要点：**Entity**、**Repository**、以及基于 **H2（内存数据库）** 的基本 CRUD。

## 学习目标

- 编写一个简单的 `@Entity`
- 用 `JpaRepository` 完成保存与查询
- 理解测试切片 `@DataJpaTest`

## 运行

```bash
mvn -pl springboot-data-jpa spring-boot:run
```

启动后会在控制台打印一段简单的“写入/查询”示例日志（示例数据写入 H2 内存库）。

## 测试

```bash
mvn -pl springboot-data-jpa test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：`BootDataJpaLabTest`（`@DataJpaTest` 切片）
  - save/find 的最小闭环
  - persistence context（managed/detach）
  - flush 与 JDBC 可见性
  - dirty checking（脏检查）
- Exercises（默认禁用）：`BootDataJpaExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl springboot-data-jpa test`。

## 小练习

- 给 `BookRepository` 增加 `findByAuthor` 查询
- 给 `Book` 增加一个字段 `publishedYear` 并映射到表字段

## 参考

- Spring Data JPA
- Hibernate / JPA
