# ИМПЕРАТИВНАЯ ПАРАДИГМА

k = 1.0
b = 10.0
x = 3.0

y = k * x + b

print(y)

# ПРОЦЕДУРНАЯ ПАРАДИГМА

def calculate_linear_equation(k: float,
                              b: float,
                              x: float) -> float:
    y = k * x + b
    return y

calculate_linear_equation(k=1.0, b=10.0, x= 3.0)


# ОБЪЕКТНАЯ ПАРАДИГМА

class LinearEquation:
    k: float
    b: float

    def calc_y(self, x: float):
        y = self.k * x + self.b
        return y


le_1 = LinearEquation(k=1.0, b=10.0)
r1 = le_1.calc_y(x=1.0)
r1 = le_1.calc_y(x=3.0)
r1 = le_1.calc_y(x=10.0)
