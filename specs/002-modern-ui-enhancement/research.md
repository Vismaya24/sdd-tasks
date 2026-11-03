# Research: Modern UI Enhancement

## Decision: Reuse Existing Server-Rendered Bootstrap

Use Flask-rendered templates and Bootstrap utilities, with enhancement-specific styling in the
existing `site.css`.

This keeps setup and implementation simple. JavaScript frameworks and separate frontend builds
would duplicate routing and state without user value.

## Decision: Text-Based Accessible Progress

Render Bootstrap progress bars from existing actual and target values while retaining the existing
Remaining, Exceeded, Fully met text and numeric status.

The visual fill must be capped at 100 percent; exceeded amounts remain numeric text. No calculation,
route, or persistence changes are required.

## Decision: Lightweight Category Presentation

Map the existing category names to a small icon or symbol and readable text directly in templates.

This avoids a new icon dependency, database field, or migration. A custom icon package or remote icon
API would add unnecessary coupling.

## Decision: Responsive Bootstrap Grid

Use Bootstrap breakpoints and utilities, with CSS only for repeated visual classes and narrow-screen
meal presentation.

Fixed-width layouts and custom JavaScript layout switching were rejected because they would add
complexity and unnecessary behavior.
