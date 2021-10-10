"""
705. Design HashSet
Easy

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:

0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
"""
#90%
class MyHashSet:

    def __init__(self):
        self.d = {}

    def add(self, key: int) -> None:
        self.d[key] = 1

    def remove(self, key: int) -> None:
        if key in self.d.keys():
            del self.d[key]

    def contains(self, key: int) -> bool:
        return key in self.d.keys()


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

'''
#Apparently sets are even faster than my inplimentation using a dictionary
sample 116 ms submission
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s=set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if(key in self.s):
            return True
        return False

#not sure what a bytearray is
sample 145 ms submission
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = bytearray(1000001)


    def add(self, key: int) -> None:
        if not self.arr[key]:
            self.arr[key] = True


    def remove(self, key: int) -> None:
        if self.arr[key]:
            self.arr[key]=False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if self.arr[key]:
            return True
        else:
            return False

sample 170 ms submission
class MyHashSet:

    def __init__(self):
        self.array = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        subkey = key%1000
        if not self.contains(key):
            self.array[subkey].append(key)

    def remove(self, key: int) -> None:
        subkey = key%1000
        if self.contains(key):
            self.array[subkey].remove(key)
        

    def contains(self, key: int) -> bool:
        subkey = key%1000
        return key in self.array[subkey]
'''