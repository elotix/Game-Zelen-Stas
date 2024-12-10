from src.card import Card
from src.deck import Deck
from src.player import Player
from src.price import Price


class GameState:
    MAX_ROUND = 6
    MIN_PLAYERS = 2
    MAX_PLAYERS = 6

    def __init__(self, cards, price, deck, players, current_player_index=0, round_index=1):
        self.cards = cards  # Список игроков
        self.price = price  # Колода карт
        self.deck = deck  # Индекс текущего игрока
        self.players = players  # Цены на овощи
        self.current_player_index = current_player_index  # Список карт
        self.round_index = round_index  # Номер раунда

    def __eq__(self, other):
        return (self.cards == other.cards and
                self.price == other.price and
                self.deck == other.deck and
                self.players == other.players and
                self.current_player_index == other.current_player_index and
                self.round_index == other.round_index)

    def get_current_player(self):
        return self.players[self.current_player_index]

    def save_game(self):
        return {  # Сохранение состояния игры в словарь
            "cards": [c.save() for c in self.cards],
            "price": str(self.price),
            "deck": str(self.deck),
            "players": [p.save() for p in self.players],
            "current_player_index": self.current_player_index,
            "round_index": self.round_index
        }