## ADDED Requirements

### Requirement: Mechanism deep-dive chapters use a heavy “source anchors + breakpoint loop” template
The `spring-core-beans` module SHALL standardize its mechanism deep-dive documentation chapters so that advanced learners can map concepts to Spring internals and close the loop via runnable Lab/Test breakpoints.

For this requirement, “mechanism deep-dive chapters” are defined as:

- `spring-core-beans/docs/12-*.md` … `spring-core-beans/docs/34-*.md`
- excluding list/self-check chapters (`spring-core-beans/docs/90-*`, `spring-core-beans/docs/99-*`)
- excluding foundation chapters (`spring-core-beans/docs/01-*` … `11-*`)

Each mechanism deep-dive chapter SHALL include the following sections (headings must match exactly for searchability):

1) `## 源码锚点（建议从这里下断点）`
   - SHALL list at least 3 “class#method” anchors (method-level preferred)
   - SHALL include a 1-line “why this anchor matters” hint per anchor (can be brief)

2) `## 断点闭环（用本仓库 Lab/Test 跑一遍）`
   - SHALL link to at least one runnable repository test entrypoint (typically a `*LabTest` file path; a specific test method is acceptable)
   - SHALL include a recommended breakpoint list (typically 3–6 points) and “what to observe” notes

3) `## 排障分流：这是定义层问题还是实例层问题？`
   - SHALL provide at least 3 symptom-to-layer triage bullets
   - SHALL cross-link to either the chapter’s own Lab/Test entrypoint or a relevant debugging chapter (e.g., container visibility / DI resolution)

#### Scenario: Find where to debug a mechanism chapter
- **WHEN** a learner opens any mechanism deep-dive chapter under `spring-core-beans/docs/12-*.md` … `34-*.md`
- **THEN** the learner can immediately locate “源码锚点” and identify at least 3 “class#method” anchors to set breakpoints on

#### Scenario: Close the loop with runnable experiments
- **WHEN** a learner follows a chapter’s “断点闭环” section and runs the referenced `*LabTest`
- **THEN** the learner can reproduce and observe the described mechanism using the suggested breakpoints, without needing a full Spring Boot application run

