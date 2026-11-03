# Tasks: Nutrition Tracker

**Input**: Design documents from `/specs/001-nutrition-tracker/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Included because the constitution and plan require validation of normal, invalid,
boundary, and edge cases.

## Format: `- [ ] [ID] [P?] [Story] Description`

- **[P]**: Can run in parallel because it uses a different file or has no incomplete dependency.
- **[Story]**: User Story 1, 2, or 3 for story-specific work.
- Every task includes an exact repository-relative file path.

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Create Flask application package directories in app/, app/templates/, and app/static/css/.
- [X] T002 Create Python dependencies for Flask and pytest in requirements.txt.
- [X] T003 [P] Add Flask application factory and configuration in app/__init__.py.
- [X] T004 [P] Add shared HTML shell and Bootstrap layout in app/templates/base.html.
- [X] T005 [P] Add fundamentals-level application styling in app/static/css/site.css.
- [X] T006 Configure pytest test isolation and temporary SQLite path in tests/conftest.py.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared infrastructure required before any user story can operate.

- [X] T007 Create SQLite connection, initialization, and transactional helpers in app/db.py.
- [X] T008 Create meals schema with id, food_name, category, calories, protein, meal_date, and created_at
  constraints in app/db.py.
- [X] T009 Create reusable nutrition_targets schema with fixed id 1, calorie_target, protein_target,
  and updated_at in app/db.py.
- [X] T010 [P] Implement trimmed 1-120 character food name validation and required-field errors in
  app/validation.py.
- [X] T011 [P] Implement meal category validation for exactly Breakfast, Lunch, Dinner, and Snacks in
  app/validation.py.
- [X] T012 [P] Implement Decimal parsing for finite non-negative calories and protein in app/validation.py.
- [X] T013 [P] Implement valid ISO `YYYY-MM-DD` calendar-date parsing in app/validation.py.
- [X] T014 [P] Implement positive finite Decimal validation for reusable targets in app/validation.py.
- [X] T015 Implement meal row conversion and parameterized CRUD helpers in app/models.py.
- [X] T016 Implement reusable target read and upsert helpers in app/models.py.
- [X] T017 Add shared field-error and friendly database-error rendering support in app/routes.py.
- [X] T018 [P] Add unit tests in tests/test_validation.py covering missing, whitespace, negative,
  nonnumeric, unsupported-category, and invalid-date inputs plus zero and positive numeric boundaries.

**Checkpoint**: Database, validation, models, and application error handling are ready.

---

## Phase 3: User Story 1 - Record and Review Meals (Priority: P1) MVP

**Goal**: Users can add valid meals and view meals and zero/recorded totals for a selected date.

**Independent Test**: Run the Flask client tests in tests/test_meals.py and verify meal creation,
daily list rendering, empty states, and invalid submissions work without targets or edit features.

### Tests for User Story 1

- [X] T019 [P] [US1] Add route tests for valid meal creation and one-per-submission storage in
  tests/test_meals.py.
- [X] T020 [P] [US1] Add route tests for duplicate identical meals remaining separate in tests/test_meals.py.
- [X] T021 [P] [US1] Add route tests for missing fields, negative nutrition, invalid category/date,
  and whitespace food names in tests/test_meals.py.
- [X] T022 [P] [US1] Add route tests for empty selected dates and zero totals in tests/test_meals.py.

### Implementation for User Story 1

- [X] T023 [US1] Implement `GET /` dashboard meal-list and selected-date flow in app/routes.py.
- [X] T024 [US1] Implement Decimal daily calorie and protein summation in app/nutrition.py.
- [X] T025 [US1] Add dashboard selected-date, empty-state, totals, and meal-list rendering in
  app/templates/dashboard.html.
- [X] T026 [US1] Implement `GET /meals/new` with active-date defaults in app/routes.py.
- [X] T027 [US1] Implement `POST /meals` validation, transactional insert, redirect, and field errors in
  app/routes.py.
- [X] T028 [US1] Add reusable meal form for creation with inline field errors in app/templates/meal_form.html.
- [X] T029 [US1] Link the dashboard, new meal form, date selection, and empty states in
  app/templates/dashboard.html and app/templates/meal_form.html.

**Checkpoint**: User Story 1 is independently functional for adding and reviewing meals.

---

## Phase 4: User Story 2 - Maintain Recorded Meals (Priority: P1)

**Goal**: Users can edit every meal field and delete records while daily totals remain accurate.

**Independent Test**: Run tests/test_meals.py and verify editing, moving dates, deleting, confirming
deletion, and recalculating source/destination totals.

### Tests for User Story 2

- [X] T030 [P] [US2] Add route tests for editing valid meal fields in tests/test_meals.py.
- [X] T031 [P] [US2] Add route tests for moving a meal between dates and recalculating both totals in
  tests/test_meals.py.
- [X] T032 [P] [US2] Add route tests for invalid edits leaving the original record unchanged in
  tests/test_meals.py.
- [X] T033 [P] [US2] Add route tests for confirmed deletion and recalculation after deleting the last meal
  in tests/test_meals.py.

### Implementation for User Story 2

- [X] T034 [US2] Implement parameterized meal lookup by primary key in app/models.py.
- [X] T035 [US2] Implement transactional meal update for all fields in app/models.py.
- [X] T036 [US2] Implement transactional meal deletion in app/models.py.
- [X] T037 [US2] Implement `GET /meals/<meal_id>/edit` and not-found handling in app/routes.py.
- [X] T038 [US2] Implement `POST /meals/<meal_id>/edit` validation, source/destination redirect behavior,
  and field errors in app/routes.py.
- [X] T039 [US2] Implement `POST /meals/<meal_id>/delete` with confirmation-compatible UI in app/routes.py.
- [X] T040 [US2] Reuse app/templates/meal_form.html for edit mode and existing values.
- [X] T041 [US2] Add edit and confirmed-delete controls to app/templates/dashboard.html.

**Checkpoint**: User Story 2 supports independently accurate meal maintenance.

---

## Phase 5: User Story 3 - Targets and Daily Progress (Priority: P1)

**Goal**: Users can configure reusable positive targets and see remaining, exceeded, or fully met
calorie and protein progress.

**Independent Test**: Run tests/test_targets.py and tests/test_nutrition.py and verify missing
targets, target validation, reusable targets, exact totals, rounding, and text progress.

### Tests for User Story 3

- [X] T042 [P] [US3] Add unit tests in tests/test_nutrition.py for remaining, exceeded, and fully-met
  calorie/protein status, including exact totals and progress percentages below, at, and above 100%.
- [X] T043 [P] [US3] Add unit tests for Decimal precision and up-to-two-decimal display formatting in
  tests/test_nutrition.py.
- [X] T044 [P] [US3] Add route tests for missing targets and unchanged totals in tests/test_targets.py.
- [X] T045 [P] [US3] Add route tests for positive reusable targets and zero/negative/nonnumeric rejection
  in tests/test_targets.py.
- [X] T046 [P] [US3] Add route tests for text progress without color dependency in tests/test_targets.py.

### Implementation for User Story 3

- [X] T047 [US3] Implement remaining, exceeded, and fully-met comparison logic in app/nutrition.py.
- [X] T048 [US3] Implement user-facing formatting with no more than two decimal places while retaining
  entered precision in
  app/nutrition.py.
- [X] T049 [US3] Integrate reusable target lookup and missing-target state into `GET /` in app/routes.py.
- [X] T050 [US3] Implement `GET /targets` and `POST /targets` in app/routes.py.
- [X] T051 [US3] Add reusable target inputs and validation errors in app/templates/targets.html.
- [X] T052 [US3] Render calorie and protein actual/target/status text in app/templates/dashboard.html
  without color-only meaning.
- [X] T053 [US3] Add accessible non-color progress styling and indicators in app/static/css/site.css.

**Checkpoint**: All three user stories operate together with reusable targets and accurate progress.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T054 [P] Add unexpected operation failure tests that confirm existing meal and target data is
  unchanged in tests/test_meals.py and tests/test_targets.py.
- [X] T055 [P] Add application-restart persistence tests for meals and reusable targets in
  tests/test_persistence.py.
- [X] T056 Add generic friendly error handling and transaction rollback around all mutations in app/routes.py
  and app/db.py.
- [X] T057 Add concise user-facing flash confirmation and navigation in app/templates/base.html and
  app/templates/dashboard.html.
- [X] T058 Run all acceptance scenarios from specs/001-nutrition-tracker/quickstart.md.
- [X] T059 Run complete pytest suite with `pytest -q`.
- [X] T060 Review requirements.md and confirm every checkbox remains valid after implementation in
  specs/001-nutrition-tracker/checklists/requirements.md.

---

## Dependencies

- T007-T017 depend on setup completion (T001-T006).
- User Story 1 depends on foundation tasks T007-T017 and should be delivered first as MVP.
- User Story 2 depends on the meal model, validation, and routes established by User Story 1.
- User Story 3 depends on the shared totals and target foundation, but does not block independent
  meal CRUD work.
- Polish tasks depend on completion of all three user stories.

## Parallel Execution Examples

### User Story 1

- T019-T022 can run together because they target separate test cases in the same test module.
- T024 and T025 can proceed together once the daily data contract is clear.
- T028 and T029 can proceed independently from dashboard computation work.

### User Story 2

- T030-T033 can run together as independent route-test cases.
- T034-T036 can proceed in parallel only after model interfaces are agreed; files such as edit and
  delete routes then integrate their results.

### User Story 3

- T042-T046 can run together across nutrition and target test modules.
- T051-T053 can proceed in parallel after progress text values are defined by T047 and T048.

## Implementation Strategy

Deliver Phase 1 and Phase 2 first, then User Story 1 as the independently usable MVP. Add User Story
2 for record maintenance, then User Story 3 for targets and progress. Finish with cross-cutting error
handling, persistence, documentation validation, and the complete pytest suite.
