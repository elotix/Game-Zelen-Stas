import random

from src.card import Card
from src.deck import Deck

cards = [Card('b', 3), Card('t', 0), Card('e', 5)]

def test_init():
    d = Deck(cards=cards)
    assert d.cards == cards