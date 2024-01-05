from controller.controller import Controller


class CustomerController(Controller):
    def __init__(self, repo):
        super().__init__(repo)

    def find_items(self, search_term):
        items = self.repo.read()
        return filter(lambda item:
                      search_term.lower() in item.name.lower() or search_term.lower() in item.address.lower(), items)


    def edit_customer(self, customer_id, name, address):
        self.repo.edit_customer(customer_id, name, address)