class Hash_Table(object):
    def __init__(self, size=10):
        self.hash_table = [None] * size

    def get(self, key):
        try:
            for val in self.hash_table[self.hash(key)]:
                if val == key:
                    return val
        except KeyError:
            raise KeyError('key does not exist')
        raise KeyError("I don't know how, but this key has no value")

    def set(self, key, val):
        key_hash = self.hash(key)
        if self.hash_table[key_hash] is None:
            self.hash_table[key_hash] = [val]
        else:
            self.hash_table[key_hash].append(val)

    def hash(self, key):
        total = 0
        for c in key:
            total += ord(c)

        return total % len(self.hash_table)
