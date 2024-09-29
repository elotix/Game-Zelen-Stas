import pytest

from src.price import Price
def test_init():
    p = Price(0,1,2,3)
    assert p.c == 0
    assert p.e == 1
    assert p.b == 2
    assert p.t == 3

def test_save():
    p = Price(0, 1, 2, 3)
    assert repr(p) == "0123"
    assert p.save() == "0123"

q