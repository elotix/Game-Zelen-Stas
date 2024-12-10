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




