from datetime import date

from flask import abort, current_app, flash, redirect, render_template, request, url_for

from .models import (
    delete_meal, get_meal, get_targets, insert_meal, list_meals, save_targets, update_meal,
    decimal_value,
)
from .nutrition import daily_totals, format_value, progress
from .validation import validate_category, validate_date, validate_decimal, validate_required_name


def database_path():
    return current_app.config["DATABASE"]


def selected_date(raw_date=None):
    if raw_date:
        valid, error = validate_date(raw_date)
        return valid if not error else date.today().isoformat()
    return request.args.get("date") or date.today().isoformat()


def meal_data(form):
    name, name_error = validate_required_name(form.get("food_name"))
    category, category_error = validate_category(form.get("category"))
    calories, calories_error = validate_decimal(form.get("calories"), "Calories", allow_zero=True)
    protein, protein_error = validate_decimal(form.get("protein"), "Protein", allow_zero=True)
    meal_date, date_error = validate_date(form.get("meal_date"))
    errors = {
        "food_name": name_error,
        "category": category_error,
        "calories": calories_error,
        "protein": protein_error,
        "meal_date": date_error,
    }
    if any(errors.values()):
        return None, errors
    return {
        "food_name": name,
        "category": category,
        "calories": calories,
        "protein": protein,
        "meal_date": meal_date,
    }, {}


def register_routes(app):
    @app.route("/", methods=["GET"])
    def dashboard():
        meal_date = selected_date(request.args.get("date"))
        meals = list_meals(database_path(), meal_date)
        calories, protein = daily_totals(database_path(), meal_date)
        targets = get_targets(database_path())
        calorie_progress = protein_progress = None
        if targets:
            calorie_progress = progress(calories, decimal_value(targets["calorie_target"]))
            protein_progress = progress(protein, decimal_value(targets["protein_target"]))
        return render_template(
            "dashboard.html", meals=meals, meal_date=meal_date,
            calories=format_value(calories), protein=format_value(protein),
            targets=targets, calorie_progress=calorie_progress,
            protein_progress=protein_progress, format_value=format_value,
        )

    @app.route("/meals/new", methods=["GET"])
    def new_meal():
        meal_date = selected_date(request.args.get("date"))
        return render_template("meal_form.html", meal=None, values={"meal_date": meal_date}, errors={})

    @app.route("/meals", methods=["POST"])
    def create_meal():
        data, errors = meal_data(request.form)
        if errors:
            return render_template("meal_form.html", meal=None, values=request.form, errors=errors), 400
        insert_meal(database_path(), data)
        flash("Meal added.")
        return redirect(url_for("dashboard", date=data["meal_date"]))

    @app.route("/meals/<int:meal_id>/edit", methods=["GET"])
    def edit_meal(meal_id):
        meal = get_meal(database_path(), meal_id)
        if not meal:
            abort(404)
        return render_template("meal_form.html", meal=meal, values=meal, errors={})

    @app.route("/meals/<int:meal_id>/edit", methods=["POST"])
    def update_meal_route(meal_id):
        if not get_meal(database_path(), meal_id):
            abort(404)
        data, errors = meal_data(request.form)
        if errors:
            return render_template("meal_form.html", meal={"id": meal_id}, values=request.form, errors=errors), 400
        update_meal(database_path(), meal_id, data)
        flash("Meal updated.")
        return redirect(url_for("dashboard", date=data["meal_date"]))

    @app.route("/meals/<int:meal_id>/delete", methods=["POST"])
    def delete_meal_route(meal_id):
        meal = get_meal(database_path(), meal_id)
        if not meal:
            abort(404)
        delete_meal(database_path(), meal_id)
        flash("Meal deleted.")
        return redirect(url_for("dashboard", date=meal["meal_date"]))

    @app.route("/targets", methods=["GET"])
    def targets():
        return render_template("targets.html", targets=get_targets(database_path()), errors={})

    @app.route("/targets", methods=["POST"])
    def update_targets():
        calories, calories_error = validate_decimal(
            request.form.get("calorie_target"), "Calorie target", allow_zero=False
        )
        protein, protein_error = validate_decimal(
            request.form.get("protein_target"), "Protein target", allow_zero=False
        )
        errors = {"calorie_target": calories_error, "protein_target": protein_error}
        if any(errors.values()):
            return render_template("targets.html", targets=request.form, errors=errors), 400
        save_targets(database_path(), calories, protein)
        flash("Nutrition targets updated.")
        return redirect(url_for("dashboard"))

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("error.html", message="The requested meal could not be found."), 404

    @app.errorhandler(Exception)
    def operation_error(error):
        app.logger.exception("Unexpected operation failure", exc_info=error)
        return render_template(
            "error.html",
            message="We could not complete that operation. Your existing records were not changed.",
        ), 500
