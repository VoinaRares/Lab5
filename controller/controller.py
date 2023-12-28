class Controller:

    def __init__(self, repo):
        self.repo = repo

    def add_item(self, item):
        self.repo.add_item(item)

    def view_items(self):
        return self.repo.read()
