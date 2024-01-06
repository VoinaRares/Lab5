from classes.dish import Dish
from repository.cooked_dish_repo import CookedDishRepo


class CookedDish(Dish):

    def __init__(self, portion_size: str, price: float, time_needed: int):
        super().__init__(portion_size, price)
        self.time_needed = time_needed
        cdr = CookedDishRepo('cooked_dish.txt')
        try:        # tries to make sure that the id doesn't repeat by checking the files that are already saved
            self.id = max(cdr.read()).id + 1
        except:
            self.id = 0

    def __str__(self):
        return super().__str__() + f"Time needed: {self.time_needed}\n"

    __repr__ = __str__
