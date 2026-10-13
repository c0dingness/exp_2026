# fight club lite (prototype)
import random


class Player:
    def __init__(self, name: str):
        self.name = name

        super_secret_number = len(name)

        self.hp = 50 + random.randint(1, super_secret_number) * 10
        self.power = 10 + random.randint(1, super_secret_number) * 2

    def get_info(self):
        return f'{self.name}: hp: {self.hp}, power: {self.power}'

    def beat(self, target: 'Player'):
        print(f'player {self.name} beats {target.name}')
        target.receive_damage(amount=self.power)

    def receive_damage(self, amount):
        self.hp -= amount


class GameSession:

    def __init__(self, first: Player,
                 second: Player):
        self.p1 = first
        self.p2 = second

    def start(self):
        print('Game begins!')
        self.p1.beat(target=self.p2)
        self.p2.beat(target=self.p1)


def tests():
    p1 = Player(name='Biba')
    p2 = Player(name='Bibery_the_third')

    print(p1.get_info())
    print(p2.get_info())

    gs = GameSession(first=p1,
                     second=p2)

    gs.start()

    print(p1.get_info())
    print(p2.get_info())


if __name__ == '__main__':
    tests()
