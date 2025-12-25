package com.learning.springboot.springcoretx;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringCoreTxExerciseTest {

    @Autowired
    private AccountRepository accountRepository;

    @Autowired
    private AccountService accountService;

    @Test
    @Disabled("Exercise: add a new method with Propagation.REQUIRES_NEW and prove its behavior with assertions")
    void exercise_requiresNew() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: demonstrate the self-invocation pitfall for @Transactional and show a mitigation")
    void exercise_selfInvocation() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a checked-exception rollback rule to AccountService and update expectations")
    void exercise_checkedRollbackRule() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a test that asserts transaction boundaries via TransactionSynchronizationManager")
    void exercise_transactionIntrospection() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a negative test: remove @Transactional from createTwoAccountsThenFail and observe what breaks")
    void exercise_removeTransactional() {
        accountRepository.deleteAll();
        accountService.createTwoAccountsThenFail();
        assertThat(accountRepository.count()).isEqualTo(0);
    }
}

