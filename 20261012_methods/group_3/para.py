
# ИМЕРАТИВНАЯ ПАРАДИГМА

k = 1.0
b = 10.0
x = 3.0

y = k * x + b
print(y)


# ПРОЦЕДУРНАЯ ПАРАДИГМА


def calc_linear_equation(k: float, b: float, x: float):
    y = k * x + b
    return y

r1 = calc_linear_equation(k=1.0, b=10.0, x= 3.0)
r2 = calc_linear_equation(k=1.0, b=10.0, x= 3.0)


# ОБЪЕКТНАЯ ПАРАДИГМА

class LinearEquation:
    k: float
    b: float

    def __init__(self, k, b):
        self.k = k
        self.b = b

    def calc_y(self, x: float):
        return self.k * x + self.b

le_1 = LinearEquation(k = 1.0, b=10.0)
r3_1 = le_1.calc_y(x=3.0)
r3_2 = le_1.calc_y(x=4.0)
r3_3 = le_1.calc_y(x=5.0)









