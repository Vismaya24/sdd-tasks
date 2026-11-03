from datetime import datetime
from decimal import Decimal

from .db import get_db, transaction


def decimal_value(value):
    return Decimal(str(value))


def insert_meal(database, data):
    with transaction(database) as connection:
        connection.execute(
            "INSERT INTO meals (food_name, category, calories, protein, meal_date) "
            "VALUES (?, ?, ?, ?, ?)",
            (data["food_name"], data["category"], str(data["calories"]), str(data["protein"]), data["meal_date"]),
        )


def get_meal(database, meal_id):
    with get_db(database) as connection:
        row = connection.execute("SELECT * FROM meals WHERE id = ?", (meal_id,)).fetchone()
    return dict(row) if row else None


def list_meals(database, meal_date):
    with get_db(database) as connection:
        rows = connection.execute(
            "SELECT * FROM meals WHERE meal_date = ? ORDER BY id", (meal_date,)
        ).fetchall()
    return [dict(row) for row in rows]


def update_meal(database, meal_id, data):
    with transaction(database) as connection:
        connection.execute(
            "UPDATE meals SET food_name=?, category=?, calories=?, protein=?, meal_date=? WHERE id=?",
            (data["food_name"], data["category"], str(data["calories"]), str(data["protein"]),
             data["meal_date"], meal_id),
        )


def delete_meal(database, meal_id):
    with transaction(database) as connection:
        connection.execute("DELETE FROM meals WHERE id=?", (meal_id,))


def get_targets(database):
    with get_db(database) as connection:
        row = connection.execute(
            "SELECT * FROM nutrition_targets WHERE id = 1"
        ).fetchone()
    if not row:
        return None
    target = dict(row)
    target["calorie_target"] = decimal_value(target["calorie_target"])
    target["protein_target"] = decimal_value(target["protein_target"])
    return target


def save_targets(database, calorie_target, protein_target):
    now = datetime.now().isoformat(timespec="seconds")
    with transaction(database) as connection:
        connection.execute(
            """
            INSERT INTO nutrition_targets (id, calorie_target, protein_target, updated_at)
            VALUES (1, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                calorie_target=excluded.calorie_target,
                protein_target=excluded.protein_target,
                updated_at=excluded.updated_at
            """,
            (str(calorie_target), str(protein_target), now),
        )
