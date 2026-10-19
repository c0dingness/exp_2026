# Описание класса
class Banana:
    weight: float

    def __init__(self, weight: float):  # метод вызывается при создании объекта
        self.weight = weight
        print('Pear was created!')

# Описание класса
class Lemur:
    name: str  # поле
    age: int  # also поле

    def tell_about(self, message: str = ''):  # описание метода внутри класса
        print(f'{id(self)}, name:{self.name}, age:{self.age}')

        if not message == '':
            print(message)

    def feed(self, banana: Banana):
        print(f'Lemur named {self.name} ate banana {id(banana)}')


lem1 = Lemur()  # создание объекта + ...
lem1.name = 'Karl'  # задание значения полю
lem1.age = 19  # также задание значения
lem1.tell_about()  # вызов метода
Lemur.tell_about(self=lem1)  # вызов метода через одно место


banana_test_1 = Banana(weight=1.5)
banana_test_2 = Banana(weight=2.5)

lem1.feed(banana=banana_test_1)
lem1.feed(banana=banana_test_2)

lem2 = Lemur()
lem2.name = 'Henry'
lem2.age = 25
lem2.tell_about()
lem2.tell_about(message='yatta!')

