from classes.identifier import Identifier
from repository.customer_repo import CustomerRepository


class Customer(Identifier):

    def __init__(self, name: str, address: str):
        super().__init__()
        self.name = name
        self.address = address
        cr = CustomerRepository('customer.txt')
        try:        # tries to make sure that the id doesn't repeat by checking the files that are already saved
            self.id = max(cr.read()).id + 1
        except:
            self.id = 0

    def __str__(self):
        return f'{self.id} {self.name} - {self.address}\n'

    __repr__ = __str__
