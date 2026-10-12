class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_info(self):
        return f'x:{self.x}, y:{self.y}'

    def plus(self, other: 'Point'):  # не мутирующий метод
        x_new = self.x + other.x
        y_new = self.y + other.y
        p_new = Point(x=x_new, y=y_new)
        return p_new

    def plus_v2(self, other: 'Point'):  # мутирующий метод
        self.x = self.x + other.x
        self.y = self.y + other.y

        return self

    def calculate_the_middle(self, other: 'Point') -> 'Point':
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        p = Point(x, y)
        return p


def calculate_the_middle(p1: Point, p2: Point) -> Point:
    x = (p1.x + p2.x) / 2
    y = (p1.y + p2.y) / 2
    p = Point(x, y)
    return p


def test_func_middle_point():
    p1 = Point(2, 4)
    p2 = Point(8, 10)
    p3 = calculate_the_middle(p1=p1, p2=p2)

    print(p1.get_info())
    print(p2.get_info())
    print(p3.get_info())


def test_point_plus():
    p1 = Point(2, 4)
    p2 = Point(8, 10)

    p3 = p1.plus(other=p2)

    print(p1.get_info())
    print(p2.get_info())
    print(p3.get_info())


# test_func_middle_point()
test_point_plus()
