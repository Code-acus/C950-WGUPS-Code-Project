# Hash map class

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = []
        for value in range(capacity):
            self.table.append([])

    # Create a hash key which should run in O(1)
    def new_hash_key(self, key):
        return int(key) % len(self.capacity)

    # Insert package into hash table which should run in O(n)
    def package_insert(self, key, value):
        key_hash = self.create_key_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Get package from hash table which should run in O(n)

