package com.learning.springboot.bootdatajpa;

import static org.assertj.core.api.Assertions.assertThat;

import jakarta.persistence.EntityManager;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.transaction.support.TransactionSynchronizationManager;

@DataJpaTest
class BootDataJpaLabTest {

    @Autowired
    private BookRepository repository;

    @Autowired
    private EntityManager entityManager;

    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Test
    void savesAndFindsByTitle() {
        Book saved = repository.save(new Book("Domain-Driven Design", "Eric Evans"));

        assertThat(saved.getId()).isNotNull();
        assertThat(repository.findByTitle("Domain-Driven Design"))
                .isPresent()
                .get()
                .extracting(Book::getAuthor)
                .isEqualTo("Eric Evans");
    }

    @Test
    void findByTitleReturnsEmptyWhenMissing() {
        assertThat(repository.findByTitle("missing")).isEmpty();
    }

    @Test
    void saveAssignsId() {
        Book saved = repository.save(new Book("Spring Data JPA", "Learning Team"));
        assertThat(saved.getId()).isNotNull();
    }

    @Test
    void entityIsManagedAfterSaveInSamePersistenceContext() {
        Book saved = repository.save(new Book("Managed", "Author"));
        assertThat(entityManager.contains(saved)).isTrue();
    }

    @Test
    void entityManagerClearDetachesEntities() {
        Book saved = repository.save(new Book("Detach", "Author"));
        assertThat(entityManager.contains(saved)).isTrue();

        entityManager.clear();

        assertThat(entityManager.contains(saved)).isFalse();
    }

    @Test
    void dirtyCheckingPersistsChangesOnFlush() {
        Book saved = repository.save(new Book("Original", "A"));
        saved.changeAuthor("B");

        entityManager.flush();
        entityManager.clear();

        Book reloaded = repository.findById(saved.getId()).orElseThrow();
        assertThat(reloaded.getAuthor()).isEqualTo("B");
    }

    @Test
    void flushMakesRowsVisibleToJdbcTemplateWithinSameTransaction() {
        repository.save(new Book("Flush", "A"));
        entityManager.flush();

        Integer count = jdbcTemplate.queryForObject("select count(*) from books", Integer.class);
        assertThat(count).isNotNull();
        assertThat(count).isGreaterThanOrEqualTo(1);
    }

    @Test
    void deleteRemovesRowAfterFlush() {
        Book saved = repository.save(new Book("ToDelete", "A"));
        entityManager.flush();

        repository.deleteById(saved.getId());
        entityManager.flush();

        assertThat(repository.findById(saved.getId())).isEmpty();
    }

    @Test
    void repositoryCountReflectsInserts() {
        repository.save(new Book("A", "A"));
        repository.save(new Book("B", "B"));
        assertThat(repository.count()).isEqualTo(2);
    }

    @Test
    void dataJpaTestRunsInsideATransaction() {
        assertThat(TransactionSynchronizationManager.isActualTransactionActive()).isTrue();
    }
}
