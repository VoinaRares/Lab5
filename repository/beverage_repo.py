from repository.data_repo import DataRepo


class BeverageRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

    def edit_beverage(self, item_id, portion_size, price, alcohol_percentage):
        self.items = self.load()
        for item in self.items:
            if item_id == item.id:
                item.portion_size = portion_size
                item.price = price
                item.alcohol_percentage = alcohol_percentage
                break
        self.save()
