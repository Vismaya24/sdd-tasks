import sqlite3
from contextlib import contextmanager
from pathlib import Path


def get_db(database):
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    return connection


def init_db(database):
    Path(database).parent.mkdir(parents=True, exist_ok=True)
    with get_db(database) as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS meals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                food_name TEXT NOT NULL CHECK(length(trim(food_name)) BETWEEN 1 AND 120),
                category TEXT NOT NULL CHECK(category IN ('Breakfast', 'Lunch', 'Dinner', 'Snacks')),
                calories NUMERIC NOT NULL CHECK(calories >= 0),
                protein NUMERIC NOT NULL CHECK(protein >= 0),
                meal_date TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS nutrition_targets (
                id INTEGER PRIMARY KEY CHECK(id = 1),
                calorie_target NUMERIC NOT NULL CHECK(calorie_target > 0),
                protein_target NUMERIC NOT NULL CHECK(protein_target > 0),
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """
        )


@contextmanager
def transaction(database):
    connection = get_db(database)
    try:
        connection.execute("BEGIN")
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
