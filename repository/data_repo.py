import pickle
import ast


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

    def convert_to_string(self, obj_list):
        obj_string_list = map(lambda x: pickle.dumps(x), obj_list)
        return list(obj_string_list)

    def convert_from_string(self, obj_string_list):
        obj_list = map(lambda x: pickle.loads(ast.literal_eval(x)), obj_string_list)
        return list(obj_list)

    def read_file(self, filename=None):
        if filename is None:
            self.read()
        else:
            f = open(filename, 'r')
            text = []
            for line in f:
                text.append(line)
            f.close()
            return text

    def write_file(self, text, filename=None):
        if filename is None:
            filename = self.filename
        else:
            f = open(filename, 'w')
            f.write(text)

    def delete_item(self, item_id):
        f = open(self.filename, 'rb')
        self.items = pickle.load(f)
        f.close()
        self.items = list(filter(lambda item: item.id != item_id, self.items))
        self.save()
