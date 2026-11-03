from decimal import Decimal, ROUND_HALF_UP

from .models import decimal_value, list_meals

ZERO = Decimal("0")


def format_value(value):
    number = decimal_value(value if value is not None else ZERO)
    rounded = number.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return format(rounded, "f").rstrip("0").rstrip(".") if rounded != rounded.to_integral() else format(rounded.quantize(Decimal("1")), "f")


def daily_totals(database, meal_date):
    meals = list_meals(database, meal_date)
    calories = sum((decimal_value(meal["calories"]) for meal in meals), ZERO)
    protein = sum((decimal_value(meal["protein"]) for meal in meals), ZERO)
    return calories, protein


def progress(actual, target):
    actual = decimal_value(actual)
    target = decimal_value(target)
    percentage = actual / target * 100 if target != ZERO else ZERO
    if actual < target:
        return "Remaining", target - actual, percentage
    if actual > target:
        return "Exceeded", actual - target, percentage
    return "Fully met", ZERO, percentage
