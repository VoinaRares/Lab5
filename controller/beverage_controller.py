from controller.controller import Controller


class BeverageController(Controller):
    def __init__(self, repo):
        super().__init__(repo)

    def edit_beverage(self, beverage_id, portion_size, price, alcohol_percentage):
        self.repo.edit_beverage(beverage_id, portion_size, price, alcohol_percentage)
