from src.card import Card
from src.price import Price

''
class Hand:

    def __init__(self, cards=None):
        if cards == None:
            cards = []
        self.card_list = cards


    def __repr__(self):
        return self.save()

    def save(self):
        saved_cards = map(lambda c: c.save(), self.card_list)
        result = ' '.join(saved_cards)
        return result.strip()

    def __eq__(self, other):
        if isinstance(other, str):
            other_hand = Hand.load_cards(other)
            return self.card_list == other_hand.card_list
        return False

    @classmethod
    def load(cls, text: str):
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def add_card(self, card):
        self.card_list.append(card)

    def __getattr__(self, name):
        """ hand.Б, а этого Б нет, тогда пробегаем по всем картам руки и берем карта.Б
                То есть считает сколько овощей с именем name во всех картах руки.
                На картах нет Б, там маленькие латинские буквы!!!
                """
        if name in Card.VEGETABLES:
            return sum(getattr(card, name) for card in self.cards)
        raise AttributeError


    def score(self, price: Price):
        total_score = 0
        for card in self.card_list:
            total_score += card.score(price)
        return total_score