package com.learning.springboot.springcorebeans;

import java.util.UUID;

import org.springframework.beans.factory.ObjectProvider;
import org.springframework.stereotype.Component;

@Component
public class ProviderPrototypeConsumer {

    private final ObjectProvider<PrototypeIdGenerator> idGeneratorProvider;

    public ProviderPrototypeConsumer(ObjectProvider<PrototypeIdGenerator> idGeneratorProvider) {
        this.idGeneratorProvider = idGeneratorProvider;
    }

    public UUID newId() {
        return idGeneratorProvider.getObject().getId();
    }
}

