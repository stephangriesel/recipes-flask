from . import recipes_blueprint
from flask import render_template, abort


breakfast_recipe_names = ['pancakes', 'acai_bowl', 'honey_bran_muffins', 'breakfast_scramble',
                          'pumpkin_donuts', 'waffles', 'omelette']


@recipes_blueprint.route('/')
def recipes():
    return render_template('recipes/recipes.html')


@recipes_blueprint.route('/breakfast/')
def breakfast_recipes():
    return render_template('recipes/breakfast.html')


@recipes_blueprint.route('/breakfast/<recipe_name>/')
def breakfast_recipe(recipe_name):
    if recipe_name not in breakfast_recipe_names:
        abort(404)

    return render_template(f'recipes/{recipe_name}.html')
