class Price:
    def __init__(self, c=0, e=0, b=0, t=0):
        if all([0 <= c <= 5, 0 <= e <= 5, 0 <= b <= 5, 0 <= t <= 5]):
            self.c = c
            self.e = e
            self.b = b
            self.t = t
        else:
            raise ValueError

    def __repr__(self):
        return f'{self.c}{self.e}{self.b}{self.t}'

    def __eq__(self, other):
        if isinstance(other, str):
            return self.c == other.c and self.e == other.e and self.b == other.b and self.t == other.t

    def save(self):
        return repr(self)



    def in_price():
        return Price(int(input('c')),
                     (int(input('e'))),
                     (int(input('b'))),
                     (int(input('t'))))
