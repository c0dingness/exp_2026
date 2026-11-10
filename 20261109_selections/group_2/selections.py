# x = 5

# print(x == 5)
# print(x != 5)
# print(x > 5)
# print(x < 5)
# print(x >= 5)
# print(x <= 5)
# print(x is None)
# print(x is not None)
# print(x in [1,4,5])


def is_into_range(a, b, x) -> bool:
    return a <= x <= b


def has_element(custom_list, element) -> bool:
    return element in custom_list


print(is_into_range(1, 10, 5))
print(is_into_range(1, 10, 11))
print(is_into_range(1, 10, -1))


class WordProcessor:
    def __init__(self, word):
        if not isinstance(word, str):  # СТОРОЖЕВОЙ ПУНКТ
            raise ValueError('Must me str type')

        self.word = word

    def process(self):
        return self.word.upper()

    def process_with(self, another_word: str):
        if not len(another_word) >= 32:
            raise ValueError()

        pass


def do_some_with_number(x: int) -> int:
    if x < 0:
        x = abs(x)

    return x * 3


wp = WordProcessor(word='biba')
print(wp.process())


def bingo_function(word: str):
    # var #1
    is_word_accepted = (
            len(word) >= 5 or
            word.islower() or
            word.isalpha()
    )

    # var #2
    conditions = [
            len(word) >= 5,
            word.islower(),
            word.isalpha(),
    ]
    is_word_accepted =any(conditions)

    # ...
    if is_word_accepted:
        print('bingo!')

    return

print('***')
bingo_function(word='lamp')