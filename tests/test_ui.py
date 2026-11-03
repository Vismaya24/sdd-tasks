from app.models import save_targets, insert_meal


VALID_MEAL = {
    "food_name": "Oats",
    "category": "Breakfast",
    "calories": "200",
    "protein": "12.5",
    "meal_date": "2026-11-02",
}


def test_dashboard_empty_state_and_missing_targets(client, app):
    response = client.get("/?date=2026-11-03")

    assert response.status_code == 200
    assert b"No meals recorded yet" in response.data
    assert b"Targets not set" in response.data
    assert b'role="progressbar"' not in response.data


def test_dashboard_remaining_and_exceeded_progress(client, app):
    save_targets(app.config["DATABASE"], "200", "20")
    insert_meal(app.config["DATABASE"], VALID_MEAL)

    remaining = client.get("/?date=2026-11-02")
    assert remaining.status_code == 200
    assert b"Remaining" in remaining.data
    assert b"aria-valuenow=\"100\"" in remaining.data

    insert_meal(app.config["DATABASE"], dict(VALID_MEAL, food_name="Dinner", calories="400", protein="30"))
    exceeded = client.get("/?date=2026-11-02")
    assert exceeded.status_code == 200
    assert b"Exceeded" in exceeded.data
    assert exceeded.data.count(b'aria-valuenow="100"') >= 2


def test_invalid_meal_uses_accessible_styled_validation(client):
    response = client.post("/meals", data=dict(VALID_MEAL, food_name="", category=""))

    assert response.status_code == 400
    assert b"is-invalid" in response.data
    assert b'aria-invalid="true"' in response.data
    assert b"aria-describedby=\"food_name_error\"" in response.data


def test_meal_category_and_actions_render(client, app):
    insert_meal(app.config["DATABASE"], VALID_MEAL)

    response = client.get("/?date=2026-11-02")

    assert response.status_code == 200
    assert b"Breakfast" in response.data
    assert b"category-badge" in response.data
    assert b"/meals/1/edit" in response.data
    assert b"/meals/1/delete" in response.data
