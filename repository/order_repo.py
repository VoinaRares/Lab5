from repository.data_repo import DataRepo


class OrderRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)
