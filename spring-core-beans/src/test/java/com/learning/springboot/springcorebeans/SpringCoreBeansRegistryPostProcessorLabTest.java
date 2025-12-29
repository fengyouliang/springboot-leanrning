package com.learning.springboot.springcorebeans;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanFactoryPostProcessor;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.beans.factory.support.BeanDefinitionBuilder;
import org.springframework.beans.factory.support.BeanDefinitionRegistry;
import org.springframework.beans.factory.support.BeanDefinitionRegistryPostProcessor;
import org.springframework.context.support.GenericApplicationContext;

class SpringCoreBeansRegistryPostProcessorLabTest {

    @Test
    void beanDefinitionRegistryPostProcessor_canRegisterNewBeanDefinitions() {
        try (GenericApplicationContext context = new GenericApplicationContext()) {
            context.registerBean(Registrar.class);
            context.refresh();

            RegisteredBean bean = context.getBean(RegisteredBean.class);

            System.out.println("OBSERVE: BDRPP registered a new BeanDefinition => bean becomes available");
            assertThat(bean.origin()).isEqualTo("from-bdrpp");
        }
    }

    @Test
    void bdrppRunsBeforeRegularBeanFactoryPostProcessor() {
        try (GenericApplicationContext context = new GenericApplicationContext()) {
            context.registerBean(Registrar.class);
            context.registerBean(Modifier.class);
            context.refresh();

            RegisteredBean bean = context.getBean(RegisteredBean.class);

            System.out.println("OBSERVE: BFPP can modify definitions that were registered by BDRPP");
            assertThat(bean.origin()).isEqualTo("modified-by-bfpp");
        }
    }

    static class RegisteredBean {
        private String origin;

        public void setOrigin(String origin) {
            this.origin = origin;
        }

        String origin() {
            return origin;
        }
    }

    static class Registrar implements BeanDefinitionRegistryPostProcessor {

        @Override
        public void postProcessBeanDefinitionRegistry(BeanDefinitionRegistry registry) throws BeansException {
            registry.registerBeanDefinition(
                    "registeredBean",
                    BeanDefinitionBuilder.genericBeanDefinition(RegisteredBean.class)
                            .addPropertyValue("origin", "from-bdrpp")
                            .getBeanDefinition()
            );
            System.out.println("OBSERVE: BDRPP registered definition 'registeredBean'");
        }

        @Override
        public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
        }
    }

    static class Modifier implements BeanFactoryPostProcessor {

        @Override
        public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
            beanFactory.getBeanDefinition("registeredBean")
                    .getPropertyValues()
                    .add("origin", "modified-by-bfpp");

            System.out.println("OBSERVE: BFPP modified definition 'registeredBean' before instantiation");
        }
    }
}
