# Вариант №3

# Функции расчета для каждой комнаты

def calc_area_toilet():
    toilet_length = 1.4
    toilet_width = 1.5
    toilet_space = toilet_length * toilet_width

    return toilet_space


def calc_area_small_room():
    small_room_length = 2
    small_room_width = 3
    small_room_space = small_room_length * small_room_width

    return small_room_space


def calc_area_hall_horizontal():
    hall_horizontal_length = 8
    hall_horizontal_width = 1.5
    hall_horizontal_space = hall_horizontal_length * hall_horizontal_width

    return hall_horizontal_space


def calc_area_hall_vertical():
    hall_vertical_length = 1.5
    hall_vertical_width = 6.0
    hall_vertical_space = hall_vertical_length * hall_vertical_width

    return hall_vertical_space


def calc_area_big_room():
    big_room_length = 3
    big_room_width = 3.5
    big_room_space = big_room_length * big_room_width

    return big_room_space


def calc_area_huge_room():
    huge_room_length = 6
    huge_room_width = 4.5
    huge_room_space = huge_room_length * huge_room_width

    return huge_room_space


# Функция расчета общей площади

def total():
    total_space = (calc_area_toilet() +
                   calc_area_small_room() +
                   calc_area_hall_horizontal() +
                   calc_area_hall_vertical() +
                   calc_area_big_room() +
                   calc_area_huge_room())

    return total_space


# Тестовая функция

def tests():
    total_area = total()
    print(f'Итоговая площадь: {total_area} квадратных метров')


# Код для запуска тестовой функции

if __name__ == '__main__':
    tests()
