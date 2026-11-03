# Research

## Web Stack

- **Decision:** Use Flask server-rendered pages, Bootstrap 5, SQLite, and direct parameterized SQL.
- **Rationale:** This matches the requested stack and keeps setup suitable for a fundamentals project.
- **Alternatives considered:** A separate API frontend was rejected because it adds build and routing
  coordination without additional user value.

## Numeric Accuracy

- **Decision:** Parse validated input as Decimal, retain entered precision for stored values and
  calculations, and round only displayed totals to two decimal places.
- **Rationale:** Decimal arithmetic avoids binary floating-point surprises and implements the
  clarified specification rule.
- **Alternatives considered:** Float arithmetic is less reliable, while integer scaling adds needless
  conversion logic.

## Storage

- **Decision:** Use SQLite and direct SQL through one connection helper rather than an ORM or repository
  framework.
- **Rationale:** It is simple, persistent, and supports parameterized CRUD.
- **Alternatives considered:** SQLAlchemy improves portability but exceeds the required assignment scope.

## Progress Calculation

- **Decision:** Calculate totals and comparisons on demand. Show remaining, exceeded, or fully-met
  status using text and numeric values; color is optional.
- **Rationale:** Derived summaries avoid stale stored totals and satisfy the clarified accessibility
  requirement.
- **Alternatives considered:** Persisted daily totals would duplicate source values and require
  synchronization on every CRUD operation.

## Targets

- **Decision:** Store one reusable settings row containing the calorie and protein targets.
- **Rationale:** This implements the clarified reusable target scope.
- **Alternatives considered:** Date-specific targets were explicitly not selected.
