package com.learning.springboot.springcorebeans;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class SpringCoreBeansAutoConfigurationExerciseTest {

    @Test
    @Disabled("Exercise: add a new @ConditionalOnProperty gate for DemoGreeting and assert matchIfMissing behavior with ApplicationContextRunner")
    void exercise_addPropertyGateToGreeting() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: create an intentional ambiguity by registering two beans of the same type, then resolve it via @Primary or @Qualifier")
    void exercise_createAndResolveAmbiguity() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a test that prints a small debug summary (active properties + which bean won) without asserting on long logs")
    void exercise_addDebugSummaryHelper() {
        assertThat(true).isFalse();
    }
}

