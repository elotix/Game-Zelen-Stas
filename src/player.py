import json
import typing

from src.hand import Hand
from src.price import Price


class Player:
    def __init__(self, n, h, s=0):
        self.name = n
        self.hand = h
        self.score = s

    def __str__(self):
        return f'{self.name}({self.score}): {self.hand}'

    def save(self):
        return {'name': self.name, 'hand': str(self.hand), 'score':self.score}

    @classmethod
    def load(cls, d):
        return cls(n=d['name'], h=Hand.load(d['hand']), s=int(d['score']))
