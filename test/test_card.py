import pytest
from src.card import Card


def test_card_create():
    card = Card(Т=1, М=1, К=1)
    assert card.t == 1
    assert card.m == 1
    assert card.k == 1
    assert card.b == 0
    assert card.z == 0

def test_card_empty():
    with pytest.raises(ValueError, match="Сумма овощей должна равняться 3."):
        Card()

def test_card_wrong_total():
    with pytest.raises(ValueError, match="Сумма овощей должна равняться 3."):
        Card(Т=2, М=2)  # Сумма 4, что недопустимо

def test_card_repr():
    card = Card(Т=1, Б=1, З=1)
    assert repr(card) == 'ТБЗ'  # Проверяем правильность строкового представления

def test_card_equality():
    card1 = Card(Т=1, М=1, К=1)
    card2 = Card(Т=1, М=1, К=1)
    card3 = Card(Т=1, М=1, Б=1)
    assert card1 == card2
    assert card1 != card3

def test_card_load():
    text = 'ТТМ'
    card = Card.load(text)
    assert card.t == 2
    assert card.m == 1
    assert card.k == 0
    assert card.b == 0
    assert card.z == 0



