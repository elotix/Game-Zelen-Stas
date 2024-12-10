class Card:
    VEGETABLES = ['Т', 'М', 'К', 'Б', 'З']
    SIZE = 3

    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError("Сумма овощей должна равняться 3.")
        total = sum(kwargs.values())
        if total != self.SIZE:
            raise ValueError("Сумма овощей должна равняться 3.")

        self.t = kwargs.get('Т', 0)
        self.m = kwargs.get('М', 0)
        self.k = kwargs.get('К', 0)
        self.b = kwargs.get('Б', 0)
        self.z = kwargs.get('З', 0)

    def __repr__(self):
        return self.t * 'Т' + self.m * 'М' + self.k * 'К' + self.b * 'Б' + self.z * 'З'

    def __eq__(self, other):
        return (self.t == other.t and
                self.m == other.m and
                self.k == other.k and
                self.b == other.b and
                self.z == other.z)

    def score(self, price):
        total = 0
        total += self.t * price.t
        total += self.m * price.m
        total += self.k * price.k
        total += self.b * price.b
        total += self.z * price.z
        return total

    def save(self):
        return repr(self)

    @staticmethod
    def load(text):
        """From 'МММ' to Card(М=3)"""
        counts = {}
        for v in Card.VEGETABLES:
            counts[v] = text.count(v)
        return Card(**counts)

    @staticmethod
    def all_cards(VEGETABLES=None):
        if VEGETABLES is None:
            VEGETABLES = Card.VEGETABLES
        cards = []
        for veg1 in VEGETABLES:
            for veg2 in VEGETABLES:
                if veg1 != veg2:
                    cards.append(Card.load(veg1 * 2 + veg2))
        cards += cards.copy()
        for veg in VEGETABLES:
            cards.append(Card.load(veg * 3))