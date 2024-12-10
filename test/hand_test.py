import pytest
from src.card import Card
from src.hand import Hand

cards = [Card.load('ТМК'), Card.load('КБЗ'), Card.load('ЗЗЗ')]


def test_init():
    i = Hand(cards)
    assert i.card_list == cards


def test_save():
    s = Hand(cards=cards)
    assert s.save_cards() == 'ТМК КБЗ ЗЗЗ'



