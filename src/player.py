import json
import typing

from src.hand import Hand


class Player:
    def __init__(self, n, h, s=0):
        self.name = n
        self.hand = h
        self.score = s

    def __str__(self):
        return self.name + '(' + str(self.score) + '): ' + str(self.hand)

    def save(self):
        return {'name': self.name, 'hand': str(self.hand), 'score': self.score}

    @classmethod
    def load(cls, d):
        return cls(d['name'], Hand.load(d['hand']), int(d['score']))