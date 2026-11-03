from decimal import Decimal

from app.models import get_meal, get_targets, insert_meal, save_targets


def test_restart_persistence(app):
    insert_meal(app.config["DATABASE"], {
        "food_name": "Persistent oats", "category": "Breakfast", "calories": Decimal("300"),
        "protein": Decimal("10"), "meal_date": "2026-11-02",
    })
    save_targets(app.config["DATABASE"], Decimal("2000"), Decimal("100"))
    assert get_meal(app.config["DATABASE"], 1)["food_name"] == "Persistent oats"
    assert get_targets(app.config["DATABASE"])["calorie_target"] == Decimal("2000")
