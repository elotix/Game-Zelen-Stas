class Price:
    def __init__(self, c=0, e=0, b=0, t=0):
        if all([0 <= c <= 5, 0 <= e <= 5, 0 <= b <= 5, 0 <= t <= 5]):
            self.c = c
            self.e = e
            self.b = b
            self.t = t
        else:
            raise ValueError
