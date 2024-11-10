import random
from src.card import Card

class Deck:
    def __init__(self, cards=None):
        if cards is None:
            cards = Card.all_cards()
            random.shuffle(cards)
        self.cards = cards  # список карт

    def __eq__(self, other):
        if isinstance(other, str):
            other = Deck.load(other)
        return self.cards == other.cards

    def __repr__(self):
        return self.save()

    def save(self):
        save_cards = []
        for c in self.cards:
            save_cards.append(c.save())
        s = ' '.join(save_cards)
        return s

    @classmethod
    def load(cls, text):
        cards = []
        for s in text.split():
            cards.append(Card.load(s))
        return cls(cards)

    def draw_card(self):
        if len(self.cards) == 0:  # Проверяем, есть ли карты в колоде
            return None
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)  # Перемешиваем карты
