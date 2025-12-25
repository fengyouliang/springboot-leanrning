package com.learning.springboot.springcoreevents;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringCoreEventsExerciseTest {

    @Autowired
    private UserRegistrationService userRegistrationService;

    @Autowired
    private InMemoryAuditLog auditLog;

    @Test
    @Disabled("Exercise: add a second listener that writes a different entry and assert both are present")
    void exercise_multipleListeners() {
        auditLog.clear();

        userRegistrationService.register("Alice");

        assertThat(auditLog.entries()).contains("userRegistered:Alice");
        assertThat(auditLog.entries()).contains("TODO");
    }

    @Test
    @Disabled("Exercise: add @Order to listeners and make a deterministic order assertion")
    void exercise_ordering() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: create an async listener with @Async and prove it runs on a different thread")
    void exercise_asyncListener() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: change the publisher so events are delivered asynchronously by default (multicaster) and update tests")
    void exercise_asyncMulticaster() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a conditional listener (SpEL condition) and prove it only triggers for matching events")
    void exercise_conditionalListener() {
        assertThat(true).isFalse();
    }
}

