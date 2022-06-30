# Hash Table Class

class HashTable:
    def __init__(self, capacity):
        self.map = None
        self.capacity = capacity
        self.table = []
        for value in range(capacity):
            self.table.append([])

    # Create a hash key which should run in O(1)
    # Explain with comments what the "with" does and why you are using this
    def new_hash_key(self, key):
        return int(key) % len(self.capacity)

    # Insert package into hash table which should run in O(n)
    # Explain with comments what the "with" does and why you are using this
    def package_insert(self, key, value, key_hash=None):
        self.create_key_hash(key)
        key_value = [key, value]

        # Add comments about the following code - what are you doing with this code and why?
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
    # Explain what you are doing with this code and why you are using
    def hash_table_update(self, key, value, key_value=None, pair=None, key_hash=None):
        self.create_key_hash(key)
        if self.map[key_hash] is None and pair[0] == key:
            pair[1] = key_value
            return True
        else:
            print("There was an error updating the hash table" + key)

    # Added by the suggested code from PyCharm
    def create_key_hash(self, key):
        pass

    # Get a value from the hash table which should run in O(n)
    # Explain what you are doing with this code and why you are using
    def get_hashtable_value(self, key):
        key_hash = self.new_hash_key(key)
        if self.map[key_hash] is None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
            return None

    # Delete a value from the hash table which should run in O(n)
    # Explain what you are doing with this code and why you are using
    def delete_hashtable_value(self, key):
        key_hash = self.new_hash_key(key)
        if self.map[key_hash] is None:
            return False
        else:
            for i in range(len(self.map[key_hash])):
                if self.map[key_hash][i] == key:
                    self.map[key_hash].remove(i)
                    return True
        return False


class HashTableCreate:
    def __init__(self, key, package):
        self.key = key
        self.package = package
