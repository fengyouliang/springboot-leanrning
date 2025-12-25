package com.learning.springboot.springcorebeans;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class SpringCoreBeansImportExerciseTest {

    @Test
    @Disabled("Exercise: extend the @Import lab to import two configurations and explain which beans come from which config")
    void exercise_importMultipleConfigurations() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: modify the ImportSelector lab so selection depends on two properties (e.g., mode + enabled flag) and add assertions")
    void exercise_importSelectorWithMultipleConditions() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: enhance the registrar lab to read multiple annotation attributes and register multiple bean definitions (with different names)")
    void exercise_registrarRegistersMultipleBeans() {
        assertThat(true).isFalse();
    }
}

