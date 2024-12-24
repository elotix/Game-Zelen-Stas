from src.card import Card
from src.deck import Deck
from src.player import Player
from src.price import Price


class GameState:
    MAX_ROUND = 6
    MIN_PLAYERS = 2
    MAX_PLAYERS = 6
    MIN_PLAYABLE_CARD = 1

    def __init__(self, players, deck, price, cards, current_player_index=0, round_index=1):
        self.cards = cards  # Карты
        self.price = price  # Цены на овощи
        self.deck = deck  # Колода
        self.players = players  # Список игроков
        self.current_player_index = current_player_index  # Индекс текущего игрока
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

    def save(self):
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
            cards=[Card.load(s) for s in data["cards"]],
            deck=Deck.load(data["deck"]),
            price=Price.load(data["price"]),
            current_player_index=int(data["current_player_index"]),
            round_index=int(data["round_index"])
        )

    def next_player(self):
        n = len(self.players)
        self.current_player_index = (self.current_player_index + 1) % n

    def deal_cards(self):
        num = len(self.players)
        self.cards = [self.deck.draw_card() for _ in range(num + 1)]