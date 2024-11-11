import pytest

from src.card import Card
from src.price import Price


def test_init():
    p = Price(Т=1, М=2, К=3, Б=4, З=5)
    assert p.Т == 1
    assert p.М == 2
    assert p.К == 3
    assert p.Б == 4
    assert p.З != 4



def test_save():
    p = Price(Т=1, М=2, К=3, Б=4, З=5)
    assert repr(p) == 'Т:1 М:2 К:3 Б:4 З:5'





