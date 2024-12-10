import pytest

from src.card import Card
from src.price import Price


def test_init():
    p = Price(Т=1, М=2, К=3, Б=4, З=5)
    assert p.t == 1
    assert p.m == 2
    assert p.k == 3
    assert p.b == 4
    assert p.z == 5

def test_save():
    p = Price(Т=1, М=2, К=3, Б=4, З=5)
    assert repr(p) == 'Т:1 М:2 К:3 Б:4 З:5'

def test_validation():
    with pytest.raises(ValueError):
        p = Price(Т=1, М=2, К=3, Б=4, З=6)


def test_load():
    t = "Т:1 М:2 К:3 Б:4 З:5"
    assert Price.load(t) == Price(Т=1, М=2, К=3, Б=4, З=5)

'''def test_add():
    p = Price(Т=2, М=2, К=3, Б=4, З=5)
    p.add("БЗЗ")
    assert p.t == p.m == 2'''
