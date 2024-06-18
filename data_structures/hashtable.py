class HashTable:
    """
    A simple HashTable class to demonstrate basic functionalities.

    """

    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __len__(self):
        return self.size

    def _hash(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self._hash(key)
        if self.data[index] is None:
            self.data[index] = []
        self.data[index].append([key, value])

    def __getitem__(self, key):
        index = self._hash(key)
        if self.data[index] is not None:
            for k, v in self.data[index]:
                if k == key:
                    return v
        raise KeyError

    def __delitem__(self, key):
        index = self._hash(key)
        if self.data[index] is not None:
            print("hello")
            for k, v in self.data[index]:
                if k == key:
                    self.data[index].remove([k, v])
                    return
        raise KeyError
