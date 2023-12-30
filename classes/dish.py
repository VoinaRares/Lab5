from classes.identifier import Identifier


class Dish(Identifier):

    def __init__(self, portion_size: str, price: int):
        super().__init__()
        self.portion_size = portion_size
        self.price = price

    def __str__(self):
        return f'Id: {self.id}, portion size: {self.portion_size}, price: {self.price} '

    __repr__ = __str__