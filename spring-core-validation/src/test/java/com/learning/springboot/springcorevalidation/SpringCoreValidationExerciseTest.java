package com.learning.springboot.springcorevalidation;

import static org.assertj.core.api.Assertions.assertThat;

import jakarta.validation.ConstraintViolation;

import java.util.Set;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringCoreValidationExerciseTest {

    @Autowired
    private ProgrammaticValidationService programmaticValidationService;

    @Test
    @Disabled("Exercise: add a new constraint to CreateUserCommand (e.g., @Size) and update this test to assert the new violation")
    void exercise_addNewConstraint() {
        CreateUserCommand invalid = new CreateUserCommand("", "not-an-email", -1);
        Set<ConstraintViolation<CreateUserCommand>> violations = programmaticValidationService.validate(invalid);

        assertThat(violations).hasSizeGreaterThanOrEqualTo(4);
    }

    @Test
    @Disabled("Exercise: introduce validation groups for Create vs Update and demonstrate different constraints per group")
    void exercise_validationGroups() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a custom constraint annotation and prove it works via programmatic validation")
    void exercise_customConstraint() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: demonstrate that method validation requires proxies (compare Spring bean vs direct new)")
    void exercise_methodValidationNeedsProxy() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add @Validated(groups=...) usage and prove group-based method validation behavior")
    void exercise_methodValidationGroups() {
        assertThat(true).isFalse();
    }
}

