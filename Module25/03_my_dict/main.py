class MyDict(dict):
    def __init__(self, dct):
        super().__init__()
        self.dct = dct

    def get_elem(self, key):
        return self.dct.get(key, 0)

dct = MyDict({1:101, 2:102, 3:103})
print(dct.get_elem(4))