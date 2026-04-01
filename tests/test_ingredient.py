import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize('name, price, ingredient_type', [
        ('Соус 1', 1, INGREDIENT_TYPE_SAUCE), 
        ('Начинка 1234', 1234, INGREDIENT_TYPE_FILLING), 
        ('Начинка 2323 232 3', 12345678, INGREDIENT_TYPE_FILLING),
    ])
    def test_ingredient_fields(self, name, price, ingredient_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.name == name and ingredient.price == price and ingredient.type == ingredient_type

    @pytest.mark.parametrize('name, price, ingredient_type', [
        ('Секретный ингредиент', 100000, INGREDIENT_TYPE_SAUCE), 
        ('Соус №12', 1234, INGREDIENT_TYPE_SAUCE), 
        ('Начинка №9', 12, INGREDIENT_TYPE_FILLING),
    ])
    def test_ingredient_getters(self, name, price, ingredient_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name and ingredient.get_price() == price and ingredient.get_type() == ingredient_type
