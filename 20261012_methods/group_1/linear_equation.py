# ИМЕРАТИВНЫЙ

k = 1.0
x = 10.0
b = 15.0

y = k * x + b
print(y)


# ПРОЦЕДУРНЫЙ
def calc_linear_equation(k, b, x):
    return k * x + b


r1 = calc_linear_equation(k=1.0, b=15.0, x=10.0)
r2 = calc_linear_equation(k=1.0, b=15.0, x=1.0)
r3 = calc_linear_equation(k=1.0, b=15.0, x=100.0)

print(r1)
print(r2)
print(r3)


# ОБЪЕКТНЫЙ СТИЛЬ

class LinearEquation:
    k: float # Поле
    b: float # Поле

    def __init__(self, k: float, b: float):
        self.k = k
        self.b = b

    def calc_y(self, x: float):
        return self.k * x + self.b


le_1 = LinearEquation(k=1.0, b=15.0)
le_1.calc_y(x=10.0)
le_1.calc_y(x=1.0)
le_1.calc_y(x=100.0)
le_2 = LinearEquation(k=2.0, b=30.0)
