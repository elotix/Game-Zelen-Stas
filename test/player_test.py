from src.hand import Hand
from src.player import Player
from src.card import Card




def test_init():
    h = Hand.load('ТМК КБЗ ЗЗЗ')
    p = Player(n='Bob', h=h, s=10)
    assert p.name == 'Bob'
    assert p.hand == h
    assert p.score == 10


def test_load():
    d = {'name': 'Bob', 'hand': 'ТМК КБЗ ЗЗЗ', 'score': 10}
    h_exp = Hand.load('ТМК КБЗ ЗЗЗ')
    p_exp = Player(n='Bob', h=h_exp, s=10)
    assert str(p_exp) == str(Player.load(d))


def test_save():
    h = Hand.load('ТМК КБЗ ЗЗЗ')
    p = Player(n='Bob', h=h, s=10)
    assert str(p) == 'Bob(10): ТМК КБЗ ЗЗЗ'
    assert p.save() == {'name': 'Bob', 'hand': 'ТМК КБЗ ЗЗЗ', 'score': 10}
