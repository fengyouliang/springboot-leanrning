package com.learning.springboot.springcorebeans;

import static org.assertj.core.api.Assertions.assertThat;

import java.util.List;

import org.junit.jupiter.api.Test;
import org.springframework.boot.autoconfigure.AutoConfiguration;
import org.springframework.boot.autoconfigure.AutoConfigurations;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.boot.autoconfigure.condition.ConditionEvaluationReport;
import org.springframework.boot.test.context.runner.ApplicationContextRunner;
import org.springframework.context.annotation.Bean;

class SpringCoreBeansConditionEvaluationReportLabTest {

    private final ApplicationContextRunner contextRunner = new ApplicationContextRunner()
            .withConfiguration(AutoConfigurations.of(PropertyGatedAutoConfiguration.class));

    @Test
    void conditionEvaluationReport_recordsNoMatchWhenPropertyIsMissing() {
        contextRunner.run(context -> {
            assertThat(context).doesNotHaveBean(DemoFeature.class);

            ConditionEvaluationReport report = ConditionEvaluationReport.get(context.getBeanFactory());
            ConditionEvaluationReport.ConditionAndOutcomes outcomes = report.getConditionAndOutcomesBySource()
                    .get(PropertyGatedAutoConfiguration.class.getName());

            assertThat(outcomes).isNotNull();
            assertThat(outcomes.isFullMatch()).isFalse();

            List<String> negativeMessages = outcomes.stream()
                    .filter(it -> !it.getOutcome().isMatch())
                    .map(it -> it.getOutcome().getMessage())
                    .toList();

            System.out.println("OBSERVE: ConditionEvaluationReport shows why auto-config did NOT match");
            System.out.println("OBSERVE: source=" + PropertyGatedAutoConfiguration.class.getName());
            System.out.println("OBSERVE: fullMatch=" + outcomes.isFullMatch());
            negativeMessages.stream()
                    .limit(3)
                    .forEach(message -> System.out.println("OBSERVE: - " + message));
        });
    }

    @Test
    void conditionEvaluationReport_recordsMatchWhenPropertyIsEnabled() {
        contextRunner
                .withPropertyValues("demo.feature.enabled=true")
                .run(context -> {
                    assertThat(context).hasSingleBean(DemoFeature.class);
                    assertThat(context.getBean(DemoFeature.class).origin()).isEqualTo("enabled-by-property");

                    ConditionEvaluationReport report = ConditionEvaluationReport.get(context.getBeanFactory());
                    ConditionEvaluationReport.ConditionAndOutcomes outcomes = report.getConditionAndOutcomesBySource()
                            .get(PropertyGatedAutoConfiguration.class.getName());

                    assertThat(outcomes).isNotNull();
                    assertThat(outcomes.isFullMatch()).isTrue();

                    System.out.println("OBSERVE: ConditionEvaluationReport shows this auto-config matched (fullMatch=true)");
                    System.out.println("OBSERVE: source=" + PropertyGatedAutoConfiguration.class.getName());
                });
    }

    record DemoFeature(String origin) {
    }

    @AutoConfiguration
    @ConditionalOnProperty(prefix = "demo.feature", name = "enabled", havingValue = "true")
    static class PropertyGatedAutoConfiguration {
        @Bean
        DemoFeature demoFeature() {
            return new DemoFeature("enabled-by-property");
        }
    }
}

