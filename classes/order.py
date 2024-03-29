from classes.identifier import Identifier
from repository.cooked_dish_repo import CookedDishRepo
from repository.beverage_repo import BeverageRepo
from repository.order_repo import OrderRepo
import functools


class Order(Identifier):

    def __init__(self, customer_id: int, dish_ids: list, beverage_ids: list):
        super().__init__()
        self.customer_id = customer_id
        self.dish_ids = dish_ids
        self.beverage_ids = beverage_ids
        self.price = 0
        self.calculate_price()
        order_repo = OrderRepo('order.txt')
        try:        # tries to make sure that the id doesn't repeat by checking the files that are already saved
            self.id = max(order_repo.read()).id + 1
        except:
            self.id = 0

    def __dishes_list(self):
        """
        A private methode for creating a list of all the prices of the cooked dishes and beverages that are in an order
        :return: A list of float numbers representing the prices
        """
        cooked_dish_repo = CookedDishRepo('cooked_dish.txt')
        beverage_repo = BeverageRepo('beverage.txt')
        dishes = ([dish.price for dish_id in self.dish_ids for dish in cooked_dish_repo.load() if dish.id == dish_id] +
                  [beverage.price for beverage_id in self.beverage_ids for beverage in beverage_repo.load()
                   if beverage_id == beverage.id])
        return dishes

    def calculate_price(self):
        """
        A methode for calculating the price of the order based on the dish and beverage ids
        :return:
        """
        dishes = self.__dishes_list()
        try:
            self.price = functools.reduce(lambda a, b: float(a) + float(b), dishes)
        except TypeError:
            self.price = 0

    def __create_receipt(self):
        """
        A private methode for creating how the receipt should look like
        :return: A string representing the receipt
        """
        dishes = self.__dishes_list()
        indexes = [x for x in range(len(dishes))]
        receipt = map(lambda a, b: f"The {b}. item                  {a} Ron", dishes, indexes)
        receipt = '\n'.join(list(receipt))
        return receipt + f"\nThe total of the order is    {self.price} Ron"

    def show_receipt(self):
        return self.__create_receipt()

    def __str__(self):
        return (f"Order {self.id}: Customer Id: {self.customer_id}, Dish Ids: {self.dish_ids} , Beverage Ids:"
                f" {self.beverage_ids}, Price: {self.price}\n")

    __repr__ = __str__
