package com.learning.springboot.springcorebeans;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class SpringCoreBeansAutoConfigurationExerciseTest {

    @Test
    @Disabled("练习：给 DemoGreeting 增加一个 @ConditionalOnProperty 门禁，并用 ApplicationContextRunner 断言 matchIfMissing 行为")
    void exercise_addPropertyGateToGreeting() {
        assertThat(true)
                .as("""
                        练习：给 DemoGreeting 增加一个 @ConditionalOnProperty 门禁，并用 ApplicationContextRunner 断言 matchIfMissing 行为。

                        下一步：
                        1) 在自动装配/配置类中为某个 Bean 增加 `@ConditionalOnProperty`。
                        2) 用 runner 分别覆盖：缺失该 property / property=false / property=true。
                        3) 断言 Bean 是否存在，并记录 matchIfMissing 的行为。

                        参考：
                        - `spring-core-beans/src/test/java/.../SpringCoreBeansAutoConfigurationLabTest.java`
                        - `spring-core-beans/src/test/java/.../SpringCoreBeansConditionEvaluationReportLabTest.java`（matchIfMissing 三态）
                        - `spring-core-beans/src/test/java/.../SpringCoreBeansAutoConfigurationOrderingLabTest.java`（顺序/时机类问题的最小复现写法）
                        - `spring-core-beans/docs/10-spring-boot-auto-configuration.md`
                        """)
                .isFalse();
    }

    @Test
    @Disabled("练习：故意制造同类型 Bean 的歧义（注册两个 Bean），再用 @Primary 或 @Qualifier 解决")
    void exercise_createAndResolveAmbiguity() {
        assertThat(true)
                .as("""
                        练习：故意制造同类型 Bean 的歧义（注册两个 Bean），再用 @Primary 或 @Qualifier 解决。

                        下一步：
                        1) 先制造歧义：在同一个场景里注册两个相同类型 Bean。
                        2) 观察启动失败的异常（NoUniqueBeanDefinitionException）。
                        3) 再用 @Primary/@Qualifier 让它变成“确定性选择”。

                        建议阅读：
                        - `spring-core-beans/docs/03-dependency-injection-resolution.md`
                        """)
                .isFalse();
    }

    @Test
    @Disabled("练习：增加一个小的 debug summary（active properties + 谁赢了），避免对长日志做断言")
    void exercise_addDebugSummaryHelper() {
        assertThat(true)
                .as("""
                        练习：增加一个小的 debug summary（active properties + 谁赢了），避免对长日志做断言。

                        下一步：
                        1) 写一个 helper：输出关键 property + 最终注入的 Bean 名/类型。
                        2) 测试里断言关键事实（Bean 存在/类型），而不是断言整段日志。

                        建议阅读：
                        - `spring-core-beans/docs/11-debugging-and-observability.md`
                        """)
                .isFalse();
    }
}
