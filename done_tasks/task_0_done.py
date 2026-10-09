# Ход решения
#
# Простой пример:
# 100 * (1-0.2) = 80
#
# Именование переменных
# user_price * (1 - discount) = wanted_earn

# Исходные
wanted_earn: float = 80
discount: float = 0.2

# Обработка данных, решение задачки
final_price: float = wanted_earn / (1 - discount)

# Вывод
print(final_price)
