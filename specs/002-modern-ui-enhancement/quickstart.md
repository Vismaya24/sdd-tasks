# UI Enhancement Quickstart

## Prerequisites

- Existing Flask application dependencies installed.
- SQLite database available through normal startup.

## Run

```text
python -m pip install -r requirements.txt
python -m app
```

Open `http://127.0.0.1:5000`.

## Browser Validation

1. Configure calorie and protein targets.
2. Add meals representing remaining, fully-met, and exceeded states.
3. Verify 320-, 768-, and 1280-pixel layouts.
4. Confirm cards, bars, statuses, empty states, and actions have no horizontal clipping.
5. Submit invalid meal and target values and verify field errors without data corruption.
6. Edit and delete meals and verify existing totals, navigation, and confirmations.
7. Verify the dashboard, form, meal cards, validation states, and navigation are rendered
   consistently without horizontal overflow at 320, 768, and 1280 pixels.
8. Verify remaining, exceeded, fully-met, empty-record, and missing-target states retain their
   existing numeric values while presenting accessible text status.

## Automated Validation

```text
python -m pytest -q
```

All existing tests must pass without backend or route changes.
