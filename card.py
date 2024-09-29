"""Карты UNO."""

class Card:
    VEGETABLES = ['c', 'e', 'b', 't']
    PRICE = list(range(6))
    def __init__(self, vegetable: str, price: int):
        if vegetable not in Card.VEGETABLES:
            raise ValueError
        if price not in Card.PRICE:
            raise ValueError
        self.vegetable = vegetable
        self.price = price

    def __repr__(self):
        return f'{self.vegetable}{self.price}'

    def __eq__(self, other):
        if isinstance(other, str):
            other = Card.load(other)
        return self.vegetable == other.vegetable and self.price == other.price

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        return Card(vegetable=text[0], price=int(text[1]))

