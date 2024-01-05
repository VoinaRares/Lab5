from ui.console import Console
from controller.controller import Controller
from repository.customer_repo import CustomerRepository
from repository.order_repo import OrderRepo
from repository.cooked_dish_repo import CookedDishRepo
from repository.beverage_repo import BeverageRepo
from tests.tests import test_adding_dish, test_finding_customer, test_edit_customer_name, test_receipt, test_convert_and_save
from classes.customer import Customer

app = Console(Controller(CustomerRepository('customer.txt')), Controller(CookedDishRepo('cooked_dish.txt')),
              Controller(BeverageRepo('beverage.txt')), Controller(OrderRepo("order.txt")))


def tests():
    # test_adding_dish()
    test_finding_customer()
    test_edit_customer_name()
    test_receipt()
    test_convert_and_save()


tests()

# c = Customer('John', 'Str lui')
# cr = CustomerRepository('customer.txt')
# s = cr.convert_to_string([c, c, c])
# lists = cr.convert_from_string(s)
# print(lists)
# print(cr.read_file('customer_file.txt'))
# print(cr.read_file())
# cr.write_file('Customer: 1 Order: 16', 'customer_file.txt')


def main():
    app.run()


main()
