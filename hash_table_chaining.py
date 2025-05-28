import random

class HashTableChaining:
    """
    Hash Table implementation using chaining for collision resolution.
    Uses a universal hash function to minimize collisions.

    Attributes:
        size (int): Number of buckets in the table.
        table (list): List of lists for chaining.
        p (int): A large prime for universal hashing.
        a, b (int): Random coefficients for universal hash function.
    """

    def __init__(self, size=101):
        """
        Initialize the hash table with a given size and universal hash function parameters.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]
        # Universal hash function parameters
        self.p = 10**9 + 7  # Large prime
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _hash(self, key):
        """
        Universal hash function for integer and string keys.
        Converts string keys to integer via built-in hash().
        """
        if isinstance(key, int):
            key_hash = key
        else:
            key_hash = hash(key)
        # Universal hash function: ((a * key + b) mod p) mod size
        return ((self.a * key_hash + self.b) % self.p) % self.size

    def insert(self, key, value):
        """
        Insert or update a key-value pair into the hash table.
        If the key already exists, its value is updated.
        """
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        """
        Retrieve the value associated with a given key, or None if not found.
        """
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Remove the key-value pair associated with the given key, if it exists.
        """
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __str__(self):
        """
        String representation for debugging.
        """
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"Bucket {i}: {bucket}")
        return "\n".join(result) if result else "Empty hash table"

# --------- Example usage and edge case tests ---------
if __name__ == "__main__":
    h = HashTableChaining(size=11)  # Small table for testing

    # Insert keys of different types and repeated values
    h.insert("apple", 1)
    h.insert("banana", 2)
    h.insert(10, "ten")
    h.insert("apple", 99)    # Update existing key

    print("Hash Table after insertions:")
    print(h)

    # Search for present and missing keys
    print("Search 'apple':", h.search("apple"))   # Should return 99
    print("Search 'banana':", h.search("banana")) # Should return 2
    print("Search 42:", h.search(42))             # Should return None

    # Delete a key
    print("Delete 'banana':", h.delete("banana")) # Should return True
    print("Delete 'banana' again:", h.delete("banana")) # Should return False

    print("Hash Table after deletions:")
    print(h)
