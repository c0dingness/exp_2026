import xxx
# НОРМ, но такое себе
# from xxx.module_x import my_little_function, f

# Самый адеватный способ

# ПОЛЬЗОВАТЕЛИ ПАКЕТА xxx
import xxx as mx


def my_little_function():
    print('!!!')


def main():
    print('main starts!')

    mx.my_little_function()

    b = xxx.Banana()
    b.weight = 333


main()