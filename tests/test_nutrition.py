from decimal import Decimal

from app.models import insert_meal
from app.nutrition import daily_totals, format_value, progress


def test_daily_totals(app):
    insert_meal(app.config["DATABASE"], {
        "food_name": "Oats", "category": "Breakfast", "calories": Decimal("125.5"),
        "protein": Decimal("4.25"), "meal_date": "2026-11-02",
    })
    insert_meal(app.config["DATABASE"], {
        "food_name": "Apple", "category": "Snacks", "calories": Decimal("75.25"),
        "protein": Decimal("0.25"), "meal_date": "2026-11-02",
    })
    calories, protein = daily_totals(app.config["DATABASE"], "2026-11-02")
    assert calories == Decimal("200.75")
    assert protein == Decimal("4.50")


def test_progress_percentages_and_status():
    assert progress(Decimal("800"), Decimal("1000"))[:2] == ("Remaining", Decimal("200"))
    assert progress(Decimal("800"), Decimal("1000"))[2] == Decimal("80")
    assert progress(Decimal("1000"), Decimal("1000"))[:2] == ("Fully met", Decimal("0"))
    assert progress(Decimal("1000"), Decimal("1000"))[2] == Decimal("100")
    assert progress(Decimal("1200"), Decimal("1000"))[:2] == ("Exceeded", Decimal("200"))
    assert progress(Decimal("1200"), Decimal("1000"))[2] == Decimal("120")


def test_up_to_two_decimal_formatting():
    assert format_value(Decimal("200")) == "200"
    assert format_value(Decimal("200.5")) == "200.5"
    assert format_value(Decimal("200.50")) == "200.5"
