x = 5

print(x == 5)
print(x != 5)
print(x >= 5)
print(x <= 5)
print(x > 5)
print(x < 5)

if 5 <= x <= 10:
    print('!!!')


def is_fit_into_range(begin, end, x: float) -> bool:
    # guard point
    if not isinstance(begin, float):
        return False

    if not isinstance(end, float):
        return False

    return begin <= x <= end


result = is_fit_into_range(begin=3.0, end=10.0, x=5)
print(result)


# def xxx(word: str):
#
#     if word.islower():
#         print('A')
#     elif len(word) >= 5:
#         print('B')
#     else:
#         print('C')


def process_word(word: str):
    condition = (
            len(word) >= 5 and
            word.isalpha() and
            word.islower()
    )


    conditions = [
        len(word) >= 5, # T
        word.isalpha(), # T
        word.islower(), # T
    ]
    condition = any(conditions)

    if condition:
        print('bingo!')

process_word(word='palma')
process_word(word='palm')