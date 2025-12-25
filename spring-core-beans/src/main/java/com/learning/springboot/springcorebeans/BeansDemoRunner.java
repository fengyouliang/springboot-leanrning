package com.learning.springboot.springcorebeans;

import java.util.UUID;

import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class BeansDemoRunner implements ApplicationRunner {

    private final FormattingService formattingService;
    private final DirectPrototypeConsumer directPrototypeConsumer;
    private final ProviderPrototypeConsumer providerPrototypeConsumer;
    private final LifecycleLogger lifecycleLogger;

    public BeansDemoRunner(
            FormattingService formattingService,
            DirectPrototypeConsumer directPrototypeConsumer,
            ProviderPrototypeConsumer providerPrototypeConsumer,
            LifecycleLogger lifecycleLogger
    ) {
        this.formattingService = formattingService;
        this.directPrototypeConsumer = directPrototypeConsumer;
        this.providerPrototypeConsumer = providerPrototypeConsumer;
        this.lifecycleLogger = lifecycleLogger;
    }

    @Override
    public void run(ApplicationArguments args) {
        System.out.println("== spring-core-beans ==");

        System.out.println("qualifier.formatterImplementation=" + formattingService.formatterImplementation());
        System.out.println("format(\"Hello\")=" + formattingService.format("Hello"));

        UUID direct1 = directPrototypeConsumer.currentId();
        UUID direct2 = directPrototypeConsumer.currentId();
        System.out.println("prototype.direct.sameId=" + direct1.equals(direct2));

        UUID provider1 = providerPrototypeConsumer.newId();
        UUID provider2 = providerPrototypeConsumer.newId();
        System.out.println("prototype.provider.differentId=" + !provider1.equals(provider2));

        System.out.println("lifecycle.initialized=" + lifecycleLogger.isInitialized());
    }
}

