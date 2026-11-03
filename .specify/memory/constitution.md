# Calorie and Nutrition Tracker Constitution

<!--
Sync Impact Report
- Version change: 1.0.0 -> 1.0.1
- Modified sections: target governance aligned with reusable daily target pair
- Modified principles: all placeholder principles -> project-specific principles
- Added sections: Data and Calculation Requirements; Development and Quality Workflow
- Removed sections: none
- Ratification status: pending mentor confirmation; no date is assigned in this version.
-->

## Core Principles

### I. Simplicity

The application MUST remain simple, user-friendly, and appropriate for a fundamentals-level
project. Features MUST prioritize the core meal tracking and progress workflows, and unnecessary
abstraction or complexity MUST be avoided.

### II. Accuracy

Calorie and protein calculations MUST be accurate. Daily totals MUST include every valid meal
entry exactly once, and progress calculations MUST compare actual totals against configured daily
targets without altering source values.

### III. Data Validation

Meal food names, calories, and protein values MUST be validated before they are accepted. Missing
values, negative nutrition values, malformed numbers, and other invalid input MUST be rejected
with clear guidance. Zero or boundary values MUST be handled explicitly and consistently.

### IV. Maintainability

Implementation MUST follow clean coding practices and maintain a clear, understandable project
structure. Responsibilities SHOULD be separated so that input handling, nutrition calculations,
data storage, and interface behavior can be reviewed and changed independently.

### V. Usability

The interface MUST make it simple to record breakfast, lunch, dinner, and snack entries and to
view daily calorie and protein progress. Labels, actions, and error messages MUST be concise,
consistent, and understandable without special knowledge.

### VI. Data Management

Meal records and daily calorie and protein targets MUST be stored and retrieved consistently.
Updates MUST preserve existing records, and read, write, and update operations MUST use a
predictable data format for daily summaries and targets.

### VII. Testing

Major functionalities MUST be validated with normal inputs, invalid inputs, boundary conditions,
and edge cases. Tests MUST cover meal recording, daily totals, target configuration, progress
comparisons, persistence, and expected error behavior.

### VIII. Error Handling

Unexpected situations MUST be handled gracefully without corrupting stored records or exposing
technical failure details. The application MUST display an appropriate, actionable message when
an operation cannot be completed.

## Data and Calculation Requirements

- Supported meal categories MUST be breakfast, lunch, dinner, and snacks.
- Meal entries MUST retain a food name, calorie value, and protein value.
- Daily summaries MUST calculate total calories and total protein from accepted meal entries.
- Users MUST be able to set and update one reusable daily calorie target and one reusable daily
  protein target that apply across all dates.
- Daily progress MUST show the relationship between actual intake and each configured target.

## Development and Quality Workflow

- Changes MUST preserve the core principles and documented application behavior.
- Implementation MUST be kept proportionate to the fundamentals-level scope of the project.
- New or changed functionality MUST include appropriate validation and automated tests before
  integration.
- Refactoring MUST not change established nutrition calculations or persisted data behavior
  without documented approval and migration or compatibility planning.

## Governance

This Constitution supersedes conflicting project practices. Amendments require a documented
change, approval by project maintainers, and an impact assessment for existing behavior and
templates. Every pull request and review MUST verify compliance with the principles and quality
requirements. Violations MUST be resolved or documented with a justified exception before merge.

- **MAJOR** version changes redefine or remove principles or governance requirements.
- **MINOR** version changes add principles, sections, or materially expand requirements.
- **PATCH** version changes clarify guidance, correct wording, or make other non-semantic
  refinements.

**Version**: 1.0.1 | **Ratified**: Pending mentor confirmation |
**Last Amended**: 2026-11-02
