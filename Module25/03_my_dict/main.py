class MyDict(dict):
    def __init__(self, dct):
        super().__init__()
        self.dct = dct

    def get(self, key, default=0):
        return self.dct.get(key, default)

dct = MyDict({1:101, 2:102, 3:103})
print(dct.get(4))