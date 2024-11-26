from src.card import Card


class Price:
    VEGETABLES = Card.VEGETABLES
    MAX_PRICE = 5

    def __init__(self, **kwargs):
        # Создаем овощи, значения по умолчанию будут 0
        for vegetable in self.VEGETABLES:
            if vegetable in kwargs:
                setattr(self, vegetable, kwargs[vegetable])
            else:
                setattr(self, vegetable, 0)

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
        result = ""
        for vegetable in self.VEGETABLES:
            result += vegetable + ":" + str(getattr(self, vegetable)) + " "
        return result.strip()  # Убираем лишние пробелы

    def __eq__(self, other):
        if not isinstance(other, Price):
            return False
        for v in self.VEGETABLES:
            if getattr(self, v) != getattr(other, v):
                return False
        return True

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

