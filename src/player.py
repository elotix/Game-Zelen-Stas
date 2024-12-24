import json
import typing

from src.hand import Hand
from src.price import Price


class Player:
    def __init__(self, n, h):
        self.name = n
        self.hand = h

    def __str__(self):
        return self.name + ': ' + str(self.hand)

    def save(self):
        return {'name': self.name, 'hand': str(self.hand)}

    @classmethod
    def load(cls, d):
        return cls(d['name'], Hand.load(d['hand']))

    def score(self, price: Price):
        return self.hand.score(price)