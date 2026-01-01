## ADDED Requirements

### Requirement: Data JPA Deep Dive Track
The `springboot-data-jpa` module SHALL include deep dive Labs and `@Disabled` Exercises that teach practical JPA mechanics, including:
- entity states and persistence context behavior
- flush timing and transactional boundaries
- common performance pitfalls (intro-level N+1)
- query methods vs explicit queries (JPQL/native) basics

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl springboot-data-jpa test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled
