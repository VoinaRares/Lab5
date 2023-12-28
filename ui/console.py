from classes.beverage import Beverage
from classes.order import Order
from classes.customer import Customer
from classes.cooked_dish import CookedDish


def menu():
    return """
            1 - Add new Order
            2 - View all Orders
            3 - Edit existing Order
            4 - Delete Order
            5 - Search Clients
            6 - Add Dish
            0 - Stop
            """


class Console:
    def __init__(self, customer_controller, cooked_dish_controller=None, beverage_controller=None,
                 order_controller=None):
        self.customer_controller = customer_controller
        self.cooked_dish_controller = cooked_dish_controller
        self.beverage_controller = beverage_controller
        self.order_controller = order_controller

    def add_order_console(self):

        customer_id = 0
        opt = int(input("""Is the customer new?
        1 - Yes
        2 - No
        Please enter your choice: """))
        if opt == 1:
            name = input("Name: ")
            address = input("Address: ")
            new_customer = Customer(name, address)
            customer_id = new_customer.id
            self.customer_controller.add_item(new_customer)
        elif opt == 2:
            print("Search for the new customer: ")
            customer_id = int(input("Enter customer id: "))

        dish_ids = []
        beverage_ids = []
        while True:
            print(self.cooked_dish_controller.view_items())
            print("-1 - Stop adding Dishes")
            try:
                dish_id = int(input("Enter the Dish id: "))
                if dish_id == -1:
                    break
                else:
                    dish_ids.append(dish_id)
                    print("Dish was added to the order")
            except ValueError:
                print("Invalid Value")

        while True:
            print(self.beverage_controller.view_items())
            print("-1 - Stop adding Beverages")
            try:
                beverage_id = int(input("Enter the Beverage id: "))
                if beverage_id == -1:
                    break
                else:
                    beverage_ids.append(beverage_id)
                    print("Beverage was added to the order")
            except ValueError:
                print("Invalid Value")
        return Order(customer_id, dish_ids, beverage_ids)

    def view_orders(self):
        return self.order_controller.view_items()

    def add_dish_console(self):
        print("1 - Cooked Dish\n2 - Beverage")
        while True:
            try:
                opt = int(input("Enter the option: "))
                break
            except ValueError:
                print("Invalid Value")
        if opt == 1:
            while True:
                try:
                    portion_size = input("Portion size: ")
                    price = int(input("Price: "))
                    time_needed = int(input("How many minutes: "))
                    self.cooked_dish_controller.add_item(CookedDish(portion_size, price, time_needed))
                    break
                except ValueError:
                    print("Invalid Value")
        if opt == 2:
            while True:
                try:
                    portion_size = input("Portion size: ")
                    price = int(input("Price: "))
                    alcohol_percentage = float(input("Alcohol percentage: "))
                    self.beverage_controller.add_item(Beverage(portion_size, price, alcohol_percentage))
                    break
                except ValueError:
                    print("Invalid Value")

    def run(self):
        while True:
            print(menu())
            while True:
                try:
                    opt = int(input("Please select an option: "))
                    break
                except ValueError:
                    print("Invalid Value! Please pick a number")

            if opt == 0:
                break

            if opt == 1:
                self.order_controller.add_item(self.add_order_console())
            if opt == 2:
                print(self.view_orders())

            if opt == 3:
                pass

            if opt == 4:
                pass

            if opt == 5:
                pass

            if opt == 6:
                self.add_dish_console()
