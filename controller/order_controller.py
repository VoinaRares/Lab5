from controller.controller import Controller


class OrderController(Controller):
    def __init__(self, repo):
        super().__init__(repo)

    def validate_dish_id(self, dish_id, dish_option):
        """
        When a dish is deleted, the method is used to verify if all the ids in the Orders still exist
        :param dish_id: the id of the dish that was deleted
        :param dish_option: Option that checks if the dish is a Cooked Dish(1) or a Beverage(2)
        :return:
        """
        items = self.repo.read()
        for item in items:
            if int(dish_option) == 1:
                element_count = item.dish_ids.count(dish_id)
                while element_count > 0:
                    item.dish_ids.remove(dish_id)
                    element_count -= 1
            if int(dish_option) == 2:
                element_count = item.beverage_ids.count(dish_id)
                while element_count > 0:
                    item.beverage_ids.remove(dish_id)
                    element_count -= 1
        self.repo.save()

    def recalculate_price(self):
        """
        Calculates the price of all the orders that are saved in the file
        :return:
        """
        items = self.repo.read()
        for item in items:
            item.calculate_price()
        self.repo.save()

    def validate_customer_id(self, customer_id):
        """
        When a customer is deleted, then the method also deletes all the orders that were associated with that customer
        :param customer_id: the id of the customer that was just deleted
        :return:
        """
        items = self.repo.read()
        for item in items:
            if int(customer_id) == int(item.customer_id):
                self.delete_item(item.id)

    def edit_order(self, item_id, customer_id, dish_ids, beverage_ids):
        self.repo.edit_order(item_id, customer_id, dish_ids, beverage_ids)
