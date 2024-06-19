class HashTable:
    """
    A simple HashTable class to demonstrate basic functionalities.

    """

    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __len__(self):
        """
        Return the length of the HashTable.

        Returns:
            int: The size of the HashTable.
        """
        return self.size

    def _hash(self, key):
        """
        Compute the hash value for the given key using the modulo operation.
        
        Parameters:
            key: The key to compute the hash value for.
        
        Return:
            The hash value of the key.
        """
        return hash(key) % self.size

    def __setitem__(self, key, value):
        """
        Set the value at a specific key in the hash table.

        Parameters:
            key: The key to set the value at.
            value: The value to set.

        Return:
            None
        """
        index = self._hash(key)
        if self.data[index] is None:
            self.data[index] = []
        self.data[index].append([key, value])

    def __getitem__(self, key):
        """
        Retrieve the value associated with the given key from the hash table.

        Parameters:
            key: The key to retrieve the value for.

        Return:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found in the hash table.
        """
        index = self._hash(key)
        if self.data[index] is not None:
            for k, v in self.data[index]:
                if k == key:
                    return v
        raise KeyError

    def __delitem__(self, key):
        """
        Delete the key-value pair associated with the given key from the hash table.

        Parameters:
            key: The key to delete from the hash table.

        Return:
            None

        Raises:
            KeyError: If the key is not found in the hash table.
        """
        index = self._hash(key)
        if self.data[index] is not None:
            for k, v in self.data[index]:
                if k == key:
                    self.data[index].remove([k, v])
                    return
        raise KeyError

    def get(self, key, default=None):
        """
        Get the value associated with the given key.

        Parameters:
            key (Hashable): The key to retrieve the value for.
            default (Any, optional): The default value to return if the key is not found. Defaults to None.

        Returns:
            Any: The value associated with the key.

        Raises:
            KeyError: If the key is not found in the hash table.
        """
        try:
            return self[key]
        except KeyError:
            return default
