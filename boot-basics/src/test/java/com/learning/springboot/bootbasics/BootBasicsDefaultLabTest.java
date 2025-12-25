package com.learning.springboot.bootbasics;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.core.env.Environment;

@SpringBootTest
class BootBasicsDefaultLabTest {

    @Autowired
    private AppProperties properties;

    @Autowired
    private GreetingProvider greetingProvider;

    @Autowired
    private Environment environment;

    @Test
    void loadsDefaultProfileConfigurationAndBean() {
        assertThat(properties.getName()).isEqualTo("boot-basics");
        assertThat(properties.getGreeting()).isEqualTo("你好，默认配置");
        assertThat(properties.isFeatureEnabled()).isFalse();

        assertThat(greetingProvider).isInstanceOf(DefaultGreetingProvider.class);
        assertThat(greetingProvider.greeting()).contains("default bean");
    }

    @Test
    void activeProfilesDoNotContainDevByDefault() {
        assertThat(environment.getActiveProfiles()).doesNotContain("dev");
        assertThat(environment.getDefaultProfiles()).contains("default");
    }

    @Test
    void greetingProviderUsesBoundProperties() {
        assertThat(greetingProvider.greeting()).contains(properties.getGreeting());
    }

    @Test
    void canReadRawPropertyValuesFromEnvironment() {
        assertThat(environment.getProperty("app.name")).isEqualTo("boot-basics");
        assertThat(environment.getProperty("app.feature-enabled")).isEqualTo("false");
    }
}
