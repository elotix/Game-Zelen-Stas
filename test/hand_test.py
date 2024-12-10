import pytest
from src.card import Card
from src.hand import Hand
from src.hand import Price
cards = [Card.load('ТМК'), Card.load('КБЗ'), Card.load('ЗЗЗ')]


def test_init():
    i = Hand(cards)
    assert i.card_list == cards


def test_save():
    s = Hand(cards=cards)
    assert s.save_cards() == 'ТМК КБЗ ЗЗЗ'

'''def test_load():
    s = Hand.load_cards('ТМК КБЗ ЗЗЗ')
    assert s == Hand(cards)'''


'''def test_add_card():
    h = Hand.load_cards('ТМК КБЗ ЗЗЗ')
    h.add_card(Card.load('ККК'))
    assert repr(h) == 'ТМК КБЗ ЗЗЗ ККК'
    '''
def test_score():
    h = Hand(cards=[Card.load('МКЗ')])
    p = Price(Т=1, М=2, К=3, Б=4, З=5)
    assert h.score(p) == 2 + 3 + 5
