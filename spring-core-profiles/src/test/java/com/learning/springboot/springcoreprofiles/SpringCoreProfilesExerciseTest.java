package com.learning.springboot.springcoreprofiles;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.runner.ApplicationContextRunner;

class SpringCoreProfilesExerciseTest {

    private final ApplicationContextRunner contextRunner = new ApplicationContextRunner()
            .withUserConfiguration(DevGreetingConfiguration.class, NonDevGreetingConfiguration.class);

    @Test
    @Disabled("Exercise: add a new profile (e.g., 'staging') and make this select a new provider")
    void exercise_addNewProfile() {
        contextRunner
                .withPropertyValues("spring.profiles.active=staging")
                .run(context -> {
                    assertThat(context).hasSingleBean(GreetingProvider.class);
                    assertThat(context.getBean(GreetingProvider.class).greeting()).contains("staging");
                });
    }

    @Test
    @Disabled("Exercise: add a new ConditionalOnProperty flag and make bean selection depend on it")
    void exercise_addNewConditional() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: demonstrate property precedence (e.g., application.properties vs test property overrides)")
    void exercise_propertyPrecedence() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a negative test that asserts context startup fails when GreetingProvider is missing")
    void exercise_missingBeanStartupFailure() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a debug helper that prints activeProfiles and selected provider (for learning)")
    void exercise_debugHelper() {
        assertThat(true).isFalse();
    }
}

