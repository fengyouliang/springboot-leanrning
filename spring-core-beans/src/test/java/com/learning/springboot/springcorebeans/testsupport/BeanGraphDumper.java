package com.learning.springboot.springcorebeans.testsupport;

import java.util.Arrays;

import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;

public final class BeanGraphDumper {

    private BeanGraphDumper() {
    }

    public static String dumpCandidates(ConfigurableListableBeanFactory beanFactory, Class<?> requiredType) {
        String[] beanNames = beanFactory.getBeanNamesForType(requiredType);
        Arrays.sort(beanNames);

        StringBuilder builder = new StringBuilder();
        builder.append(requiredType.getSimpleName()).append(" candidates").append(System.lineSeparator());
        if (beanNames.length == 0) {
            builder.append("- (none)").append(System.lineSeparator());
            return builder.toString();
        }

        for (String beanName : beanNames) {
            builder.append("- ").append(beanName);
            if (beanFactory.containsBeanDefinition(beanName) && beanFactory.getBeanDefinition(beanName).isPrimary()) {
                builder.append(" (primary)");
            }
            builder.append(System.lineSeparator());
        }
        return builder.toString();
    }

    public static String dumpDependencies(ConfigurableListableBeanFactory beanFactory, String beanName) {
        String[] dependencies = beanFactory.getDependenciesForBean(beanName);
        Arrays.sort(dependencies);

        StringBuilder builder = new StringBuilder();
        builder.append(beanName).append(System.lineSeparator());

        if (dependencies.length == 0) {
            builder.append("└─ (no dependencies recorded)").append(System.lineSeparator());
            return builder.toString();
        }

        for (int index = 0; index < dependencies.length; index++) {
            String dependency = dependencies[index];
            String branch = (index == dependencies.length - 1) ? "└─ " : "├─ ";
            builder.append(branch).append("depends on: ").append(dependency).append(System.lineSeparator());
        }
        return builder.toString();
    }
}
