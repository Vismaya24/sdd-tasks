# Quickstart

## Prerequisites

- Python 3.11 or newer
- Flask and pytest

## Setup

```text
python -m venv .venv
.venv\Scripts\activate
pip install flask pytest
python -m app
```

The first application start creates the SQLite database and required tables.

## Validation Scenarios

1. Open the dashboard and verify empty dates show zero calorie and protein totals.
2. Add a Breakfast meal of 500 kcal and 30 g protein and verify it appears once.
3. Add an identical Breakfast meal and verify it remains a separate record.
4. Edit the first meal to a different date and verify both date totals change.
5. Delete one meal and verify totals are recalculated.
6. Configure 2000 kcal and 100 g protein targets.
7. Verify actual intake of 1600 kcal and 75 g protein shows 400 kcal and 25 g remaining.
8. Verify actual intake above targets shows exceeded amounts without relying on color.
9. Submit invalid meal and target values and verify existing data is unchanged.
10. Restart the application and verify meals and targets remain available.

## Automated Tests

```text
pytest -q
```

Acceptance coverage includes AC-01 through AC-13, including decimal rounding, accessible text
progress, empty states, and operation failure integrity.
