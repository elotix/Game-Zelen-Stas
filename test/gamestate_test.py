import pytest

from src.card import Card
from src.deck import Deck
from src.gamestate import GameState
from src.player import Player
from src.price import Price

data = {

    "cards": ['ТМК', 'КБЗ', 'ЗЗЗ'],
    "price": 'Т:5 М:4 К:3 Б:2 З:1',
    "deck": 'ТМК КБЩ БЗЗ ТММ МКК',
    "players": [
        {'name': 'Bob', 'hand': 'ТМК КБЗ БЗЗ', 'score': 5},
        {'name': 'Leon', 'hand': 'ТММ МКК КББ', 'score': 10}],
    "current_player_index": 1,
    "round_index": 1}
Bob = Player.load(data["players"][0])
Leon = Player.load(data["players"][1])
cards = (Card.load(s) for s in data["cards"])
full_deck = Deck(None)
price = Price.load('Т:5 М:4 К:3 Б:2 З:1')


def test_init():
    players = [Bob, Leon]
    game = GameState(players=players, deck=full_deck, price=price, cards=cards, current_player_index=0, round_index=1)
    assert game.players == players
    assert game.deck == full_deck
    assert game.price == price
    assert game.cards == cards
    assert game.current_player_index == 0
    assert game.round_index == 1


def test_current_players():
    players = [Bob, Leon]
    game = GameState(players=players, deck=full_deck, price=price, cards=cards, round_index=1)
    assert game.current_player() == Bob
    game = GameState(players=players, deck=full_deck, price=price, cards=cards, current_player_index=1, round_index=1)
    assert game.current_player() == Leon


def test_eq():
    players = [Bob, Leon]
    game1 = GameState(players=players, deck=full_deck, price=price, cards=cards, current_player_index=1, round_index=1)
    game2 = GameState(players=players.copy(), deck=full_deck, price=price, cards=cards, current_player_index=1,
                      round_index=1)
    game3 = GameState(
        players=players, deck=Deck(Card.all_cards(['Б', 'З'])), price=price, cards=cards, current_player_index=1,
        round_index=1
    )
    assert game1 == game2
    assert game1 != game3


# def test_save():
#     players = [Bob, Leon]
#     game = GameState(players=players, deck=Deck(Card.all_cards(['Б', 'З'])), price=price, cards=cards,
#                      current_player_index=1, round_index=1)
#     assert game.save() == data
#
#
# def test_load():
#     game = GameState.load(data)
#     assert game.save() == data
#
#
# def test_next_player():
#     game = GameState.load(data)
#     assert str(game.current_player()) == 'Leon(10): ТММ МКК КББ'
#     game.next_player()
#     assert str(game.current_player()) == 'Bob(5): ТМК КБЗ БЗЗ'
#     game.next_player()
#     assert str(game.current_player()) == 'Leon(10): ТММ МКК КББ'
