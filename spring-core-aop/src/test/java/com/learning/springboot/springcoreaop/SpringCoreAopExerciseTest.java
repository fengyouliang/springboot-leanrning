package com.learning.springboot.springcoreaop;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.aop.framework.AopContext;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringCoreAopExerciseTest {

    @Autowired
    private SelfInvocationExampleService selfInvocationExampleService;

    @Autowired
    private InvocationLog invocationLog;

    @Test
    @Disabled("Exercise: enable exposeProxy and use AopContext.currentProxy() so inner(...) also gets traced")
    void exercise_makeSelfInvocationTriggerAdvice() {
        invocationLog.reset();

        // Hint: exposeProxy requires configuration. When enabled, this should work:
        // ((SelfInvocationExampleService) AopContext.currentProxy()).inner("Bob");
        assertThat(AopContext.currentProxy()).isNotNull();
        assertThat(selfInvocationExampleService.outer("Bob")).contains("outer");
        assertThat(invocationLog.count()).isGreaterThanOrEqualTo(2);
    }

    @Test
    @Disabled("Exercise: add a new Aspect with @Order(0) and prove it runs before the existing TracingAspect")
    void exercise_addOrderedAspect() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add an interface to TracedBusinessService and make Spring use JDK proxies; then assert proxy type changes")
    void exercise_switchToJdkProxy() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: change the pointcut to intercept a package pattern instead of @Traced and update tests accordingly")
    void exercise_changePointcutStyle() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: demonstrate a proxy limitation (final class or final method) and explain it in README")
    void exercise_proxyLimitation() {
        assertThat(true).isFalse();
    }
}

