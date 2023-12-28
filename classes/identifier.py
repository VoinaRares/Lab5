class Identifier:
    id_count = 0

    def __init__(self):
        self.id = Identifier.id_count
        Identifier.id_count += 1

