package com.learning.springboot.bootactuator;

import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.stereotype.Component;

@Component
public class LearningHealthIndicator implements HealthIndicator {

    @Override
    public Health health() {
        return Health.up()
                .withDetail("module", "boot-actuator")
                .withDetail("hint", "change this indicator to learn Actuator")
                .build();
    }
}
