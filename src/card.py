"""Карты UNO."""
from typing import Self
class Card:
    VEGETABLES = ['c', 'e', 'b', 't']
    PRICE = list(range(6))
    def __init__(self, vegs: str, price: int):
        if vegs not in Card.VEGETABLES:
            raise ValueError
        if price not in Card.PRICE:
            raise ValueError
        self.vegs = vegs
        self.price = price

    def __repr__(self):
        return f'{self.vegs}{self.price}'

    def __eq__(self, other):
        if isinstance(other, str):
            other = Card.load(other)
        return self.vegs == other.vegs and self.price == other.price

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        return Card(vegs=text[0], price=int(text[1]))

    @staticmethod
    def all_cards(vegetables: list[str] | None = None, price: None | list[int] = None):
        if vegetables is None:
            vegetables = Card.VEGETABLES
        if price is None:
            price = Card.PRICE
        cards = [Card(vegs=veg, price=pr) for veg in vegetables for pr in price]
        return cards