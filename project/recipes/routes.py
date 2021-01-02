from . import recipes_blueprint
from flask import render_template, redirect, url_for


@recipes_blueprint.route('/')
def recipes():
    return render_template('recipes/recipes.html')


@recipes_blueprint.route('/breakfast')
def breakfast_recipes():
    return render_template('recipes/breakfast.html')


@recipes_blueprint.route('/breakfast/pancakes')
def breakfast_recipe_pancake():
    return render_template('recipes/recipe_details.html')
