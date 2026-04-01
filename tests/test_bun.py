import pytest

from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize('name, price', [
        ('', 0), 
        ('test_name', 1234), 
        ('2323 232 3', 12345678),
    ])
    def test_bun_fields(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name and bun.price == price

    @pytest.mark.parametrize('name, price', [
        (' ', 321), 
        ('test!1234', 12), 
        ('2323 232 3', 9875000),
    ])
    def test_bun_getters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name and bun.get_price() == price
