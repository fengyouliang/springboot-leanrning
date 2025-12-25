package com.learning.springboot.bootbasics;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.runner.ApplicationContextRunner;

class BootBasicsExerciseTest {

    @Test
    @Disabled("Exercise: add a new @ConfigurationProperties field and prove it binds correctly (update README)")
    void exercise_addNewPropertyField() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: demonstrate property precedence with multiple sources and document the observations")
    void exercise_propertyPrecedence() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add an optional feature toggle and conditionally create a bean when enabled")
    void exercise_conditionalBeanByProperty() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: convert these @SpringBootTest tests to ApplicationContextRunner-based tests for faster feedback")
    void exercise_applicationContextRunner() {
        ApplicationContextRunner runner = new ApplicationContextRunner();
        assertThat(runner).isNotNull();
    }

    @Test
    @Disabled("Exercise: add a failure case for invalid property types and assert the startup error")
    void exercise_invalidPropertyType() {
        assertThat(true).isFalse();
    }
}

