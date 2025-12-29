package com.learning.springboot.springcorebeans;

import static org.assertj.core.api.Assertions.assertThat;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

class SpringCoreBeansDependsOnLabTest {

    @Test
    void dependsOn_forcesInitializationOrder_evenWithoutDirectDependencies() {
        List<String> events = new ArrayList<>();

        try (AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext()) {
            context.registerBean("first", First.class, () -> new First(events));
            context.registerBean("second", Second.class, () -> new Second(events), bd -> bd.setDependsOn("first"));
            context.refresh();
        }

        System.out.println("OBSERVE: dependsOn is about initialization order, not about injection");
        assertThat(events).containsExactly(
                "first:constructed",
                "second:constructed"
        );
    }

    static class First {
        First(List<String> events) {
            events.add("first:constructed");
        }
    }

    static class Second {
        Second(List<String> events) {
            events.add("second:constructed");
        }
    }
}
