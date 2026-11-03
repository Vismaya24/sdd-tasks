# Data Model

No persistent data or database schema changes are required.

## Existing Presentation Inputs

### Meal

Rendered fields remain `food_name`, `category`, `calories`, `protein`, and `meal_date`.

Presentation controls only determine grouping, category symbol, responsive layout, and visual state.
Meal records remain individually stored and editable.

### Nutrition Target

The existing reusable calorie and protein pair supplies summary-card target values.

No target entity is added.

### Derived Daily Summary

Existing server-provided totals and progress status remain unchanged.

Template presentation may derive a visual fill percentage from actual and target values and must cap
the fill at 100 percent.
