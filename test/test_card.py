import pytest

from src.card import Card


def test_init():
    c = Card('b', 5)
    assert c.vegs == 'b'
    assert c.price == 5


def test_save():
    c = Card('b', 5)
    assert repr(c) == 'b5'
    assert c.save() == 'b5'

    c = Card('t', 2)
    assert repr(c) == 't2'
    assert c.save() == 't2'


def test_eq():
    c1 = Card('e', 3)
    c2 = Card('e', 3)
    c3 = Card('e', 1)
    c4 = Card('t', 3)
    c5 = Card('b', 5)

    assert c1 == c2
    assert c1 != c3
    assert c1 != c4
    assert c1 != c5

def test_load():
    s = 'b3'
    c = Card.load(s)
    assert c == Card('b', 3)

    s = 't5'
    c = Card.load(s)
    assert c == Card('t', 5)

def test_all_cards():
    cards = Card.all_cards(['b', 'e'], price=[1, 2, 3])
    # print(cards)
    expected_cards = [
        Card.load('b1'),
        Card.load('b2'),
        Card.load('b3'),
        Card.load('e1'),
        Card.load('e2'),
        Card.load('e3')
    ]
    assert cards == expected_cards

    cards = Card.all_cards()
    assert len(cards) == 4 * 6