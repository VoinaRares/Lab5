class Controller:

    def __init__(self, repo):
        self.repo = repo

    def add_item(self, item):
        self.repo.add_item(item)

    def view_items(self):
        return self.repo.read()

    def find_items(self, search_term):
        items = self.repo.read()
        return filter(lambda item:
                      search_term.lower() in item.name.lower() or search_term.lower() in item.address.lower(), items)

    def find_by_id(self, item_id):
        items = self.repo.read()
        # return filter(lambda item: item_id == item.id, items)
        for item in items:
            if item.id == item_id:
                return item

    def delete_item(self, item_id):
        self.repo.delete_item(item_id)

    def edit_order(self, item_id, customer_id, dish_ids, beverage_ids):
        self.repo.edit_order(item_id, customer_id, dish_ids, beverage_ids)
