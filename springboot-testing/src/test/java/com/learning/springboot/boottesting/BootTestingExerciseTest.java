package com.learning.springboot.boottesting;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class BootTestingExerciseTest {

    @Test
    @Disabled("Exercise: add a @WebMvcTest that verifies a 400 response for invalid input (add a new endpoint + validation)")
    void exercise_webMvcValidation() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a @SpringBootTest that proves a bean is NOT loaded in a slice test")
    void exercise_sliceVsFull() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a @TestConfiguration to override a bean and write a focused test")
    void exercise_testConfigurationOverride() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a test using @DynamicPropertySource and document when to use it")
    void exercise_dynamicPropertySource() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a test that uses @MockBean incorrectly and explain what problem it can hide")
    void exercise_mockBeanPitfall() {
        assertThat(true).isFalse();
    }
}

