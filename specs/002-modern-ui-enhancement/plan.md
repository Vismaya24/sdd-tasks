# Implementation Plan: Modern UI Enhancement

**Branch**: `002-modern-ui-enhancement` | **Date**: 2026-11-02 | **Spec**: [spec.md](./spec.md)

## Summary

Enhance the existing Flask application's presentation through responsive Bootstrap layouts,
sage-green reusable styles, clear summary cards, accessible progress bars, meal-category
presentation, improved forms, empty states, and validation styling. Backend routes, SQLite schema,
CRUD behavior, and nutrition calculations remain unchanged.

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**: Flask, HTML, Bootstrap 5, pytest

**Storage**: Existing SQLite database; no schema changes

**Testing**: pytest and Flask test client, plus manual viewport verification

**Target Platform**: Desktop, tablet, and mobile web browsers

**Project Type**: Server-rendered Flask web application

**Performance Goals**: Ordinary local page loads and form submissions under two seconds

**Constraints**: Presentation changes only; no new dependencies, API behavior, or data entities

**Scale/Scope**: Existing single-user fundamentals-level application

## Constitution Check

Pass. The enhancement preserves simplicity, accuracy, validation, maintainability, usability, data
management, testing, and graceful error handling. Presentation changes will not alter nutrition
calculations or persisted behavior.

## Project Structure

### Documentation

```text
specs/002-modern-ui-enhancement/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```

### Source Code

```text
app/
├── static/
│   └── css/
│       └── site.css
└── templates/
    ├── base.html
    ├── dashboard.html
    ├── meal_form.html
    ├── targets.html
    └── error.html

tests/
```

**Structure Decision**: Keep the existing server-rendered Flask structure. Modify the shared
templates and `app/static/css/site.css`; use existing template context rather than adding JavaScript,
frontend components, routes, or backend state.

## Component Plan

- **base.html**: Modern navigation, sage-green branding, reusable page spacing, flash-message
  styling, and responsive Bootstrap shell.
- **dashboard.html**: Responsive date controls, calorie/protein summary cards, accessible progress
  bars, remaining/exceeded/fully-met text, meal presentation, category icons, empty state, and actions.
- **meal_form.html and targets.html**: Rounded controls, consistent form-card spacing, modern buttons,
  field-associated validation states, and responsive stacking.
- **error.html**: Friendly error presentation consistent with the application palette.
- **site.css**: CSS custom properties for palette and spacing, reusable card/button/form classes,
  progress status classes, responsive breakpoints, hover/focus states, transitions, and reduced-motion
  support.

## CSS Organization

Keep styling in the existing `app/static/css/site.css` with sections for:

1. Theme variables and base element styles.
2. Shared layout and navigation.
3. Buttons, cards, and summary components.
4. Nutrition progress and status states.
5. Meal presentation and category icons.
6. Forms and validation.
7. Empty and error states.
8. Responsive breakpoints and reduced-motion fallback.

Use Bootstrap utilities for layout and spacing where concise. Add custom classes only for repeated
visual patterns or nutrition-specific states.

## Responsive Approach

- Use Bootstrap containers, grid, flex, and responsive utilities.
- Show summary cards in two columns at medium and larger widths, and stack them below.
- Use a card-like layout for meals at narrow widths while retaining the desktop table.
- Preserve labels, text, category meaning, and actions at 320 pixels without horizontal scrolling.
- Use wrapping and overflow safeguards instead of fixed content widths.
- Apply transitions to color, background, border, and transform properties.
- Respect reduced-motion preferences with `prefers-reduced-motion`.

## Implementation Sequence

1. Establish theme variables, base styles, reusable cards, buttons, and form control styling.
2. Enhance the shared navigation and responsive page shell.
3. Update dashboard summary cards and accessible progress bars from existing values.
4. Update meal presentation and category icons while preserving edit/delete actions.
5. Improve meal and target forms, validation styling, and empty/error states.
6. Verify 320-, 768-, and 1280-pixel layouts and run existing Flask tests.

No route, model, database, or calculation changes are planned.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | UI-only enhancement | No additional architecture is necessary |
