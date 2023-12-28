from repository.data_repo import DataRepo


class CustomerRepository(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

