import pickle


class DataRepo:
    def __init__(self, filename):
        self.filename = filename
        self.items = []
        self.load()

    def save(self):
        f = open(self.filename, 'wb')
        pickle.dump(self.items, f)

        f.close()

    def load(self):
        try:
            f = open(self.filename, 'rb')
            self.items = pickle.load(f)
            f.close()
        except:
            self.items = []
        return self.items

    def read(self):
        self.load()
        # print(self.items)
        return self.items

    def add_item(self, item):
        self.items.append(item)
        self.save()

    def delete_item(self, item_id):
        f = open(self.filename, 'rb')
        self.items = pickle.load(f)
        f.close()
        self.items = list(filter(lambda item: item.id != item_id, self.items))
        self.save()
