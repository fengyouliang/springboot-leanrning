package com.learning.springboot.bootdatajpa;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

@DataJpaTest
class BootDataJpaExerciseTest {

    @Test
    @Disabled("Exercise: add a new repository query method and prove it works (e.g., findByAuthor)")
    void exercise_addQueryMethod() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a new entity relationship (e.g., Author -> Books) and demonstrate a fetch pitfall (N+1)")
    void exercise_relationshipsAndFetching() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: demonstrate rollback behavior in @DataJpaTest (e.g., @Commit or @Rollback(false))")
    void exercise_rollbackBehavior() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: demonstrate getReferenceById lazy behavior and document what you observe")
    void exercise_getReferenceById() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a JPQL or native query and prove it returns the expected result")
    void exercise_customQuery() {
        assertThat(true).isFalse();
    }
}

