miss_numbers = [50, 60, 100]
x = 0
while True:
    if x > 100:  # условия прерывания цикла
        # print('log: breaking loop')
        break

    x += 10
    # print('log: x changed')

    if x in miss_numbers:  # условие пропуска цифры 50
        # print('log: number pass triggered')
        continue

    print(x)
    # print('log: x printed')