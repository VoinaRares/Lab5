from classes.identifier import Identifier
from repository.customer_repo import CustomerRepository


class Customer(Identifier):

    def __init__(self, name: str, address: str):
        super().__init__()
        self.name = name
        self.address = address
        cr = CustomerRepository('customer.txt')
        try:
            self.id = max(cr.read()).id + 1
        except:
            self.id = 0

    def __str__(self):
        return f'{self.id} {self.name} - {self.address}'

    def __lt__(self, other):
        return self.id < other.id

    __repr__ = __str__
