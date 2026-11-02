# массивы
# C: arr = []

# списки

my_list = list()
my_list.append(1)
my_list.append(3)
my_list.append(7)
my_list.append(9)

print(my_list[0])
print(my_list[-1])
print(my_list[1:])
print(my_list[:-1])


class StudentAttendanceMark:
    def __init__(self, name):
        self.name: str = name
        self.is_offline = False
        self.is_online = False


group_list = [
    StudentAttendanceMark(name='Biba'),
    StudentAttendanceMark(name='Boba')
]

# append / pop / remove / index


my_list = ['a', 'b', 'g', 'w']

my_list.append('ko')

print(my_list)
element = my_list.pop()
print(my_list)
print(element)

my_list.remove('b')
print(my_list)

print(my_list.index('g'))

print(len(my_list))


def select_words(words: list[str],
                 letters_count: int) -> list[str]:
    new_list = list()
    for w in words:
        w = w.strip()
        if len(w) == letters_count:
            new_list.append(w)

    return new_list


words_to_test = ['banana  ', 'sky', 'beaver']

selection = select_words(words=words_to_test,
                         letters_count=6)

print(selection)

words_to_test = ['banana', 'sky', 'beaver']

for w in words_to_test:
    w_mod = w.upper()
    print(w_mod)

for _ in range(10):
    print('kokokok')

words_to_test = ['banana', 'sky', 'beaver']

counter = 0
for x in words_to_test:
    print(counter, x)
    counter += 1

for counter, x in enumerate(words_to_test):
    text = x.upper()
    print(counter, text)

x = 0
while x < 100:
    x += 10
    print(x)


x = 0
miss_numbers = [50 , 60]
while True:
    if x < 100:
        break

    if x in miss_numbers:
        continue

    x += 10
    print(x)





