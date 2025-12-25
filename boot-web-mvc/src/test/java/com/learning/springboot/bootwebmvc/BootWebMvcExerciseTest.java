package com.learning.springboot.bootwebmvc;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class BootWebMvcExerciseTest {

    @Test
    @Disabled("Exercise: add a new endpoint (e.g., GET /api/users/{id}) and test it via MockMvc")
    void exercise_pathVariables() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a @ControllerAdvice handler for JSON parse errors and return a consistent ApiError shape")
    void exercise_handleMalformedJson() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a HandlerInterceptor and prove it runs for /api/* routes")
    void exercise_interceptor() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a Converter/Formatter for request binding and prove it works")
    void exercise_converterFormatter() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add an integration test that starts the server and verifies behavior end-to-end")
    void exercise_integrationTest() {
        assertThat(true).isFalse();
    }
}

