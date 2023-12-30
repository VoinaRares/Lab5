from repository.data_repo import DataRepo


class OrderRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

    def edit_order(self, item_id, customer_id, dish_ids, beverage_ids):
        self.items = self.load()
        for item in self.items:
            if item_id == item.id:
                item.customer_id = customer_id
                item.dish_ids = dish_ids
                item.beverage_ids = beverage_ids
                item.calculate_price()
                break
        self.save()
