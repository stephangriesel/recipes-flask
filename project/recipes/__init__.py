"""
The `recipes` blueprint handles the create/read/update/delete functions for the recipes.
"""
from flask import Blueprint

recipes_blueprint = Blueprint('recipes', __name__, template_folder='templates')

from . import routes
