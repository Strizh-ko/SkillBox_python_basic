import os


class File:

    def __init__(self, name, mode, encoding='utf-8'):
        self.name = name
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        if os.path.exists(self.name):
            self.file = open(self.name, self.mode, encoding=self.encoding)
        else:
            self.file = open(self.name, 'w', encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is not None:
            if exc_type is IOError or issubclass(IOError, exc_type):
                return True


with File('new-file.txt', 'a') as file:
    file.write('Ля-ля тополя!\n')