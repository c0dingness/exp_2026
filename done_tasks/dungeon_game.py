import random


class Enemy:
    hp: int
    damage: int

    def __init__(self):
        self.hp = random.randint(5, 12)
        self.damage = random.randint(2, 6)

    def is_alive(self) -> bool:
        return self.hp > 0

    def to_text(self) -> str:
        return f'health: {self.hp}, damage: {self.damage}'

    def receive_damage(self, amount):
        self.hp -= amount

    def deal_damage(self, player: 'Player'):
        amount = self.damage
        player.receive_damage(amount=amount)


class Player:
    hp: int
    damage: int

    def __init__(self):
        self.hp = random.randint(10, 22)
        self.damage = random.randint(7, 10)
        return

    def to_text(self) -> str:
        return f'health: {self.hp}, damage: {self.damage}'

    def is_alive(self) -> bool:
        return self.hp > 0

    def heal(self, amount):
        if not self.is_alive():
            return

        self.hp += amount

    def deal_damage(self, enemy: Enemy):
        amount = self.damage
        enemy.receive_damage(amount=amount)

    def receive_damage(self, amount):
        self.hp -= amount


class Room:
    def __init__(self, number):
        self.number = number
        self.monster1 = Enemy()
        self.monster2 = Enemy()

    def to_text(self):
        t1 = self.monster1.to_text()
        t2 = self.monster2.to_text()

        return (f'm1: {t1}\n'
                f'm2: {t2}')

    def get_enemy(self) -> Enemy | None:
        alive_monsters = []
        for m in [self.monster1, self.monster2]:
            if m.is_alive():
                alive_monsters.append(m)

        if len(alive_monsters) <= 0:
            return None

        return random.choice(alive_monsters)


class GameSession:
    def __init__(self):
        self.player = Player()

        # todo: можно указать с какой комнаты начнется game_session

        self.rooms = [
            Room(number=1),
            Room(number=2),
            Room(number=3),
        ]

        self.number_of_rooms = 3
        self.is_won = False

    def damage_exchange(self, room: Room):
        round_number = 0
        while True:
            round_number += 1
            print(f'room {room.number}, round: {round_number}')
            current_enemy = room.get_enemy()

            if current_enemy is None:
                print(f'No enemies in room: {room.number}')
                break

            self.player.deal_damage(enemy=current_enemy)

            if not current_enemy.is_alive():
                current_enemy.deal_damage(player=self.player)

            if not self.player.is_alive():
                print(f'Player is dead at room: {room.number}')
                break

    def heal_some_hp(self):
        random_number = random.randint(3, 6)
        print(f'healing player: {random_number}')
        self.player.heal(amount=random_number)

    def do_combat_phase(self, room: Room):
        self.damage_exchange(room)
        self.heal_some_hp()

    def go_through_rooms(self):
        for room in self.rooms:
            print(f'\n ROOM #{room.number}')
            print('=== before combat phase')
            print(f' p: {self.player.to_text()}')
            print(room.to_text())

            self.do_combat_phase(room=room)

            print('=== after combat phase')
            print(self.player.to_text())
            print(room.to_text())

            if not self.player.is_alive():
                return

        self.is_won = True

    def start(self):
        self.go_through_rooms()

        if self.is_won:
            print("ПОБЕДА!")
        else:
            print("ПОРАЖЕНИЕ!")


def test():
    gs = GameSession()
    gs.start()


test()
