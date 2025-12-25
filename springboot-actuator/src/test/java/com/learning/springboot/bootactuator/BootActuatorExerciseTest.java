package com.learning.springboot.bootactuator;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class BootActuatorExerciseTest {

    @Test
    @Disabled("Exercise: add a new HealthIndicator that can be toggled UP/DOWN via a property and test it")
    void exercise_toggleableHealthIndicator() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add an InfoContributor and prove it appears on /actuator/info")
    void exercise_infoContributor() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: restrict endpoint exposure and prove endpoints return 404 when not exposed")
    void exercise_endpointExposure() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a custom actuator endpoint (@Endpoint) and test it")
    void exercise_customEndpoint() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add security (basic) for actuator endpoints and test authorized vs unauthorized responses")
    void exercise_actuatorSecurity() {
        assertThat(true).isFalse();
    }
}

