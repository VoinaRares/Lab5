from controller.controller import Controller


class OrderController(Controller):
    def __init__(self, repo):
        super().__init__(repo)

    def validate_dish_id(self, dish_id, dish_option):
        items = self.repo.read()
        for item in items:
            if int(dish_option) == 1:
                element_count = item.dish_ids.count(dish_id)
                while element_count > 0:
                    item.dish_ids.remove(dish_id)
                    element_count -= 1
            if int(dish_option) == 2:
                element_count = item.dish_ids.count(dish_id)
                while element_count > 0:
                    item.beverage_ids.remove(dish_id)
                    element_count -= 1
        self.repo.save()

    def recalculate_price(self):
        items = self.repo.read()
        for item in items:
            item.calculate_price()
        self.repo.save()

    def validate_customer_id(self, customer_id):
        items = self.repo.read()
        for item in items:
            if int(customer_id) == int(item.customer_id):
                self.delete_item(item.id)

    def edit_order(self, item_id, customer_id, dish_ids, beverage_ids):
        self.repo.edit_order(item_id, customer_id, dish_ids, beverage_ids)
