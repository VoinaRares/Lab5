from classes.identifier import Identifier


class Dish(Identifier):         # Base class for the Cooked Dish and the Beverage classes

    def __init__(self, portion_size: str, price: float):
        super().__init__()
        self.portion_size = portion_size
        self.price = price

    def __str__(self):
        return f'Id: {self.id}, portion size: {self.portion_size}, price: {self.price} '

    __repr__ = __str__
