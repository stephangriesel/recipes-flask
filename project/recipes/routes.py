from . import recipes_blueprint
from flask import render_template, redirect, url_for


@recipes_blueprint.route('/')
def recipes():
    return render_template('recipes/recipes.html')
