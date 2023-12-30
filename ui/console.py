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
            7 - CRUD Customer
            8 - CRUD Dish
            0 - Stop
            """


def crud():
    return """
            1 - Add
            2 - View
            3 - Edit
            4 - Delete
           """


def new_customer():
    name = input("Name: ")
    address = input("Address: ")
    new_cust = Customer(name, address)
    return new_cust


class Console:
    def __init__(self, customer_controller, cooked_dish_controller, beverage_controller,
                 order_controller):
        self.customer_controller = customer_controller
        self.cooked_dish_controller = cooked_dish_controller
        self.beverage_controller = beverage_controller
        self.order_controller = order_controller

    def delete_order(self):
        print(self.view_orders())
        order_id = int(input("Choose which order to delete by ID: "))
        self.order_controller.delete_item(order_id)

    def crud_customer(self, opt):
        if opt == 1:
            customer = new_customer()
            self.customer_controller.add_item(customer)
        if opt == 2:
            print(self.customer_controller.view_items())
        if opt == 3:
            self.find_customer()
            customer_id = int(input("Choose the customer by ID: "))
            customer = self.customer_controller.find_by_id(customer_id)
            while True:
                print("What do you want to edit?\n1-Name\n2-Address\n0-Stop")
                edit_option = int(input("Choose the option: "))
                if edit_option == 1:
                    name = input("Name: ")
                    customer.name = name
                if edit_option == 2:
                    address = input("Address: ")
                    customer.address = address
                if edit_option == 0:
                    break
            self.customer_controller.edit_customer(customer.id, customer.name, customer.address)
        if opt == 4:
            self.find_customer()
            customer_id = int(input("Choose the customer by ID: "))
            self.customer_controller.delete_item(customer_id)

    def crud_operations(self, class_option):
        print(crud())
        opt = int(input("Choose which: "))
        if class_option == 7:
            self.crud_customer(opt)

    def edit_order(self):
        print(self.view_orders())
        order_id = int(input("Choose which order to edit by ID: "))
        order = self.order_controller.find_by_id(order_id)
        while True:
            print("1 - Edit cooked dishes\n2 - Edit beverages\n3 - Edit customer\n0 - Stop")
            option = int(input("Please choose: "))
            if option == 1:
                dish_ids = self.dish_ids_to_list()
                order.dish_ids = dish_ids
            if option == 2:
                beverage_ids = self.beverage_ids_to_list()
                order.beverage_ids = beverage_ids
            if option == 3:
                self.find_customer()
                customer_id = int(input("Choose new customer by ID: "))
                order.customer_id = customer_id
            if option == 0:
                break
        self.order_controller.edit_order(order.id, order.customer_id, order.dish_ids, order.beverage_ids)
        print("The order has been edited", order)

    def dish_ids_to_list(self):
        dish_ids = []
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
        return dish_ids

    def beverage_ids_to_list(self):
        beverage_ids = []
        while True:
            print(self.beverage_controller.view_items())
            print("-1 - Stop adding Beverages")
            try:
                beverage_id = int(input("Enter the Beverage id: "))
                if beverage_id == -1:
                    break
                else:
                    beverage_ids.append(beverage_id)            # Check if the id exists
                    print("Beverage was added to the order")
            except ValueError:
                print("Invalid Value")
        return beverage_ids

    def find_customer(self):
        print("Search for the new customer: ")
        search_term = input("Search: ")
        possible_terms = self.customer_controller.find_items(search_term)
        print("Our current customers are: \n")
        for term in possible_terms:
            print(term.id, term.name, term.address)

    def customer_id_for_order(self):
        customer_id = 0
        opt = int(input("""Is the customer new?
                1 - Yes
                2 - No
                Please enter your choice: """))
        if opt == 1:
            customer = new_customer()
            self.customer_controller.add_item(customer)
            customer_id = customer.id
        elif opt == 2:
            self.find_customer()
            customer_id = input("Customer ID: ")
        return customer_id

    def add_order_console(self):

        customer_id = self.customer_id_for_order()
        dish_ids = self.dish_ids_to_list()
        beverage_ids = self.beverage_ids_to_list()
        return Order(customer_id, dish_ids, beverage_ids)

    def view_orders(self):
        return self.order_controller.view_items()

    def add_dish_console(self):     # restructurare
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
                self.edit_order()
            if opt == 4:
                self.delete_order()
            if opt == 5:
                self.find_customer()
            if opt == 6:
                self.add_dish_console()
            if opt == 7:
                self.crud_operations(opt)
            if opt == 8:
                pass
