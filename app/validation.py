from datetime import datetime
from decimal import Decimal, InvalidOperation

CATEGORIES = ("Breakfast", "Lunch", "Dinner", "Snacks")


def validate_required_name(value):
    value = (value or "").strip()
    if not value:
        return None, "Food name is required."
    if len(value) > 120:
        return None, "Food name must be 120 characters or fewer."
    return value, None


def validate_category(value):
    if value not in CATEGORIES:
        return None, "Choose Breakfast, Lunch, Dinner, or Snacks."
    return value, None


def validate_decimal(value, field_name, allow_zero=True):
    try:
        number = Decimal((value or "").strip())
    except (InvalidOperation, AttributeError):
        return None, f"{field_name} must be a number."
    if not number.is_finite():
        return None, f"{field_name} must be a finite number."
    if number < 0:
        return None, f"{field_name} cannot be negative."
    if not allow_zero and number == 0:
        return None, f"{field_name} must be greater than zero."
    if number.as_tuple().exponent < -2:
        return None, f"{field_name} can have no more than two decimal places."
    return number, None


def validate_date(value):
    try:
        parsed = datetime.strptime((value or "").strip(), "%Y-%m-%d")
        if parsed.strftime("%Y-%m-%d") != value.strip():
            raise ValueError
        return parsed.strftime("%Y-%m-%d"), None
    except (AttributeError, ValueError):
        return None, "Enter a valid date in YYYY-MM-DD format."
