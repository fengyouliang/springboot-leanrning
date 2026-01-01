# Change: Add Additional Spring Core Learning Modules (Validation, Resources, Tx, Profiles)

## Why
After introducing the first Spring Core modules (`spring-core-beans`, `spring-core-aop`, `spring-core-events`), learners are ready for additional fundamentals that appear frequently in real Spring apps:

- Validation (Bean Validation integration and common patterns)
- Resources abstraction (classpath/file/URL resources, patterns)
- Transaction management (declarative `@Transactional` and rollback behavior)
- Profiles / conditional bean registration (how configuration changes what beans exist)

Keeping each topic in its own runnable module preserves the repository’s beginner-friendly structure while enabling gradual, focused learning.

## What Changes
- Add four new modules:
  - `spring-core-validation`
  - `spring-core-resources`
  - `spring-core-tx`
  - `spring-core-profiles`
- Update the root module catalog (flat list) to include these modules.
- Keep each module self-contained (no shared `common` module) and runnable with the same workflow as existing modules.

## Impact
- Affected specs:
  - `spring-core-validation-module`
  - `spring-core-resources-module`
  - `spring-core-tx-module`
  - `spring-core-profiles-module`
  - `learning-module-catalog`
- Affected code (apply stage):
  - Root build module list (`pom.xml`)
  - Root catalog (`README.md`)
  - New module directories with code, tests, and docs:
    - `spring-core-validation/`
    - `spring-core-resources/`
    - `spring-core-tx/`
    - `spring-core-profiles/`

