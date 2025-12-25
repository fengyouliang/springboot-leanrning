## ADDED Requirements

### Requirement: Root Module Catalog
The repository SHALL provide a root-level module catalog that lists every learning module with a short description and a link to the module documentation.

#### Scenario: Find a learning module by topic
- **WHEN** a learner opens the repository root documentation
- **THEN** the learner can find the relevant module and navigate to its README

### Requirement: Initial Starter Modules
At initial bootstrap, the workspace SHALL include the following starter modules:
- `boot-basics`
- `boot-web-mvc`
- `boot-data-jpa`
- `boot-actuator`
- `boot-testing`

#### Scenario: Verify starter modules exist
- **WHEN** a learner views the workspace module list
- **THEN** each starter module is present and can be built as part of the workspace

### Requirement: Single-Topic Module Scope
Each learning module SHALL declare its primary topic in its module `README.md` and keep its scope focused on that topic.

#### Scenario: Understand module scope quickly
- **WHEN** a learner reads a module `README.md`
- **THEN** the primary topic is stated clearly and the examples align with that topic

