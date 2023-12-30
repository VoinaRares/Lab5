from repository.data_repo import DataRepo


class CookedDishRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

    def edit_cooked_dish(self, item_id, portion_size, price, time_needed):
        self.items = self.load()
        for item in self.items:
            if item_id == item.id:
                item.portion_size = portion_size
                item.price = price
                item.time_needed = time_needed
                break
        self.save()
