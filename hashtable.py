
class HashTable:

    def __init__(self):
        self.hashtable = [[]]
        for i in range(10):
            self.hashtable.append([])

    # Create a hash key which should run in O(1)
    # Explain with comments what the "with" does and why you are using this
    def get_hash_value(self, key):
        return int(key) % 10

    # Insert package into hash table which should run in O(n)
    # Explain with comments what the "with" does and why you are using this
    def package_insert(self, new_package_insert):
       key_hash = self.get_hash_value(new_package_insert.package_id)
       self.hashtable[key_hash].append(new_package_insert)

    def package_find(self, key):
        key_hash = self.get_hash_value(key)
        for p in self.hashtable[key_hash]:
            if p.package_id == key:
                return p
        return None

    def package_search(self, package_id):
        pass

