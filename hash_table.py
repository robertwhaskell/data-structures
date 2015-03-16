class Hash_Table(object):
    '''Class contains methods implementing a hash table.'''
    def __init__(self, size=10):
        self.hash_table = [None] * size

    def get(self, key):
        '''
        Search the buckets in the hash table for the key. Return the value if
        found. Raise an error if not.
        '''
        try:
            for val_tuple in self.hash_table[self.hash(key)]:
                if val_tuple[0] == key:
                    return val_tuple[1]
        except KeyError:
            raise KeyError('key does not exist')
        raise KeyError("this key does not have a matching value")

    def set(self, key, val):
        '''
        Hash the key, place the value in the hashed bucket. If the bucket
        is not empty, append the value to the list of items in the bucket.
        If the key is duplicate, overwrites previous key.
        if either the key or the val is not a string, throws an error.
        '''
        if type(key) != str:
            raise TypeError('only accepts strings')

        key_hash = self.hash(key)
        if self.hash_table[key_hash] is None:
            self.hash_table[key_hash] = [(key, val)]
        else:
            for i in range(len(self.hash_table[key_hash])):
                if self.hash_table[key_hash][i][0] == key:
                    self.hash_table[key_hash][i] = (key, val)
                    return
            self.hash_table[key_hash].append((key, val))

    def hash(self, key):
        '''Return a hashed value for the key'''
        total = 0
        for c in key:
            total += ord(c)

        return total % len(self.hash_table)
