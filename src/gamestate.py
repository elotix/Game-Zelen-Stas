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
            "players": [p.save() for p in self.players],
            "cards": [c.save() for c in self.cards],
            "deck": str(self.deck),
            "price": str(self.price),
            "current_player_index": self.current_player_index,
            "round_index": self.round_index
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(d) for d in data["players"]]
        cards = [Card.load(c) for c in data["cards"]]

        return cls(
            players=players,
            cards=cards,
            deck=Deck.load(data["deck"]),
            price=Price.load(data["price"]),
            current_player_index=int(data["current_player_index"]),
            round_index=int(data["round_index"])
        )

    def next_player(self):
        n = len(self.players)
        self.current_player_index = (self.current_player_index + 1) % n
