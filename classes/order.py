from classes.identifier import Identifier
from repository.cooked_dish_repo import CookedDishRepo
from repository.beverage_repo import BeverageRepo


class Order(Identifier):

    def __init__(self, customer_id: int, dish_ids: list, beverage_ids: list):
        super().__init__()
        self.customer_id = customer_id
        self.dish_ids = dish_ids
        self.beverage_ids = beverage_ids
        self.price = 0
        self.calculate_price()

    def calculate_price(self):
        cooked_dish_repo = CookedDishRepo('cooked_dish.txt')
        beverage_repo = BeverageRepo('beverage.txt')
        for dish_id in self.dish_ids:
            pass

    def __create_receipt(self):
        pass

    def show_receipt(self):
        pass

    def __str__(self):
        return (f"Order {self.id}: Customer Id: {self.customer_id}, Dish Ids: {self.dish_ids} , Beverage Ids:"
                f" {self.beverage_ids}, Price: {self.price}\n")

    __repr__ = __str__
