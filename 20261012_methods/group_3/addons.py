# FIGHT_CLUB_LITE
import random


class Player:
    name: str
    hp: float
    power: float

    def __init__(self, name: str):
        self.name = name

        magic_number = len(self.name)
        self.hp = 50 + magic_number * 2 + random.randint(1,magic_number)
        self.power = 10 + magic_number + random.randint(1, magic_number)

    def get_info(self):
        return f'{self.name}, hp:{self.hp}, power:{self.power}'

    def beat(self, other: 'Player'):
        other.receive_dmg(amount=self.power)

    def receive_dmg(self, amount):
        self.hp -= amount


class GameSession:
    def __init__(self, first: Player, second: Player):
        self.p1 = first
        self.p2 = second

    def start(self):
        self.p1.beat(other=self.p2)
        self.p2.beat(other=self.p1)


def test():
    p1 = Player(name='Biba')
    p2 = Player(name='Bibariy_the_third')

    print(p1.get_info())
    print(p2.get_info())

    gs = GameSession(first=p1,
                     second=p2)

    gs.start()


if __name__ == '__main__':
    test()
