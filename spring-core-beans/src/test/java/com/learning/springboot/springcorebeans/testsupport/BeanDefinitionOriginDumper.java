package com.learning.springboot.springcorebeans.testsupport;

import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.beans.factory.support.AbstractBeanDefinition;

public final class BeanDefinitionOriginDumper {

    private BeanDefinitionOriginDumper() {
    }

    public static String dump(ConfigurableListableBeanFactory beanFactory, String beanName) {
        if (!beanFactory.containsBeanDefinition(beanName)) {
            return beanName + System.lineSeparator()
                    + "└─ (no BeanDefinition, maybe resolvable dependency or manual singleton?)" + System.lineSeparator();
        }

        BeanDefinition definition = beanFactory.getBeanDefinition(beanName);

        StringBuilder builder = new StringBuilder();
        builder.append(beanName).append(System.lineSeparator());
        builder.append("├─ beanClassName: ").append(nullToDash(definition.getBeanClassName())).append(System.lineSeparator());
        builder.append("├─ resource: ").append(nullToDash(definition.getResourceDescription())).append(System.lineSeparator());
        builder.append("├─ role: ").append(definition.getRole()).append(System.lineSeparator());

        if (definition instanceof AbstractBeanDefinition abd) {
            builder.append("├─ factoryBeanName: ").append(nullToDash(abd.getFactoryBeanName())).append(System.lineSeparator());
            builder.append("├─ factoryMethodName: ").append(nullToDash(abd.getFactoryMethodName())).append(System.lineSeparator());
            builder.append("├─ scope: ").append(blankToDash(abd.getScope())).append(System.lineSeparator());
            builder.append("├─ primary: ").append(abd.isPrimary()).append(System.lineSeparator());

            BeanDefinition originating = abd.getOriginatingBeanDefinition();
            builder.append("├─ originatingBeanDefinition: ")
                    .append(originating == null ? "-" : originating.getClass().getName())
                    .append(System.lineSeparator());
        }

        Object source = definition.getSource();
        builder.append("└─ source: ")
                .append(source == null ? "-" : source.getClass().getName())
                .append(System.lineSeparator());

        return builder.toString();
    }

    private static String nullToDash(String value) {
        return value == null ? "-" : value;
    }

    private static String blankToDash(String value) {
        return value == null || value.isBlank() ? "-" : value;
    }
}
