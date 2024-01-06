class Identifier:       # Base class for Dish, Order and Customer
    id_count = 0

    def __init__(self):
        self.id = Identifier.id_count
        Identifier.id_count += 1

    def __lt__(self, other):
        return self.id < other.id
