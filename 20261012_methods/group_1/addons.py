import random


# FIGHT_CLUB_LITE

class Player:
    name: str

    hp: float
    power: float

    def __init__(self, name: str):
        self.name = name

        number = len(name)
        self.hp = 10 * random.randint(1, number)
        self.power = 1 * random.randint(3, 3 + number)

    def get_info(self):
        return f'{self.name}: hp={self.hp}, power={self.power}'

    def beat(self, other: 'Player'):
        dmg = self.power / 10
        other.receive_damage(dmg)

    def receive_damage(self, dmg):
        self.hp -= dmg


class GameSession:
    p1: Player
    p2: Player

    def __init__(self, first_player: Player,
                 second_player: Player):
        self.p1 = first_player
        self.p2 = second_player

    def start(self):
        print('GAME STARTS!')
        self.p1.beat(other=self.p2)
        self.p2.beat(other=self.p1)


def tests():
    p1 = Player('Biba')
    p2 = Player('Bibiborii_the_third')

    print(p1.get_info())
    print(p2.get_info())

    gs = GameSession(first_player=p1,
                     second_player=p2)

    gs.start()

    print(p1.get_info())
    print(p2.get_info())


if __name__ == '__main__':
    tests()
