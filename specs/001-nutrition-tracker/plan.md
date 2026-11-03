# Implementation Plan: Nutrition Tracker

**Branch**: `001-nutrition-tracker` | **Date**: 2026-11-02 | **Spec**: [spec.md](./spec.md)

## Summary

Build a single Flask application with server-rendered HTML and Bootstrap. SQLite stores meal
records and one reusable pair of nutrition targets. Flask routes validate form input, call small
service functions for totals and progress, and render templates with clear errors.

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**: Flask; HTML, CSS, and Bootstrap 5

**Storage**: SQLite

**Testing**: pytest and Flask test client

**Target Platform**: Local web browser on a Python-capable workstation

**Project Type**: Server-rendered web application

**Performance Goals**: Complete ordinary local interactions in under two seconds

**Constraints**: Fundamentals-level scope; no authentication or external services

**Scale/Scope**: Single local user and small meal history

## Constitution Check

Passed before design:

- **Simplicity:** A single Flask package and direct SQLite access are sufficient.
- **Accuracy:** Decimal arithmetic is used for totals and target differences.
- **Data Validation:** Meal and target fields are validated before persistence.
- **Maintainability:** Routes, validation, database access, calculations, and templates are separate.
- **Usability:** Bootstrap pages use concise labels, inline errors, and text-based progress.
- **Data Management:** Transactional SQLite writes preserve consistent records.
- **Testing:** Tests cover valid, invalid, boundary, and failure cases.
- **Error Handling:** Validation and operation failures are communicated without technical details.

Post-design review: All design artifacts comply with the constitution.

## Project Structure

### Documentation

```text
specs/001-nutrition-tracker/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── routes.md
└── tasks.md
```

### Source Code

```text
app/
├── __init__.py
├── db.py
├── models.py
├── validation.py
├── nutrition.py
├── routes.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── meal_form.html
│   └── targets.html
└── static/
    └── css/site.css

tests/
├── test_meals.py
├── test_targets.py
├── test_nutrition.py
└── test_validation.py

requirements.txt
```

**Structure Decision**: Use one application package with direct SQLite helpers and server-rendered
templates. This is maintainable for a fundamentals-level project without a repository or service framework.

## Application Components

- **Database module:** Opens SQLite connections, creates tables, and supplies transaction helpers.
- **Models module:** Defines simple row conversion and database CRUD operations.
- **Validation module:** Parses calendar dates and non-negative positive Decimal values; returns
  field-specific errors without writing data.
- **Nutrition module:** Calculates daily totals and remaining, exceeded, or fully-met status.
- **Routes module:** Handles dashboard, meal CRUD, and target settings requests.
- **Templates:** Render data-entry forms, errors, meal lists, totals, targets, and progress.

## Processing Flows

### Add Meal

1. Render a form preselected with the active dashboard date.
2. Parse every field and return field errors when any value is invalid.
3. Insert the meal in one transaction only when validation passes.
4. Redirect to the dashboard for the meal date and display confirmation.

### Edit Meal

1. Load the existing meal by primary key.
2. Validate submitted values using the same rules as meal creation.
3. Update all meal fields in one transaction.
4. Recalculate totals when the dashboard reloads, including totals for changed source and destination
   dates.

### Delete Meal

1. Confirm deletion in the browser.
2. Delete by primary key within a transaction.
3. Redirect to the meal's date and show recalculated totals.

### Daily Summary

1. Query meals whose meal date equals the selected date.
2. Sum calories and protein with Decimal arithmetic.
3. Query the reusable target row, if present.
4. Compare actual intake with each target and derive remaining, exceeded, or fully met text.
5. Round displayed totals and differences to no more than two decimal places.

## Input Validation and Error Handling

- Required strings are trimmed and checked for non-whitespace content.
- Meal categories are limited to Breakfast, Lunch, Dinner, and Snacks.
- Calories and protein accept finite non-negative Decimals; zero is valid.
- Targets accept finite positive Decimals; zero and negative values are invalid.
- Dates must be real ISO `YYYY-MM-DD` calendar dates.
- Duplicate nutrition values create separate rows; rows are not deduplicated.
- Expected validation errors remain next to their fields.
- Database errors roll back the current transaction, are logged, and display a generic friendly
  message.

## Testing Approach

- Unit tests for exact decimal totals, up-to-two-decimal formatting, remaining, exceeded, fully-met
  calculations, and progress percentages.
- Validation tests for missing fields, whitespace, unsupported categories, negatives, zero, malformed
  decimals, invalid dates, and finite-number limits.
- Flask client tests for add, list, edit, move-date, delete, and empty states.
- Target tests for missing targets, positive values, invalid updates, and reuse across dates.
- Persistence tests confirm records survive normal application restart.
- Each failed operation test confirms existing data is unchanged.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | All constitution gates pass | No alternative required |
