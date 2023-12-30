from repository.data_repo import DataRepo


class CustomerRepository(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

    def edit_customer(self, customer_id, name, address):
        self.items = self.load()
        for item in self.items:
            if customer_id == item.id:
                item.id = customer_id
                item.name = name
                item.address = address
                break
        self.save()
