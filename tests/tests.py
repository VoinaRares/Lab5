from classes.cooked_dish import CookedDish
from classes.beverage import Beverage
from repository.cooked_dish_repo import CookedDishRepo
from repository.beverage_repo import BeverageRepo
from repository.customer_repo import CustomerRepository
from controller.customer_controller import CustomerController
from classes.order import Order
from repository.order_repo import OrderRepo


def test_adding_dish():
    """
    Test adding Cooked Dishes and Beverages
    :return:
    """
    cooked_dish_repo = CookedDishRepo('cooked_dish.txt')
    beverage_repo = BeverageRepo('beverage.txt')
    cooked_dish_repo.add_item(CookedDish('230g', 123, 120))
    beverage_repo.add_item(Beverage('260ml', 12, 12))
    assert cooked_dish_repo.load()[len(cooked_dish_repo.load()) - 1].portion_size == '230g'
    assert cooked_dish_repo.load()[len(cooked_dish_repo.load()) - 1].price == 123
    assert cooked_dish_repo.load()[len(cooked_dish_repo.load()) - 1].time_needed == 120
    assert beverage_repo.load()[len(beverage_repo.load()) - 1].portion_size == '260ml'
    assert beverage_repo.load()[len(beverage_repo.load()) - 1].price == 12
    assert beverage_repo.load()[len(beverage_repo.load()) - 1].alcohol_percentage == 12


def test_finding_customer():
    """
    Test the finding a customer by partial name or partial address
    :return:
    """
    customer_controller = CustomerController(CustomerRepository('customer.txt'))
    for term in customer_controller.find_items('Plop'):
        assert 'Plop' in term.address
        assert 'Plop' not in term.name

    for term in customer_controller.find_items('John'):
        assert 'John' in term.name
        assert 'John' not in term.address


def test_edit_customer_name():
    """
    Test the editing the customer name
    :return:
    """
    customer_controller = CustomerController(CustomerRepository('customer.txt'))
    customer_controller.edit_customer(3, "Changed", "Street")
    assert customer_controller.find_by_id(3).name == 'Changed'


def test_convert_and_save():
    """
    Creates an order and converts it into a string that represents a byte of an order.
    That string is then saved onto a file and then retrieved from the file
    The string is then converted into a byte again and used to retrieve the order that was originally saved
    :return:
    """
    order_repo = OrderRepo('order_file.txt')
    obj_list_string = order_repo.convert_to_string([Order(3, [1, 1, 0], [2, 3, 2]), Order(4, [3, 2, 1], [])])
    for obj in obj_list_string:
        order_repo.write_file(str(obj), 'order_file.txt')
    obj_list = order_repo.read_file('order_file.txt')
    obj_list = order_repo.convert_from_string(obj_list)
    for obj in obj_list:
        assert obj.customer_id == 4
        assert obj.dish_ids == [3, 2, 1]
        assert obj.beverage_ids == []


def test_receipt():
    new_order = Order(9, [0, 1, 1], [1, 1])
    receipt = new_order.show_receipt()
    assert receipt == """The 0. item                  24 Ron
The 1. item                  100 Ron
The 2. item                  100 Ron
The 3. item                  15 Ron
The 4. item                  15 Ron
The total of the order is    254.0 Ron"""
