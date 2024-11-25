from src.card import Card

class Hand:

    def __init__(self, cards=None):
        if cards == None:
            cards = []
        self.card_list = cards

    def __repr__(self):
        return self.save()

    def save_cards(self):
        saved_cards = []
        for c in self.card_list:
            saved_cards.append(c.save())
        result = ''
        for sc in saved_cards:
            result += sc + ' '
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
        if name in Card.VEGETABLES:
            total = 0
            for card in self.card_list:
                total += getattr(card, name)
            return total
        raise AttributeError

    def score(self, other):
        total_score = 0
        for v in Card.VEGETABLES:
            total_score += getattr(self, v) * getattr(other, v)
        return total_score