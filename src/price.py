from src.card import Card
''

class Price:
    VEGETABLES = Card.VEGETABLES
    MAX_PRICE = 5

    def __init__(self, **kwargs):
        # Создаем овощи, значения по умолчанию будут 0
        self.t = kwargs.get('Т', 0)
        self.m = kwargs.get('М', 0)
        self.k = kwargs.get('К', 0)
        self.b = kwargs.get('Б', 0)
        self.z = kwargs.get('З', 0)

        # Проверяем все переданные овощи
        for vegetable in kwargs.keys():
            if vegetable not in self.VEGETABLES:
                raise ValueError("Неизвестный овощ: " + vegetable)

        # Проверяем все значения
        for value in kwargs.values():
            if value < 0 or value > Price.MAX_PRICE:
                raise ValueError("Цена овоща должна быть между 0 и " + str(Price.MAX_PRICE))

    def validate_vegetables(self, symbols):
        for v in symbols:
            if v not in self.VEGETABLES:
                raise ValueError(f"Неизвестный овощ: {v}")

    def validate_values(self, values):
        for v in values:
            if not 0 <= v <= Price.MAX_PRICE:
                raise ValueError(f"Цена овоща должна быть между 0 и {Price.MAX_PRICE}")

    def __repr__(self):
        result = f'Т:{self.t} М:{self.m} К:{self.k} Б:{self.b} З:{self.z}'
        return result

    def __eq__(self, other):
        if not isinstance(other, Price):
            return False
        return self.t == other.t \
            and self.m == other.m \
            and self.k == other.k \
            and self.b == other.b \
            and self.z == other.z

    def save(self):
        return repr(self)

    @classmethod
    def load(cls, price: str|dict):
        """'Т:1 М:2 К:3 Б:4 З:5' или {'T': 1} """
        if isinstance(price, str):
            words = price.split()
            d = {}
            for word in words:
                # word = 'T:1'
                k, v = word.split(':')
                d[k] = int(v)
            price = d
        return cls(**price)

    def add(self, card: Card):
        def add_vegetabel(a, b):
            return (a + b) % (self.MAX_PRICE + 1)
        self.t = add_vegetabel(self.t, card.t)
        self.k = add_vegetabel(self.k, card.k)
        self.m = add_vegetabel(self.m, card.m)
        self.b = add_vegetabel(self.b, card.b)
        self.z = add_vegetabel(self.z, card.z)
