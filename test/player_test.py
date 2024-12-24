from src.hand import Hand
from src.player import Player
from src.card import Card


cards = [Card.load(' '), Card.load('КБЗ'), Card.load('ЗЗЗ')] #[ТМК, КБЗ, ЗЗЗ]

def test_init():
    h = Hand.load('ТМК КБЗ ЗЗЗ')
    p = Player(n='Bob', h=h)
    assert p.name == 'Bob'
    assert p.hand == h


def test_load():
    d = {'name': 'Bob', 'hand': 'ТМК КБЗ ЗЗЗ'}
    h_exp = Hand.load('ТМК КБЗ ЗЗЗ')
    p_exp = Player(n='Bob', h=h_exp)
    assert str(p_exp) == str(Player.load(d))


def test_save():
    h = Hand.load('ТМК КБЗ ЗЗЗ')
    p = Player(n='Bob', h=h)
    assert str(p) == 'Bob: ТМК КБЗ ЗЗЗ'
    assert p.save() == {'name': 'Bob', 'hand': 'ТМК КБЗ ЗЗЗ'}