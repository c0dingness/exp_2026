# Операторы

x = 3


# print(x == 5)
# print(x != 5)
# print(x >= 5)
# print(x <= 5)
# print(x < 5)
# print(x < 5)


# 0 <= x <= 5
# проверка на вхождение в диапазон
def into_range(a, b, x) -> bool:
    return a <= x <= b



def calculate(x):
    if not isinstance(x, float):
        return 0

    if x < 0:
        x = abs(x)

    return x + 67


def exp(word: str):
    conditions = [
        len(word) >= 5, # True
        word.isalpha(), # True
        word.islower(), # True
    ]

    if any(conditions):
        print(f'{word}: any bingo!')

    if all(conditions):
        print(f'{word}: all bingo!')

if __name__ == '__main__':
    exp(word='12345')
    exp(word='palma')




