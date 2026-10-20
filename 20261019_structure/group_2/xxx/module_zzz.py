def my_little_function():
    print('my_little_function')
    return None

def f():
    print('...!!!!')


def tests():
    print('MY TESTS')
    my_little_function()
    f()

if __name__ == '__main__':
    print(f'__name__ = {__name__}')
    print('DIRECT')
    tests()
else:
    print(f'__name__ = {__name__}')
