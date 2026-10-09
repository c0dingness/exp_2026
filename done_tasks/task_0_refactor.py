# Разработка
def calc_final_price(wanted_earn: float,
                     discount: float) -> float:
    final_price: float = wanted_earn / (1 - discount)
    return final_price


# Тестированием
def tests():
    print(calc_final_price(wanted_earn=333, discount=0.5))
    print(calc_final_price(wanted_earn=111, discount=0.5))
    x = calc_final_price(wanted_earn=444, discount=0.5)

    print(calc_final_price(wanted_earn=555, discount=0.5))
    pass


# Запуск тестов
if __name__ == '__main__':
    tests()
