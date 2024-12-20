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

    def save_cards(self):
        saved_cards = map(lambda c: c.save(), self.card_list)
        result = ' '.join(saved_cards)
        return result.strip()

    def __eq__(self, other):
        if isinstance(other, str):
            other_hand = Hand.load(other)
            return self.card_list == other_hand.card_list
        return False

    @classmethod
    def load_cards(cls, text):
        cards_from_text = []
        for s in text.split():
            cards_from_text.append(Card.load(s))
        return cls(cards=cards_from_text)

    def add_card(self, card):
        self.card_list.append(card)

    def __getattr__(self, name):
        """ hand.Б, а этого Б нет, тогда пробегаем по всем картам руки и берем карта.Б
        То есть считает сколько овощей с именем name во всех картах руки.
        На картах нет Б, там маленькие латинские буквы!!!
        """
        if name in Card.VEGETABLES:
            total = 0
            for card in self.card_list:
                total += getattr(card, name)
            return total
        raise AttributeError

    def score(self, price: Price):
        total_score = 0
        for card in self.card_list:
            total_score += card.score(price)
        return total_score