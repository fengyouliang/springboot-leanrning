package com.learning.springboot.springcorebeans;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import java.util.UUID;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.ApplicationContext;

@SpringBootTest
class SpringCoreBeansExerciseTest {

    @Autowired
    private FormattingService formattingService;

    @Autowired
    private DirectPrototypeConsumer directPrototypeConsumer;

    @Autowired
    private ProviderPrototypeConsumer providerPrototypeConsumer;

    @Autowired
    private ApplicationContext applicationContext;

    @Test
    @Disabled("Exercise: remove @Disabled, run the test, then assert the specific Spring exception type for a missing bean lookup")
    void exercise_identifyExceptionTypeForMissingBeanLookup() {
        assertThatThrownBy(() -> applicationContext.getBean("doesNotExist"))
                .isInstanceOf(NoSuchBeanDefinitionException.class);
    }

    @Test
    @Disabled("Exercise: switch FormattingService to use the lower formatter (and update this expected output)")
    void exercise_switchQualifierToLowerCaseFormatter() {
        assertThat(formattingService.format("Hello")).isEqualTo("hello");
    }

    @Test
    @Disabled("Exercise: change DirectPrototypeConsumer so each call returns a fresh prototype id (hint: ObjectProvider or scoped proxy)")
    void exercise_makeDirectPrototypeConsumerUseFreshPrototypeEachCall() {
        UUID first = directPrototypeConsumer.currentId();
        UUID second = directPrototypeConsumer.currentId();
        assertThat(first).isNotEqualTo(second);
    }

    @Test
    @Disabled("Exercise: remove @Qualifier in FormattingService and resolve ambiguity via @Primary (choose which formatter should win)")
    void exercise_resolveMultipleBeansViaPrimaryInsteadOfQualifier() {
        assertThat(formattingService.format("Hello")).isEqualTo("HELLO");
        assertThat(formattingService.formatterImplementation()).containsIgnoringCase("Upper");
    }

    @Test
    @Disabled("Exercise: make providerPrototypeConsumer return the same id twice (hint: make PrototypeIdGenerator singleton) and update expectations")
    void exercise_changePrototypeScopeAndUpdateExpectations() {
        UUID provider1 = providerPrototypeConsumer.newId();
        UUID provider2 = providerPrototypeConsumer.newId();
        assertThat(provider1).isEqualTo(provider2);
    }
}

