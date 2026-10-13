hp = 0.0

if hp <= 0:
    print('dead')
else:
    print('alive')


class Player:
    hp: float

    def is_dead(self) -> bool:
        if self.hp <= 0:
            return True
        else:
            return False




import random


def random_100(digits: int = 2):
    multiplier = 10 ** digits

    number = random.randint(1, 100 * multiplier)
    return number / multiplier


for i in range(5):
    print(f'{i} {random_100(3)}')


import math

x = 12.34567
tail, head = math.modf(x)
print(tail)  # 0.345
print(head)  # 12.0


# def tests():
#     # .... часть псведокода игры next door farmer
#     for _ in range(10):
#         meadow.next_day()
#
#         player.drop_water(target=plant_1)
#         player.drop_water(target=plant_2)
#         player.drop_water(target=plant_3)



