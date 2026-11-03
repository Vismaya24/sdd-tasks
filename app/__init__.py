import os

from flask import Flask

from .db import init_db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "nutrition.db"),
    )

    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    with app.app_context():
        init_db(app.config["DATABASE"])

    from . import routes

    routes.register_routes(app)
    return app


app = create_app()
