# Route Contracts

## `GET /`

Optional query parameter: `date=YYYY-MM-DD`.

Renders meals, totals, targets, and progress for the selected date. It defaults to the current date.

## `GET /meals/new`

Optional query parameter: `date=YYYY-MM-DD`.

Renders the meal form with the selected date.

## `POST /meals`

Fields: `food_name`, `category`, `calories`, `protein`, and `meal_date`.

Valid input inserts one meal and redirects to that date. Invalid input renders field errors and
preserves entered values.

## `GET /meals/<meal_id>/edit`

Renders the existing meal values.

## `POST /meals/<meal_id>/edit`

Accepts the meal creation fields. Valid input updates every field in one transaction. Invalid input
renders errors without changing the record.

## `POST /meals/<meal_id>/delete`

Deletes one record after browser confirmation and redirects to its date.

## `GET /targets`

Renders configured reusable targets or empty target fields.

## `POST /targets`

Fields: `calorie_target` and `protein_target`.

Valid positive values upsert settings row `id = 1`. Invalid values render field errors without
changing existing targets.

## HTTP Error Behavior

- Validation errors remain beside the relevant fields.
- Unknown meals produce a clear not-found page and return action.
- Missing targets are a normal dashboard state.
- Unexpected database failures are logged and shown as a friendly operation error.
