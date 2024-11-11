import pytest
from src.deck import Deck
from src.card import Card

# Пример колоды
cards_for_test = [Card.load('ТТТ'), Card.load('МЗЗ'), Card.load('БТК'), Card.load('МТК')]


def test_deck_init():
    deck = Deck(cards_for_test)
    assert deck.cards == cards_for_test  # Проверяем, что колода правильно создана


def test_save():
    deck = Deck(cards=cards_for_test)
    assert deck.save() == 'ТТТ МЗЗ ТКБ ТМК'

    deck = Deck(cards=[])
    assert deck.save() == ''


def test_deck_load():
    loaded_deck = Deck.load('ТТТ ЗМЗ БТК МТК')
    expected_deck = Deck(cards_for_test)
    assert loaded_deck == expected_deck  # Проверяем что колода загружается


def test_draw_card():
    deck_1 = Deck.load('ТТТ ЗМЗ БТК МТК')  # Загружаем колоду
    deck_2 = Deck.load('ТТТ ЗМЗ БТК')  # Создаем ожидаемую колоду, без одной карты
    card_drawn = deck_1.draw_card()  # Берем карту из колоды
    assert card_drawn == Card.load('МТК')  # Проверяем, что это именно нужная карта
    assert deck_1 == deck_2  # Проверяем, что колоды совпадают






