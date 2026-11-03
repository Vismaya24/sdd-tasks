# Data Model

## meals

| Field | Type | Constraints | Purpose |
|---|---|---|---|
| id | INTEGER | Primary key | Stable edit and delete target |
| food_name | TEXT | Trimmed, 1-120 characters | Meal name |
| category | TEXT | Breakfast, Lunch, Dinner, or Snacks | Meal category |
| calories | NUMERIC | Non-negative finite decimal | Calories in kcal |
| protein | NUMERIC | Non-negative finite decimal | Protein in grams |
| meal_date | TEXT | Valid ISO YYYY-MM-DD date | Date grouping key |
| created_at | TEXT | Not null | Creation timestamp |

Every row is independently editable and deletable. Identical records are not merged.

## nutrition_targets

Use one settings row with primary key `id = 1`.

| Field | Type | Constraints | Purpose |
|---|---|---|---|
| id | INTEGER | Primary key, fixed value 1 | Single reusable settings row |
| calorie_target | NUMERIC | Positive finite decimal | Reusable calorie target |
| protein_target | NUMERIC | Positive finite decimal | Reusable protein target |
| updated_at | TEXT | Not null | Last update timestamp |

The row is absent until targets are configured. Target updates reuse this row for every date.

## Daily Nutrition Summary

Calculated, not stored:

- Actual calories: sum of `calories` for the selected date.
- Actual protein: sum of `protein` for the selected date.
- Remaining: target minus actual, when actual is lower than target.
- Exceeded: actual minus target, when actual is higher than target.
- Fully Met: actual is equal to target.

Stored precision is retained for calculations. Displayed values are rounded to two decimal places.

## Validation Rules

- Reject blank or whitespace-only food names.
- Reject negative, infinite, malformed, or missing nutrition values.
- Accept zero calories and protein.
- Reject unsupported categories and invalid calendar dates.
- Require positive calorie and protein targets.
- Database changes occur only after complete validation succeeds.
