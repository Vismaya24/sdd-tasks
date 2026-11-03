# UI Contract

## Presentation Contract

This enhancement does not alter Flask routes, request fields, response behavior, database operations,
or nutrition calculations. Existing templates must continue receiving the same values and actions.

## Dashboard

- Retain selected-date navigation, meal add/edit/delete actions, totals, targets, and text progress.
- Display a visual progress bar in addition to numeric and text status.
- Cap the displayed fill at 100 percent.
- Do not render a misleading progress bar when targets are missing.

## Meal Forms

- Retain existing field names and POST targets for add and edit operations.
- Preserve invalid-submission values and field-associated errors.
- Retain browser confirmation before deletion.

## Responsive States

- Support 320-, 768-, and 1280-pixel viewport widths.
- Keep primary actions and labels visible without horizontal scrolling.
- Keep category meaning in text when icons are decorative.
