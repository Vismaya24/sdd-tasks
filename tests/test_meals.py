

VALID_MEAL = {
    "food_name": "Eggs",
    "category": "Breakfast",
    "calories": "200",
    "protein": "12.5",
    "meal_date": "2026-11-02",
}


def test_create_duplicate_meals(client):
    assert client.post("/meals", data=VALID_MEAL).status_code == 302
    assert client.post("/meals", data=VALID_MEAL).status_code == 302
    response = client.get("/?date=2026-11-02")
    assert response.data.count(b"Eggs") >= 2


def test_empty_date(client):
    response = client.get("/?date=2026-11-03")
    assert b"No meals recorded" in response.data
    assert b"0 kcal" in response.data


def test_invalid_meal_does_not_save(client):
    invalid = dict(VALID_MEAL, food_name="   ", calories="-1", category="Dessert")
    response = client.post("/meals", data=invalid)
    assert response.status_code == 400
    assert b"Food name is required" in response.data
    assert client.get("/?date=2026-11-02").data.count(b"Eggs") == 0


def test_edit_move_and_delete(client):
    client.post("/meals", data=VALID_MEAL)
    source = client.get("/?date=2026-11-02").data
    assert b"Eggs" in source
    response = client.post("/meals/1/edit", data=dict(VALID_MEAL, meal_date="2026-11-03"))
    assert response.status_code == 302
    assert b"Eggs" in client.get("/?date=2026-11-03").data
    assert b"No meals recorded" in client.get("/?date=2026-11-02").data
    assert client.post("/meals/1/delete").status_code == 302
    assert b"Eggs" not in client.get("/?date=2026-11-03").data
