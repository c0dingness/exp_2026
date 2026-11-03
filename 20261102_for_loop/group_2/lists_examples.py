# CRUD

# Create
my_list_1 = []
my_list_2 = list()

my_list_3 = [
    1,
    3,
    100,
]

my_list_3.append(9000)
my_list_3.append(777)
print(my_list_3)

# Read
print(my_list_3[0])
print(my_list_3[-1])
print(my_list_3[1:])
print(my_list_3[:-1])
print(my_list_3[1:-1])

# Read/Update

# append / pop / remove / index

print('***')
print(my_list_3)
last_element = my_list_3.pop(0)
print(last_element)
print(my_list_3)

# Delete
my_list_3.remove(9000)
print(my_list_3)

print(my_list_3.index(100))

print(len(my_list_1))
print(len(my_list_2))
print(len(my_list_3))

my_list_3.clear()
print(len(my_list_3))


class Job:
    def do(self):
        print(f'{id(self)} starting do things!')


jobs_list = [
    Job(),  # 140259094426880 starting do things!
    Job(),  # 140259094426928 starting do things!
    Job(),  # 140259094427072 starting do things!
    Job(),  # 140259094427168 starting do things!
    Job(),  # 140259094427216 starting do things!
]

for j in jobs_list:
    # Тело цикла
    j.do()


def select_words(words: list[str],
                 count_of_letters: int
                 ) -> list[str]:
    new_list = []

    for w in words:
        if len(w) == count_of_letters:
            new_list.append(w)

    return new_list


my_words = ['hi', 'my', 'some', 'night']
selection = select_words(words=my_words, count_of_letters=2)
print(selection)

for _ in range(3):
    print('koko-check-check')

my_words = ['hi', 'my', 'some', 'night']

counter = 0
for w in my_words:
    print(f'{counter}: {w}')
    counter += 1

for i, w in enumerate(my_words):
    print(f'{i}: {w}')

x = 0
number_to_pass = 50
while True:
    if x == number_to_pass:
        x += 10
        continue  # переход на следующий шаг итерации

    print(x)

    if x >= 100:
        break  # выход из цикла

    # Тело цикла

    x += 10
