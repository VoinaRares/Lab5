from controller.controller import Controller


class CookedDishController(Controller):
    def __init__(self, repo):
        super().__init__(repo)

    def edit_cooked_dish(self, cooked_dish_id, portion_size, price, time_needed):
        self.repo.edit_cooked_dish(cooked_dish_id, portion_size, price, time_needed)
