import pytest

from praktikum.database import Database
from praktikum.ingredient_types import *

class TestDatabase:
    @pytest.mark.parametrize("index, bun_name, bun_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_database_available_buns(self, index, bun_name, bun_price):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3 and buns[index].name == bun_name and buns[index].price == bun_price

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, bun_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_database_ingredients(self, index, ingredient_type, ingredient_name, bun_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6 and ingredients[index].type == ingredient_type and ingredients[index].name == ingredient_name and ingredients[index].price == bun_price
