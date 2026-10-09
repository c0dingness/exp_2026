class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_info(self):
        return f'x:{self.x}, y:{self.y}'


def calculate_the_middle(p1: Point, p2: Point) -> Point:
    x = (p1.x + p2.x) / 2
    y = (p1.y + p2.y) / 2
    p = Point(x, y)
    return p


def test():
    p1 = Point(2, 4)
    p2 = Point(8, 10)
    p3 = calculate_the_middle(p1=p1, p2=p2)

    print(p1.get_info())
    print(p2.get_info())
    print(p3.get_info())


test()
