# Tasks: Modern UI Enhancement

**Input**: Design documents from `/specs/002-modern-ui-enhancement/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/ui-contract.md, quickstart.md

**Organization**: Tasks are grouped by user story so each UI increment can be implemented and verified independently.

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Confirm the existing Flask templates, stylesheet, and test suite are the baseline in app/templates/, app/static/css/site.css, and tests/ (AC: UI-AC-09)
- [X] T002 [P] Add the UI enhancement section structure to app/static/css/site.css and preserve existing page styling compatibility (AC: UI-AC-01, UI-AC-08)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared presentation foundations required before story-specific UI work.

- [X] T003 Define the sage green, white, neutral, status, spacing, and transition theme variables in app/static/css/site.css (AC: UI-AC-01, UI-AC-03, UI-AC-08)
- [X] T004 Add reusable card, button, form-control, validation, focus, and status classes in app/static/css/site.css (AC: UI-AC-05, UI-AC-06, UI-AC-08)
- [X] T005 Update the shared page shell and navigation styling in app/templates/base.html (AC: UI-AC-01, UI-AC-10)

**Checkpoint**: Foundation ready; user stories can proceed independently.

---

## Phase 3: User Story 1 - Review Daily Nutrition Dashboard (Priority: P1) 🎯 MVP

**Goal**: Present calorie and protein summaries and progress clearly on a responsive dashboard.
**Independent Test**: Open populated, empty, remaining, exceeded, and fully-met dashboard states and verify existing values plus responsive status presentation.

- [X] T006 [P] [US1] Add a responsive dashboard summary-card wrapper around calorie and protein data in app/templates/dashboard.html (AC: UI-AC-01)
- [X] T007 [US1] Render calorie actual, target, remaining/exceeded/fully-met text, and existing numeric progress in app/templates/dashboard.html (AC: UI-AC-02, UI-AC-03, UI-AC-04)
- [X] T008 [US1] Render protein actual, target, remaining/exceeded/fully-met text, and existing numeric progress in app/templates/dashboard.html (AC: UI-AC-02, UI-AC-03, UI-AC-04)
- [X] T009 [US1] Add accessible calorie and protein Bootstrap progress bars capped visually at 100 percent in app/templates/dashboard.html (AC: UI-AC-02, UI-AC-03, UI-AC-04)
- [X] T010 [US1] Add status-specific positive, warning, and fully-met visual classes in app/static/css/site.css (AC: UI-AC-02, UI-AC-03)
- [X] T011 [US1] Style the calorie and protein summary cards in app/static/css/site.css (AC: UI-AC-01, UI-AC-10)
- [X] T012 [US1] Prevent progress bars from appearing when reusable nutrition targets are missing in app/templates/dashboard.html (AC: UI-AC-04, UI-AC-09)
- [X] T013 [US1] Replace the plain empty-meal alert with a styled guided empty state and Add Meal action in app/templates/dashboard.html (AC: UI-AC-04)
- [X] T014 [US1] Add responsive dashboard breakpoint rules in app/static/css/site.css (AC: UI-AC-01, UI-AC-10)
- [X] T015 [P] [US1] Add dashboard rendering tests for remaining, exceeded, empty, and missing-target states in tests/test_ui.py (AC: UI-AC-02, UI-AC-03, UI-AC-04)

**Checkpoint**: User Story 1 provides a complete independently testable modern nutrition dashboard.

---

## Phase 4: User Story 2 - Record Meals in the Enhanced Form (Priority: P1)

**Goal**: Improve meal-entry usability while preserving validation and submission behavior.
**Independent Test**: Complete valid and invalid add/edit submissions at 320, 768, and 1280 pixels and verify existing persistence and navigation.

- [X] T016 [P] [US2] Wrap meal fields in a responsive form card in app/templates/meal_form.html (AC: UI-AC-05)
- [X] T017 [US2] Apply rounded reusable control classes to food, category, calories, protein, and date inputs in app/templates/meal_form.html (AC: UI-AC-05)
- [X] T018 [US2] Associate each existing meal validation message with its input using ARIA attributes in app/templates/meal_form.html (AC: UI-AC-06)
- [X] T019 [US2] Style invalid fields and associated validation messages in app/static/css/site.css (AC: UI-AC-06)
- [X] T020 [US2] Update primary Save Meal and secondary Cancel actions for modern consistent styling in app/templates/meal_form.html (AC: UI-AC-05, UI-AC-08)
- [X] T021 [US2] Apply the responsive form card and field spacing rules in app/static/css/site.css (AC: UI-AC-05, UI-AC-10)
- [X] T022 [US2] Apply consistent card, control, validation, and action styling to app/templates/targets.html (AC: UI-AC-05, UI-AC-06, UI-AC-09)
- [X] T023 [P] [US2] Add Flask template tests for meal validation styling and persisted valid add/edit behavior in tests/test_ui.py (AC: UI-AC-06, UI-AC-09)

**Checkpoint**: User Story 2 provides an independently testable modern meal and target form experience.

---

## Phase 5: User Story 3 - Review Meals by Category (Priority: P2)

**Goal**: Make recorded meals easy to scan in a responsive category-aware layout.
**Independent Test**: View all four categories with edit/delete actions at desktop and mobile widths and confirm accessible text, icons, and no clipping.

- [X] T024 [P] [US3] Add readable category text and lightweight Breakfast, Lunch, Dinner, and Snacks icons in app/templates/dashboard.html (AC: UI-AC-07, UI-AC-10)
- [X] T025 [US3] Add responsive meal-card markup for narrow viewports while retaining desktop table semantics in app/templates/dashboard.html (AC: UI-AC-07, UI-AC-10)
- [X] T026 [US3] Preserve existing edit and delete actions, URLs, confirmation, and delete form behavior in app/templates/dashboard.html (AC: UI-AC-09)
- [X] T027 [US3] Style category icons, meal cards, desktop table rows, numeric values, and actions in app/static/css/site.css (AC: UI-AC-07, UI-AC-08)
- [X] T028 [US3] Add subtle hover and focus transitions without layout shift to supported controls and meal rows in app/static/css/site.css (AC: UI-AC-08)
- [X] T029 [US3] Add narrow-screen meal layout rules and overflow containment in app/static/css/site.css (AC: UI-AC-07, UI-AC-10)
- [X] T030 [P] [US3] Add responsive meal-list rendering and action-preservation tests in tests/test_ui.py (AC: UI-AC-07, UI-AC-09, UI-AC-10)

**Checkpoint**: User Story 3 provides an independently testable category-aware responsive meal list.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Finish shared interactions and verify presentation does not regress existing behavior.

- [X] T031 [P] Add reduced-motion handling and keyboard-visible focus styles in app/static/css/site.css (AC: UI-AC-08, UI-AC-10)
- [X] T032 Style flash messages and the friendly error page consistently in app/templates/base.html and app/templates/error.html (AC: UI-AC-06, UI-AC-10)
- [X] T033 Verify the complete UI at 320, 768, and 1280 pixels and document the tested states in specs/002-modern-ui-enhancement/quickstart.md (AC: UI-AC-01, UI-AC-05, UI-AC-10)
- [X] T034 Run all existing Flask and pytest functionality tests and confirm no CRUD, persistence, target, or calculation regression in tests/ (AC: UI-AC-09)
- [X] T035 Verify remaining, exceeded, fully-met, empty, validation, category, hover, keyboard, and missing-target states against UI-AC-01 through UI-AC-10 in tests/test_ui.py and specs/002-modern-ui-enhancement/quickstart.md (AC: UI-AC-01, UI-AC-02, UI-AC-03, UI-AC-04, UI-AC-05, UI-AC-06, UI-AC-07, UI-AC-08, UI-AC-09, UI-AC-10)

---

## Dependencies & Execution Order

### Phase Dependencies

- Setup (Phase 1) has no dependencies and can start immediately.
- Foundational (Phase 2) depends on Setup and blocks all user-story work.
- User Story 1 (dashboard), User Story 2 (forms), and User Story 3 (meal listing) depend on Foundational and can proceed independently afterward.
- Polish (Phase 6) depends on all selected user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Independent; reuses existing dashboard template context.
- **User Story 2 (P1)**: Independent; preserves existing meal and target field names and routes.
- **User Story 3 (P2)**: Can share dashboard foundations from User Story 1, but remains independently testable.

## Parallel Opportunities

- T002 can run alongside setup work because it modifies only the stylesheet section structure.
- T006, T015, T016, T023, T024, and T030 are parallelizable within separate files or test additions.
- Dashboard, meal-form, and meal-list template work can be assigned independently after foundational styling exists.

## Parallel Example: User Story 1

```text
T006 summary-card wrapper in app/templates/dashboard.html
T010 progress status styles in app/static/css/site.css
T015 dashboard state tests in tests/test_ui.py
```

## Parallel Example: User Story 2

```text
T016 responsive form card in app/templates/meal_form.html
T019 validation styles in app/static/css/site.css
T023 form behavior and persistence tests in tests/test_ui.py
```

## Parallel Example: User Story 3

```text
T024 category icons in app/templates/dashboard.html
T027 meal presentation styles in app/static/css/site.css
T030 responsive meal-list tests in tests/test_ui.py
```

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phases 1-2.
2. Complete Phase 3: User Story 1.
3. Validate dashboard summary cards, progress states, empty state, and 320/768/1280 layouts.
4. Stop before other stories if the dashboard MVP is the delivery checkpoint.

### Incremental Delivery

1. Complete shared foundation.
2. Add the dashboard MVP.
3. Add meal and target form improvements.
4. Add category-aware responsive meal presentation.
5. Run responsive, automated regression, and quickstart validation.

## Format Validation

All tasks use the required `- [X] TNNN` checkbox format, include `[P]` only for parallelizable tasks, and use `[US1]`, `[US2]`, or `[US3]` only in user-story phases. Every implementation and verification task names its relevant UI acceptance criterion and exact affected file where applicable.
