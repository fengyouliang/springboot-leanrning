package com.learning.springboot.springcoreresources;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SpringCoreResourcesExerciseTest {

    @Autowired
    private ResourceReadingService resourceReadingService;

    @Test
    @Disabled("Exercise: add a new resource under src/main/resources/data/ and update tests + README accordingly")
    void exercise_addNewResourceFile() {
        String content = resourceReadingService.readClasspathText("classpath:data/todo.txt");
        assertThat(content).contains("TODO");
    }

    @Test
    @Disabled("Exercise: implement a method that returns Resource metadata (filename, contentLength) and write tests")
    void exercise_resourceMetadata() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: demonstrate jar vs filesystem resource behavior (document observations)")
    void exercise_jarVsFilesystem() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add a test that proves pattern sorting is stable and update service accordingly if needed")
    void exercise_sorting() {
        assertThat(true).isFalse();
    }

    @Test
    @Disabled("Exercise: add error handling that distinguishes missing resource vs unreadable resource")
    void exercise_errorHandling() {
        assertThat(true).isFalse();
    }
}

