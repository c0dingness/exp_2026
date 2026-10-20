class Banana:
    weight: int


def tests():
    b = Banana()
    print(id(b))
    # ...


if __name__ == '__main__':
    tests()
    print(f'__name__ = {__name__}')
else:
    print(f'__name__ = {__name__}')
