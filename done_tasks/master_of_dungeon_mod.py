import enum
import random


class Item:
    def use(self, target: 'GameActor'):
        raise NotImplemented()


class HealingPotion(Item):
    def use(self, target: 'GameActor'):
        hp = random.randint(3, 10)

        print(f"Restoring {hp} HP to {target.u_name} {target.name}")
        target.heal(hp=hp)


class GameActor:
    u_name = 'Actor'

    def __init__(self, name: str, hp: int, base_power: int):
        self.name = name
        self.hp = hp
        self.base_power = base_power

    def get_possible_damage(self):
        return self.base_power

    def do_damage(self, target: 'GameActor'):
        damage_to_deal = self.get_possible_damage()

        print(f"{self.u_name} {self.name} trying "
              f"to do {damage_to_deal} damage "
              f"to {target.u_name} {target.name}")

        target.receive_damage(damage=damage_to_deal)

    def receive_damage(self, damage: int):
        self.hp -= damage

        print(f"{self.u_name} {self.name} received {damage} "
              f"and have {self.hp} hp")

    def use_buff(self, item: Item):
        item.use(target=self)

    def heal(self, hp):
        self.hp += hp

    def is_dead(self):
        return self.hp <= 0

    def get_info(self):
        return f'{self.u_name} name:{self.name}; hp: {self.hp}; bp:{self.base_power}'


class Player(GameActor):
    u_name = 'Player'


class Monster(GameActor):
    u_name = 'Monster'


class RoomStatus(enum.StrEnum):
    not_passed = 'not passed'
    passed_alive = 'passed alive'
    dead_while_passing = 'dead while passing'


class Room:
    def __init__(self, name: str, monsters: list[Monster]):
        self.name = name
        self.monsters = monsters
        self.__status = RoomStatus.not_passed

    def get_status(self):
        return self.__status

    def begin_battle(self, player: Player):
        print(f"\n===== You have entered into {self.name} =====")
        print(player.get_info())
        is_player_turn = True

        while True:
            if player.is_dead():
                print(f'{player.u_name} {player.name} is dead, leaving battle')
                break

            if any(m.is_dead() for m in self.monsters):
                print(f'All monsters are dead, leaving battle')
                break

            live_monsters = [m for m in self.monsters if not m.is_dead()]

            if is_player_turn:
                target_monster = random.choice(live_monsters)
                player.do_damage(target_monster)
                is_player_turn = False
            else:
                for monster in live_monsters:
                    monster.do_damage(player)

                    if player.is_dead():
                        print(f'{monster.u_name} {monster.name} '
                              f'defeats {player.u_name} {player.name}')
                        break

                is_player_turn = True

        if player.is_dead():
            print("The player has died.")
            self.__status = RoomStatus.dead_while_passing
        else:
            print(f"All monsters in {self.name} were defeated!")

            healing_potion = HealingPotion()
            player.use_buff(item=healing_potion)

            self.__status = RoomStatus.passed_alive


class MonsterFactory:
    # Как интерфейс
    def create_random_monster(self) -> Monster:
        raise NotImplemented()

    def create_monsters(self) -> list[Monster]:
        raise NotImplemented()


class OrcMonsterFactory(MonsterFactory):
    def __init__(self):
        self.counter = 0
        self.limit = 1000
        self.alphabet: list[str] = list('abcdefghijklmnopqrstuvwxyz')

    def generate_word(self) -> str:
        word = ''
        for _ in range(3):
            letter: str = random.choice(self.alphabet)
            word += letter.upper()

        return word

    def create_random_monster(self) -> Monster:
        self.counter += 1

        if self.counter >= self.limit:
            return Monster(name='Baby orc', hp=1, base_power=1)

        word = self.generate_word()
        name = f'Orc [{word}]'
        hp = random.randint(40, 60)
        bp = random.randint(10, 20)
        orc = Monster(name=name, hp=hp, base_power=bp)

        return orc

    def create_monsters(self) -> list[Monster]:
        monster_count = random.randint(1, 3)
        return [self.create_random_monster() for _ in range(monster_count)]


class GameSession:
    def __init__(self, player: Player, monster_factory: OrcMonsterFactory):
        self.player = player

        mf = monster_factory
        rooms = random.randint(2, 4)

        self.rooms = []
        for i in range(rooms):
            self.rooms.append(Room(
                name=f'Room #{i + 1}',
                monsters=mf.create_monsters()
            ))

    def start(self):
        print("Game start")

        for room in self.rooms:
            room.begin_battle(self.player)

            room_status = room.get_status()

            if room_status is RoomStatus.dead_while_passing:
                print("You lose.")
                return

            if room_status is RoomStatus.passed_alive:
                print(f"You win in Room {room.name}")

            if room_status is RoomStatus.not_passed:
                print(f'Something goes wrong, room passing interrupted somehow')
                return

        print("\nYou passed all rooms! Victory!")


if __name__ == '__main__':
    # tests
    test_player = Player("Fin", 150, base_power=20)
    session = GameSession(test_player, monster_factory=OrcMonsterFactory())
    session.start()
