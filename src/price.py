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
        result = f'T:{self.t} М:{self.m} К:{self.k} Б:{self.b} З:{self.z}'
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

    def add(self, other):
        if isinstance(other, Price):
            for v in self.VEGETABLES:

                new_value = getattr(self, v) + getattr(other, v)
                print(new_value)
                setattr(self, v, min(new_value, Price.MAX_PRICE))
        elif isinstance(other, dict):
            for v in other.keys():
                if v in self.VEGETABLES:
                    new_value = getattr(self, v) + other[v]
                    setattr(self, v, min(new_value, Price.MAX_PRICE))
        else:
            raise TypeError("Неподдерживаемый тип для добавления")

    def total_value(self):
        total = 0
        for v in self.VEGETABLES:
            total += getattr(self, v)
        return total  # Возвращает общую стоимость овощей в коробке

    def clear(self):
        for v in self.VEGETABLES:
            setattr(self, v, 0)  # Сбрасывает все овощи до 0

