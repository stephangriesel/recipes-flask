"""
This file (test_recipes.py) contains the functional tests for the `recipes` blueprint.
"""


def test_get_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    header_items = [b'Kennedy Family Recipes', b'Recipes', b'Blog', b'About']
    recipe_types = [b'Breakfast', b'Lunch', b'Dinner', b'Side Dishes',
                    b'Dessert', b'Smoothies', b'Baked Goods', b'Drinks']
    response = test_client.get('/')
    assert response.status_code == 200
    for header_item in header_items:
        assert header_item in response.data
    for recipe_type in recipe_types:
        assert recipe_type in response.data


def test_get_breakfast_recipes(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/breakfast/' page is requested (GET)
    THEN check the response is valid
    """
    recipes = [b'Pancakes', b'Honey Bran Muffins', b'Acai Bowl',
               b'Breakfast Scramble', b'Pumpkin Donuts', b'Waffles',
               b'Omelette']
    response = test_client.get('/breakfast/')
    assert response.status_code == 200
    for recipe in recipes:
        assert recipe in response.data
