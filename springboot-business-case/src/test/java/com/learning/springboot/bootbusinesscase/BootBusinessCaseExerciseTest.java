package com.learning.springboot.bootbusinesscase;

import static org.assertj.core.api.Assertions.assertThat;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import com.learning.springboot.bootbusinesscase.domain.PurchaseOrderRepository;

@SpringBootTest
@AutoConfigureMockMvc
class BootBusinessCaseExerciseTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private PurchaseOrderRepository repository;

    @Test
    @Disabled("Exercise: implement GET /api/orders/{id} and make this test pass")
    void exercise_getOrderById() throws Exception {
        assertThat(repository.count()).isEqualTo(0);
        mockMvc.perform(get("/api/orders/1"))
                .andExpect(status().isOk());
    }

    @Test
    @Disabled("Exercise: implement GET /api/orders and make this test pass")
    void exercise_listOrders() throws Exception {
        mockMvc.perform(get("/api/orders"))
                .andExpect(status().isOk());
    }

    @Test
    @Disabled("Exercise: change OrderService so checked exceptions also roll back (and demonstrate via a new endpoint + test)")
    void exercise_checkedExceptionRollbackRule() {
        // Enable this test, then implement a new flow that throws a checked exception inside @Transactional.
        // Default Spring rollback behavior is runtime exceptions; learn how to change it.
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: demonstrate self-invocation pitfall (Tx/AOP) and document the mitigation")
    void exercise_selfInvocationPitfall() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add an AFTER_ROLLBACK transactional event listener and assert it triggers only on rollback")
    void exercise_transactionalEventAfterRollback() {
        assertThat(true).isFalse();
    }
}

