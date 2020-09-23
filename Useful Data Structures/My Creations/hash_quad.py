class HashTable:

    def __init__(self, table_size):             # can add additional attributes
        self.table_size = table_size            # initial table size
        self.hash_table = [None]*table_size     # hash table for storing values
        self.key_table = [None]*table_size      # table for storing key values
        self.num_items = 0                      # empty hash table

    # HT str data -> None
    # Inserts data into HT according to Horner's Hash and quadratic probing
    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        slot = self.horner_hash(key)
        if self.key_table[slot] == None:
            self.key_table[slot] = key
            self.hash_table[slot] = value
        else:
            if self.key_table[slot] == key:
                self.hash_table[slot] = value
            else:
                newSlot = self.rehash(key, slot)
                self.key_table[newSlot] = key
                self.hash_table[newSlot] = value

        self.num_items += 1
        lFactor = self.get_load_factor()
        if lFactor > 0.5:
            # adjust the tables
            self.hash_table.extend([None] * (self.table_size + 1))
            self.key_table.extend([None] * (self.table_size + 1))
            self.table_size = (2 * self.table_size) + 1
            # rehash everything
            index = 0
            self.num_items = 0

            nKeys = []
            nVals = []
            while index < ((self.table_size - 1) / 2):
                if self.key_table[index] != None:
                    nKeys.append(self.key_table[index])
                    nVals.append(self.hash_table[index])
                    self.key_table[index] = None
                    self.hash_table[index] = None
                index += 1
            for i in range(len(nKeys)):
                self.insert(nKeys[i], nVals[i])

            '''
            while index < ((self.table_size - 1)/2):
                if self.key_table[index] != None:
                    nKey = self.key_table[index]
                    nVal = self.hash_table[index]
                    self.key_table[index] = None
                    self.hash_table[index] = None
                    self.insert(nKey, nVal)
                index += 1
            '''

    # HT str -> int
    # Computes the hash value for the entry
    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        # p = ord(key[0])
        # n = min(len(key), 8)
        # i = n - 2
        # j = n - 1 - i
        # while j >= 0:
        #     p = p * 31 + ord(key[j])
        #     j -= 1
        # print(p)
        # return p
        slot = 0
        n = min(len(key), 8)
        for i in range(0, n):
            slot += ord(key[i]) * 31**(n - 1 - i)
        return slot % self.get_table_size()

    # HT str -> bool
    # Returns true if key is in the HT, false otherwise
    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        slot = self.get_index(key)
        if slot == None:
            return False
        return True

    # HT str -> int
    # Returns index of key in HT, returns None if not in HT
    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        slot = self.horner_hash(key)
        if self.key_table[slot] == key:
            return slot
        else:
            newSlot = self.rehash(key, slot)
            if self.key_table[newSlot] == key:
                return newSlot
        return None

    # HT -> keyList
    # Returns all the keys in HT, in order
    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        keys = []
        for item in self.key_table:
            if item != None:
                keys.append(item)
        return keys

    # HT str -> element
    # Returns the value associated with a key. Returns None if not in HT
    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        index = self.get_index(key)
        if index == None:
            return None
        return self.hash_table[index]

    # HT -> int
    # Returns number of keys in HT
    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    # HT -> int
    # Returns size of HT
    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    # HT -> float
    # Returns the load factor on HT as a decimal
    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return 1.0 * self.get_num_items()/self.get_table_size()

    # HT -> int
    # Rehashes in case of collisions using quadratic probing
    def rehash(self, key, hash):
        probe = 1
        newHash = hash
        while self.key_table[newHash] != None and self.key_table[newHash] != key:
            newHash = (hash + probe**2) % self.get_table_size()
            probe += 1
        return newHash