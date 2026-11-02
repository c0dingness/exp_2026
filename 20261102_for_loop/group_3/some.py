# массив

# C/C++ ... arr = []


# список
my_list = [-1, 2, 1000]

my_list_2 = list()
my_list_2.append(-1)  # 0
my_list_2.append(2)  # 1
my_list_2.append(1000)  # 2
my_list_2.append(9000)  # 3

print(my_list_2[0])  # первый элемент
print(my_list_2[-1])  # последний элемент
print(my_list_2[1:])
print(my_list_2[:-1])

# Методы: append / pop / remove / index

print('***')
print(my_list_2)
element = my_list_2.pop()
print(my_list_2)
print(element)

print('***')
print(my_list_2)
my_list_2.remove(2)
print(my_list_2)

my_list_2.append(777)

print('***')
print(my_list_2)
print(my_list_2.index(1000))

my_list_2.append(7771)
my_list_2.append(7772)

print(len(my_list))
print(len(my_list_2))


def print_list_contents(custom_list: list[int]):
    for x in custom_list:
        print(x)


print('***')
print_list_contents(custom_list=my_list_2)

print(my_list_2)

fruit_words = [
    'meadow',
    'peach',
    'apple',
    'strawberry',
]


def select_by_letters(words: list[str],
                      letter_count: int
                      ) -> list[str]:
    new_list = []
    for w in words:
        if len(w) == letter_count:
            new_list.append(w)
    return new_list


print(select_by_letters(words=fruit_words, letter_count=5))


class Job:
    def do(self):
        print(f'{id(self)} starting doing things')


jobs_list = [
    Job(),
    Job(),
    Job(),
    Job(),
    Job(),
]

for j in jobs_list:
    j.do()

print('***')  # start, stop, step
for i in range(3):
    # тело цикла
    print('koko')

print('***')
words = ['biba', 'boba', 'labuba']

n = 0
for w in words:
    n += 1
    print(f'{n} {w}')

for n, w in enumerate(words):
    print(f'{n} {w}')

print('***')

x = 0 # Как сделать так, чтобы 0 выводился?
numbers_to_pass = [30, 40]
while True:
    if x >= 70:
        break  # выход из цикла

    x += 10

    if x in numbers_to_pass:
        continue  # переход к следующему шагу итерации

    print(x)
