from ui.console import Console
from controller.controller import Controller
from repository.customer_repo import CustomerRepository
from repository.order_repo import OrderRepo
from repository.cooked_dish_repo import CookedDishRepo
from repository.beverage_repo import BeverageRepo

app = Console(Controller(CustomerRepository('customer.txt')), Controller(CookedDishRepo('cooked_dish.txt')),
              Controller(BeverageRepo('beverage.txt')), Controller(OrderRepo("order.txt")))


def main():
    app.run()


main()
