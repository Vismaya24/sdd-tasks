from decimal import Decimal

from app.validation import validate_decimal, validate_required_name, validate_category, validate_date


def test_required_name_and_category_validation():
    assert validate_required_name("  Eggs  ")[0] == "Eggs"
    assert validate_required_name("   ")[1]
    assert validate_category("Breakfast")[0] == "Breakfast"
    assert validate_category("Dessert")[1]


def test_numeric_boundaries():
    assert validate_decimal("0", "Calories")[0] == 0
    assert validate_decimal("-0.01", "Calories")[1]
    assert validate_decimal("NaN", "Calories")[1]
    assert validate_decimal("Infinity", "Calories")[1]
    assert validate_decimal("1.001", "Calories")[1]
    assert validate_decimal("0", "Calories", allow_zero=False)[1]
    assert validate_decimal("1.23", "Calories", allow_zero=False)[0] == Decimal("1.23")


def test_date_validation():
    assert validate_date("2026-11-02")[0] == "2026-11-02"
    assert validate_date("2026-02-30")[1]
