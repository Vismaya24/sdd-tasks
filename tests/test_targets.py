from decimal import Decimal

from app.models import get_targets, insert_meal


def test_missing_and_exceeded_targets(client, app):
    response = client.get("/?date=2026-11-02")
    assert b"Targets not set" in response.data

    assert client.post("/targets", data={"calorie_target": "2000", "protein_target": "100"}).status_code == 302
    insert_meal(app.config["DATABASE"], {
        "food_name": "Large meal", "category": "Dinner", "calories": Decimal("2200"),
        "protein": Decimal("120"), "meal_date": "2026-11-02",
    })
    response = client.get("/?date=2026-11-02")
    assert b"Exceeded" in response.data
    assert b"200 kcal" in response.data


def test_invalid_targets_do_not_replace_existing(client, app):
    client.post("/targets", data={"calorie_target": "2000", "protein_target": "100"})
    response = client.post("/targets", data={"calorie_target": "0", "protein_target": "-1"})
    assert response.status_code == 400
    targets = get_targets(app.config["DATABASE"])
    assert targets["calorie_target"] == Decimal("2000")
    assert targets["protein_target"] == Decimal("100")
