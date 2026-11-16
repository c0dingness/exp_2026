some_list = ['bee',
             'cat',
             'dog',
             'zebra',
             'giraffe',
             'tux',
             'ze']
some_list2 = some_list.copy()

print(some_list)
some_list.sort()
print(some_list)
some_list.sort(key=lambda x: len(x))
print(some_list)

sss = sorted(some_list2, key=lambda x: len(x))
