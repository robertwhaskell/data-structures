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
            for val in self.hash_table[self.hash(key)]:
                if val == key:
                    return val
        except KeyError:
            raise KeyError('key does not exist')
        raise KeyError("this key does not have a matching value")

    def set(self, key, val):
        '''
        Hash the key, place the value in the hashed bucket. If the bucket
        is not empty, append the value to the list of items in the bucket.
        '''
        if type(key) != str:
            raise TypeError('only accepts strings')

        if key != val:
            raise TypeError('key must equal value')

        key_hash = self.hash(key)
        if self.hash_table[key_hash] is None:
            self.hash_table[key_hash] = [val]
        else:
            self.hash_table[key_hash].append(val)

    def hash(self, key):
        '''Return a hashed value for the key'''
        total = 0
        for c in key:
            total += ord(c)

        return total % len(self.hash_table)
