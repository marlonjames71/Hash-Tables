#!/usr/bin/env python3
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # if self.storage[index] != None:
        #     print(f"There is already a value here at: {index}")
        # else:
        #     self.storage[index] = (key, value)
            
        pair = self.storage[index]
        if pair is not None:
            if pair.key != key:
                print("Warning: Overwriting value")
                pair.key = key
                pair.value = value
            else:
                self.storage[index] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)
        # if self.storage[index] == None:
        #     print(f"Value with given key: {key}, does not exist")
        # else:
        #     self.storage[index] = None
            
        # Get the index from hashmod
        index = self._hash_mod(key)
        # Check if a pair exists in the bucket with matching keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # if so, return the value
            self.storage[index] = None
        else:
            print("Warning: Key does not exists")

        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Get the index from hashmod
        index = self._hash_mod(key)
        # Check if a pair exists in the bucket with matching keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # if so, return the value
            return self.storage[index].value
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
