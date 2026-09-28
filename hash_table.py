import random
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

        self.p = 109345121
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)


    def hash_function(self, key):
        return ((self.a * key + self.b) % self.p) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1
        if self.load_factor() > 0.75:
            self.resize()
    
    def search(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for existing_key, existing_value in bucket:
            if existing_key == key:
                return existing_value

        return None        
    
    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(i)
                self.count -= 1

                return True

        return False
    def load_factor(self):
        return self.count / self.size
    def resize(self):
        old_table = self.table
        self.size = self.size * 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
    
if __name__ == "__main__":
    hash_table = HashTable(size=3)  

    # Insert key-value pairs
    hash_table.insert(10, "Alice")
    hash_table.insert(20, "Bob")
    hash_table.insert(30, "Charlie")
    hash_table.insert(40, "David")
    hash_table.insert(50, "Eve")
    print("Table size:", hash_table.size)
    print("Number of items:", hash_table.count)
    print("Load factor:", hash_table.load_factor())
    print("Hash Table:")
    for i, bucket in enumerate(hash_table.table):
        print(f"Bucket {i}: {bucket}")

    # Search
    print("\nSearch for key 30:", hash_table.search(30))
    print("Search for key 99:", hash_table.search(99))

    # Delete
    print("\nDeleting key 20:", hash_table.delete(20))
    print("Search for key 20 after deletion:", hash_table.search(20))

    print("\nHash Table after deletion:")
    for i, bucket in enumerate(hash_table.table):
        print(f"Bucket {i}: {bucket}")

    print("\nCollision Test:")

    collision_table = HashTable(size=3)

    first_key = 10
    first_index = collision_table.hash_function(first_key)

    second_key = 11

    while collision_table.hash_function(second_key) != first_index:
        second_key += 1

    collision_table.insert(first_key, "First")
    collision_table.insert(second_key, "Second")

    for i, bucket in enumerate(collision_table.table):
        print(f"Bucket {i}: {bucket}")