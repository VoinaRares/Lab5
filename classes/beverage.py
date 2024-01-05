from classes.dish import Dish
from repository.beverage_repo import BeverageRepo

class Beverage(Dish):

    def __init__(self, portion_size: str, price: float, alcohol_percentage: float):
        super().__init__(portion_size, price)
        self.alcohol_percentage = alcohol_percentage
        br = BeverageRepo('beverage.txt')
        try:
            self.id = max(br.read()).id + 1
        except:
            self.id = 0

    def __str__(self):
        return super().__str__() + f'Alcohol percentage: {self.alcohol_percentage}\n'

    __repr__ = __str__
