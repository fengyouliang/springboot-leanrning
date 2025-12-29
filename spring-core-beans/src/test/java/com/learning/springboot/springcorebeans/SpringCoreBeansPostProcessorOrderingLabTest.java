package com.learning.springboot.springcorebeans;

import static org.assertj.core.api.Assertions.assertThat;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanFactoryPostProcessor;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.core.Ordered;
import org.springframework.core.PriorityOrdered;
import org.springframework.context.support.GenericApplicationContext;

class SpringCoreBeansPostProcessorOrderingLabTest {

    @Test
    void beanFactoryPostProcessors_areInvokedInPriorityOrderedThenOrderedThenUnorderedOrder() {
        List<String> events = new ArrayList<>();

        try (GenericApplicationContext context = new GenericApplicationContext()) {
            context.registerBean("priorityBfpp", PriorityBfpp.class, () -> new PriorityBfpp(events));
            context.registerBean("orderedBfpp", OrderedBfpp.class, () -> new OrderedBfpp(events));
            context.registerBean("unorderedBfpp", UnorderedBfpp.class, () -> new UnorderedBfpp(events));
            context.refresh();
        }

        System.out.println("OBSERVE: BFPP ordering is PriorityOrdered -> Ordered -> unordered");
        assertThat(events).containsExactly(
                "bfpp:priority",
                "bfpp:ordered",
                "bfpp:unordered"
        );
    }

    @Test
    void beanPostProcessors_areAppliedInPriorityOrderedThenOrderedThenUnorderedOrder() {
        List<String> events = new ArrayList<>();

        try (GenericApplicationContext context = new GenericApplicationContext()) {
            context.registerBean("priorityBpp", PriorityBpp.class, () -> new PriorityBpp(events));
            context.registerBean("orderedBpp", OrderedBpp.class, () -> new OrderedBpp(events));
            context.registerBean("unorderedBpp", UnorderedBpp.class, () -> new UnorderedBpp(events));

            context.registerBean(Target.class);
            context.refresh();
        }

        System.out.println("OBSERVE: BPP ordering is PriorityOrdered -> Ordered -> unordered");
        assertThat(events).containsExactly(
                "bpp:priority",
                "bpp:ordered",
                "bpp:unordered"
        );
    }

    static class PriorityBfpp implements BeanFactoryPostProcessor, PriorityOrdered {
        private final List<String> events;

        PriorityBfpp(List<String> events) {
            this.events = events;
        }

        @Override
        public int getOrder() {
            return 0;
        }

        @Override
        public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
            events.add("bfpp:priority");
        }
    }

    static class OrderedBfpp implements BeanFactoryPostProcessor, Ordered {
        private final List<String> events;

        OrderedBfpp(List<String> events) {
            this.events = events;
        }

        @Override
        public int getOrder() {
            return 0;
        }

        @Override
        public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
            events.add("bfpp:ordered");
        }
    }

    static class UnorderedBfpp implements BeanFactoryPostProcessor {
        private final List<String> events;

        UnorderedBfpp(List<String> events) {
            this.events = events;
        }

        @Override
        public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
            events.add("bfpp:unordered");
        }
    }

    static class PriorityBpp implements BeanPostProcessor, PriorityOrdered {
        private final List<String> events;

        PriorityBpp(List<String> events) {
            this.events = events;
        }

        @Override
        public int getOrder() {
            return 0;
        }

        @Override
        public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
            if (bean instanceof Target) {
                events.add("bpp:priority");
            }
            return bean;
        }
    }

    static class OrderedBpp implements BeanPostProcessor, Ordered {
        private final List<String> events;

        OrderedBpp(List<String> events) {
            this.events = events;
        }

        @Override
        public int getOrder() {
            return 0;
        }

        @Override
        public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
            if (bean instanceof Target) {
                events.add("bpp:ordered");
            }
            return bean;
        }
    }

    static class UnorderedBpp implements BeanPostProcessor {
        private final List<String> events;

        UnorderedBpp(List<String> events) {
            this.events = events;
        }

        @Override
        public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
            if (bean instanceof Target) {
                events.add("bpp:unordered");
            }
            return bean;
        }
    }

    static class Target {
    }
}
