class ArrayList:

    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.data[:self.size])

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of bounds")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def add(self, value):
        if self.size == len(self.data):
            # double the size
            self._resize(2 * len(self.data))
        self.data[self.size] = value
        self.size += 1

    def remove(self, index):
        if 0 <= index < self.size:
            for i in range(index, self.size - 1):
                self.data[i] = self.data[i + 1]
            self.data[self.size - 1] = None
            self.size -= 1

            # Resize the array if it's too empty to save space
            if 0 < self.size < len(self.data) // 4:
                self._resize(len(self.data) // 2)
        else:
            raise IndexError("Index out of bounds")
