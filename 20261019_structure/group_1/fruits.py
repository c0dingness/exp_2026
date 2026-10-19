class FruitId:
    id: int


class Pear:
    weight: int

    def __init__(self, id: FruitId):
        self.id = id
