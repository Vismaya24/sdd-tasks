# Feature Specification: Nutrition Tracker

**Feature Branch**: `001-nutrition-tracker`

**Created**: 2026-11-02

**Status**: Draft

**Input**: User description: "Calorie and Nutrition Tracker with manual meal entry, daily totals, targets, and progress comparison."

## Project Overview

The Calorie and Nutrition Tracker is a fundamentals-level application for manually recording
meals and monitoring daily calorie and protein intake. The product prioritizes accurate totals,
clear validation, editable records, and straightforward progress feedback.

## Clarifications

### Session 2026-11-02

- Q: How should decimal nutrition values be formatted? → A: Accept calorie and protein values with up to two decimal places, retain precision for calculation, and display totals and differences with no more than two decimal places.
- Q: Should identical meals be treated as separate entries? → A: Yes, allow identical entries as separate records.
- Q: How should progress be conveyed without color? → A: Use text labels and numeric amounts with optional color.

## Target Users

- Individuals who want to monitor daily calorie and protein intake.
- Beginners who want a simple nutrition tracking tool suitable for academic or learning use.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Record and Review Meals (Priority: P1)

A user selects a date, adds meals for breakfast, lunch, dinner, or snacks, and reviews the meals
recorded for that date.

**Why this priority**: Meal recording is the core value of the application.

**Independent Test**: A user can add valid meals, view the selected day's meal list, and see the
correct meal details without configuring targets or other features.

**Acceptance Scenarios**:

1. **Given** the user is on a selected date, **When** valid food name, category, calories, protein,
   and date are submitted, **Then** the meal appears in that date's record list.
2. **Given** no meals exist for a selected date, **When** the user opens the date, **Then** the
   application displays an empty-record message and zero intake totals.
3. **Given** required or numeric fields are invalid, **When** the user submits the meal, **Then**
   the meal is not saved and clear field-specific messages are shown.

---

### User Story 2 - Maintain Recorded Meals (Priority: P1)

A user views, edits, and deletes incorrect or outdated meals so the daily record remains accurate.

**Why this priority**: Corrections must be possible for the nutrition totals to remain trustworthy.

**Independent Test**: A meal can be changed and deleted, with totals recalculated after each
operation.

**Acceptance Scenarios**:

1. **Given** an existing meal, **When** the user changes its details and saves valid values, **Then**
   the meal is updated and daily totals are recalculated.
2. **Given** an existing meal, **When** the user confirms deletion, **Then** the meal is removed
   and daily totals are recalculated.
3. **Given** the last meal is deleted, **When** the update completes, **Then** the date shows zero
   intake and an appropriate empty-record message.

---

### User Story 3 - Set Targets and Review Progress (Priority: P1)

A user sets calorie and protein targets and compares intake with those targets for a selected date.

**Why this priority**: Targets and progress convert recorded meals into actionable daily feedback.

**Independent Test**: Valid targets can be configured and intake progress can be viewed with
remaining or exceeded amounts.

**Acceptance Scenarios**:

1. **Given** no targets are configured, **When** the user views progress, **Then** the application
   explains that targets are missing and does not present misleading progress.
2. **Given** positive calorie and protein targets, **When** the user saves them, **Then** the daily
   progress displays actual intake, target, and remaining or exceeded amounts.
3. **Given** intake exceeds either target, **When** progress is displayed, **Then** the exceeded
   amount is shown clearly and no negative remaining amount is presented as remaining.
4. **Given** a reusable pair of targets, **When** the user changes either target, **Then** progress
   for the selected and other dates uses the updated pair.

### Edge Cases

- A food name containing only whitespace is rejected.
- Calories and protein equal to zero are accepted.
- Negative calories, negative protein, blank required values, and nonnumeric values are rejected.
- A target of zero, a negative target, or a nonnumeric target is rejected.
- Decimal calorie and protein values are supported.
- Totals may exceed targets.
- A valid date format and calendar date are required.
- An operation failure or unexpected situation displays a user-friendly error without losing existing
  meal records.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST allow a user to create a meal with a food name, meal category, calories,
  protein, and date.
- **FR-001a**: The system MUST allow multiple meals with identical food, category, nutrition values,
  and date to be stored as separate records.
- **FR-002**: The system MUST restrict meal category to Breakfast, Lunch, Dinner, or Snacks.
- **FR-003**: The system MUST require a non-whitespace food name and meal category.
- **FR-004**: The system MUST require calories and protein to be non-negative numeric values.
- **FR-005**: The system MUST require a valid calendar date for each meal.
- **FR-006**: The system MUST reject invalid meal submissions and identify each invalid field without
  saving the meal.
- **FR-007**: The system MUST display meals recorded for a user-selected date.
- **FR-008**: The system MUST allow a user to edit every meal field, including date; moving a meal to
  another date MUST update both affected daily totals.
- **FR-009**: The system MUST allow a user to delete an existing meal after clear confirmation.
- **FR-010**: The system MUST calculate and display calorie and protein totals for the selected date.
- **FR-011**: The system MUST recalculate daily totals immediately after meals are added, edited, or
  deleted.
- **FR-012**: The system MUST allow one reusable pair of positive daily calorie and protein targets
  to be set and updated.
- **FR-013**: The system MUST compare actual intake with the configured calorie and protein targets.
- **FR-014**: The system MUST display remaining amounts when intake is below a target and exceeded
  amounts when intake exceeds a target.
- **FR-015**: The system MUST provide simple, understandable progress indicators for calories and
  protein.
- **FR-015a**: Progress indicators MUST include text labels and numeric amounts; color MUST NOT be
  the only way to communicate progress status.
- **FR-016**: The system MUST display zero totals and an empty-record message when a selected date
  has no meals.
- **FR-017**: The system MUST display a clear missing-target message when targets have not been set.
- **FR-018**: The system MUST display clear validation and operation error messages without exposing
  technical implementation details.
- **FR-019**: The system MUST retain meal records and targets consistently when the application is
  reopened during normal operation.

### Non-Functional Requirements

- **NFR-001**: Primary meal-recording, editing, deletion, target-setting, and progress-viewing tasks
  MUST be understandable to a beginner without training.
- **NFR-002**: A valid meal submission MUST be completed in no more than three user actions after
  opening the meal form, excluding data entry.
- **NFR-003**: Nutrition totals and progress shown after a data change MUST be accurate for every
  meal date represented in the current view.
- **NFR-004**: Validation messages MUST identify the affected field and the required correction.
- **NFR-005**: Empty, invalid-input, missing-target, and operation-failure states MUST be presented
  without corruption of existing records.
- **NFR-006**: The application MUST remain suitable for a fundamentals-level project, with no
  authentication, external food database, barcode scanning, AI recommendation, or third-party
  nutrition integration.
- **NFR-007**: Progress status MUST remain understandable when color is unavailable or not
  distinguishable because the status and amounts MUST be presented in text.

### Business Rules

- BR-001: Meal category is required and limited to Breakfast, Lunch, Dinner, and Snacks.
- BR-002: Food name is required and cannot contain only whitespace.
- BR-003: Calories and protein MUST be non-negative decimal numbers with up to two decimal places
  and MUST include zero as a valid value.
- BR-003a: Stored values MUST retain their entered precision for calculations. Displayed calorie
  and protein totals MUST be rounded to no more than two decimal places.
- BR-004: Daily calorie and protein targets MUST be greater than zero.
- BR-005: Daily totals are the sum of accepted meals for the selected calendar date.
- BR-006: Remaining amount is target minus actual intake when actual intake is less than target.
- BR-007: Exceeded amount is actual intake minus target when actual intake is greater than target.
- BR-008: Actual intake equal to a target is neither remaining nor exceeded and MUST be displayed
  as fully met.
- BR-009: Targets are one reusable pair for the application and are applied to progress for every
  selected date.
- BR-010: Invalid meals and invalid target values are not saved and do not affect existing totals.

### Key Entities *(include if feature involves data)*

- **Meal**: Food name, meal category, calories, protein, and date; belongs to one date record.
  Identical meal values MUST not be merged or deduplicated and each record MUST have its own edit
  and delete target.
- **Daily Nutrition Target**: Reusable positive calorie target and reusable positive protein target.
- **Daily Nutrition Summary**: Calculated calorie total, protein total, target comparisons, remaining
  amount, and exceeded amount for a selected date.

## Acceptance Criteria

- **AC-01**: Given a selected date, when a meal with all required valid fields is submitted, then
  exactly one meal is saved under that date and category.
- **AC-02**: Given valid meals totaling 500 calories and 30 grams of protein, when their date is
  viewed, then both daily totals equal the stated values.
- **AC-02a**: Given decimal meal values whose calculated total contains more than two decimal
  places, when the daily total is displayed, then the value is displayed with no more than two decimal places without
  changing the stored inputs used for subsequent calculations.
- **AC-03**: Given missing or whitespace food name, unsupported category, negative or nonnumeric
  nutrition values, or invalid date, when submitted, then no meal is saved and clear field-specific
  errors appear.
- **AC-04**: Given a valid meal, when its food name, category, calories, protein, or date is edited
  and saved, then the meal and all affected daily totals update consistently.
- **AC-05**: Given an existing meal, when deletion is confirmed, then the meal is removed and its
  nutrition values no longer contribute to any total.
- **AC-06**: Given targets of 2000 calories and 100 grams of protein, when actual intake is 1600
  calories and 75 grams of protein, then progress shows 400 calories remaining and 25 grams remaining.
- **AC-07**: Given targets of 2000 calories and 100 grams of protein, when actual intake is 2200
  calories and 120 grams of protein, then progress shows 200 calories exceeded and 20 grams exceeded.
- **AC-08**: Given actual intake exactly equal to a target, when progress is viewed, then the
  application indicates that the target is fully met with no remaining or exceeded amount.
- **AC-08a**: Given progress is displayed without color, when intake is remaining, exceeded, or
  fully met, then the status is communicated through readable text and numeric amounts.
- **AC-09**: Given zero or negative targets or nonnumeric targets, when submitted, then no target
  is saved and clear field-specific errors appear.
- **AC-10**: Given a date with no meals, when it is viewed, then totals are zero and an empty-record
  message is displayed.
- **AC-11**: Given targets have not been configured, when progress is viewed, then a missing-target
  message is displayed and totals remain visible.
- **AC-12**: Given a user updates targets, when any date is viewed afterward, then its progress uses
  the updated reusable targets.
- **AC-13**: Given a meal or target operation fails unexpectedly, when the failure is handled, then
  existing records remain intact and a user-friendly error is displayed.

## Constraints

- The application MUST focus only on calorie and protein tracking.
- Meal nutrition details MUST be entered manually.
- Authentication, barcode scanning, AI recommendations, external food databases, and third-party
  nutrition integrations are excluded.
- The feature MUST remain simple and suitable for a fundamentals-level project.
- Calorie values are measured in kcal and protein values in grams.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: At least 95% of test users can record a complete meal and find the saved record on the
  first attempt without assistance.
- **SC-002**: At least 95% of test users can edit or delete a meal and verify the updated daily
  totals without assistance.
- **SC-003**: At least 95% of daily total and progress calculations in representative test cases
  match expected values exactly.
- **SC-004**: All tested invalid meal and target submissions produce a clear, field-specific message
  without changing existing data.
- **SC-005**: At least 90% of representative beginner users report that the meal, target, and progress
  workflows are understandable.

## Assumptions

- Calories are entered in kcal and protein is entered in grams; these units are displayed beside
  their values.
- A calendar date can be selected for viewing and entering meals.
- Confirm-before-delete behavior is used because it prevents accidental removal of records.
- Daily targets are one reusable pair rather than date-specific values.
- Unexpected operation failures are recoverable locally and do not require administrator intervention.
