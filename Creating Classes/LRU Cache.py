"""
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

100%
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            self.d.move_to_end(key, last=True)
            return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key, last=True)
        self.d[key] = value
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)

"""
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # key -> node
        # dummy head and tail so we never deal with null pointers
        self.head = Node()  # least recent
        self.tail = Node()  # most recent
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self._remove(self.map[key])
        self._insert_tail(self.map[key])
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        self.map[key] = Node(key, value)
        self._insert_tail(self.map[key])
        if len(self.map) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    # ============================================================
    # HIGHEST RISK CATEGORIES FOR LRU CACHE:
    # - Problem-specific traps: order of operations matters heavily
    # - Off-by-one: capacity boundaries (exactly at capacity, one over)
    # - Duplicate keys: put with existing key should update not add
    # - Recency tracking: get should count as "recently used"
    # - Return type: get must return int, put must return None
    # ============================================================

    def run_sequence(operations, arguments):
        results = []
        cache = None
        for op, args in zip(operations, arguments):
            if op == "LRUCache":
                cache = LRUCache(*args)
                results.append(None)
            elif op == "get":
                results.append(cache.get(*args))
            elif op == "put":
                cache.put(*args)
                results.append(None)
        return results


    # Test 1: [Minimum constraint / Example from problem]
    # Why: Validates the core example from the problem statement works end to end.
    assert run_sequence(
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    ) == [None, None, None, 1, None, -1, None, -1, 3, 4], "Test 1 failed: basic example"

    # Test 2: [Single element capacity]
    # Why: Capacity of 1 means every new put evicts the previous key.
    assert run_sequence(
        ["LRUCache", "put", "put", "get", "get"],
        [[1], [1, 1], [2, 2], [1], [2]]
    ) == [None, None, None, -1, 2], "Test 2 failed: capacity 1 evicts on every put"

    # Test 3: [Get missing key]
    # Why: get on a key that was never inserted should return -1.
    assert run_sequence(
        ["LRUCache", "get"],
        [[2], [1]]
    ) == [None, -1], "Test 3 failed: get on empty cache should return -1"

    # Test 4: [Put updates existing key]
    # Why: Putting an existing key should update value, not add a second entry.
    assert run_sequence(
        ["LRUCache", "put", "put", "get"],
        [[2], [1, 1], [1, 99], [1]]
    ) == [None, None, None, 99], "Test 4 failed: put should update existing key"

    # Test 5: [Put existing key does not grow cache]
    # Why: Updating an existing key should not count as a new entry, so no eviction should occur.
    assert run_sequence(
        ["LRUCache", "put", "put", "put", "get", "get"],
        [[2], [1, 1], [2, 2], [1, 99], [1], [2]]
    ) == [None, None, None, None, 99, 2], "Test 5 failed: updating key should not evict other keys"

    # Test 6: [Get marks as recently used]
    # Why: After get(1), key 2 should be LRU and evicted next, not key 1.
    assert run_sequence(
        ["LRUCache", "put", "put", "get", "put", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [1], [2]]
    ) == [None, None, None, 1, None, 1, -1], "Test 6 failed: get should mark key as recently used"

    # Test 7: [Put marks as recently used]
    # Why: After put(1, new_val), key 1 should be most recent, key 2 should be evicted next.
    assert run_sequence(
        ["LRUCache", "put", "put", "put", "get", "get"],
        [[2], [1, 1], [2, 2], [1, 10], [2], [1]]
    ) == [None, None, None, None, 2, 10], "Test 7 failed: put on existing key should mark as recently used"

    # Test 8: [Eviction order with capacity 3]
    # Why: Tests LRU ordering with larger capacity to catch off-by-one in eviction logic.
    assert run_sequence(
        ["LRUCache", "put", "put", "put", "put", "get", "get", "get"],
        [[3], [1, 1], [2, 2], [3, 3], [4, 4], [1], [2], [3]]
    ) == [None, None, None, None, None, -1, 2, 3], "Test 8 failed: capacity 3 eviction order"

    # Test 9: [Exactly at capacity, no eviction]
    # Why: Filling cache to exactly capacity should not trigger eviction.
    assert run_sequence(
        ["LRUCache", "put", "put", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [2]]
    ) == [None, None, None, 1, 2], "Test 9 failed: no eviction when at capacity"

    # Test 10: [One over capacity triggers eviction]
    # Why: Adding one more than capacity must evict exactly one item.
    assert run_sequence(
        ["LRUCache", "put", "put", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [3, 3], [1], [2], [3]]
    ) == [None, None, None, None, -1, 2, 3], "Test 10 failed: one over capacity should evict LRU"

    # Test 11: [All same value, different keys]
    # Why: Tests that key tracking works independently of value.
    assert run_sequence(
        ["LRUCache", "put", "put", "put", "get", "get"],
        [[2], [1, 42], [2, 42], [3, 42], [1], [2]]
    ) == [None, None, None, None, -1, 42], "Test 11 failed: same values different keys"

    # Test 12: [Zero as key]
    # Why: Key of 0 could break implementations using 0 as a sentinel value.
    assert run_sequence(
        ["LRUCache", "put", "get"],
        [[1], [0, 100], [0]]
    ) == [None, None, 100], "Test 12 failed: key 0 should work correctly"

    # Test 13: [Zero as value]
    # Why: Value of 0 could break implementations checking `if value` instead of `if value is not None`.
    assert run_sequence(
        ["LRUCache", "put", "get"],
        [[1], [1, 0], [1]]
    ) == [None, None, 0], "Test 13 failed: value 0 should be stored and returned correctly"

    # Test 14: [Large key and value]
    # Why: Tests upper constraint boundaries (key up to 10^4, value up to 10^5).
    assert run_sequence(
        ["LRUCache", "put", "get"],
        [[1], [10000, 100000], [10000]]
    ) == [None, None, 100000], "Test 14 failed: max key and value should work"

    # Test 15: [Interleaved gets and puts]
    # Why: Complex sequence tests that recency is tracked correctly across mixed operations.
    assert run_sequence(
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [2, 22], [2]]
    ) == [None, None, None, 1, None, -1, None, 22], "Test 15 failed: interleaved ops recency tracking"

    # Test 16: [Repeated gets on same key]
    # Why: Multiple gets on same key should keep returning correct value without side effects.
    assert run_sequence(
        ["LRUCache", "put", "get", "get", "get"],
        [[1], [1, 42], [1], [1], [1]]
    ) == [None, None, 42, 42, 42], "Test 16 failed: repeated gets should return same value"

    # Test 17: [Put same key repeatedly]
    # Why: Repeatedly updating same key should always reflect latest value.
    assert run_sequence(
        ["LRUCache", "put", "put", "put", "get"],
        [[1], [1, 1], [1, 2], [1, 3], [1]]
    ) == [None, None, None, None, 3], "Test 17 failed: repeated puts should update to latest value"

    # Test 18: [Evict then reinsert]
    # Why: A key that was evicted and reinserted should behave as a fresh entry.
    assert run_sequence(
        ["LRUCache", "put", "put", "put", "put", "get"],
        [[2], [1, 1], [2, 2], [3, 3], [1, 10], [1]]
    ) == [None, None, None, None, None, 10], "Test 18 failed: evicted key reinserted should return new value"

    # Test 19: [Return type check for get]
    # Why: get must return an int, not a string or other type.
    cache = LRUCache(1)
    cache.put(1, 42)
    result = cache.get(1)
    assert isinstance(result, int), "Test 19 failed: get should return int"

    # Test 20: [Return type check for put]
    # Why: put must return None.
    cache = LRUCache(1)
    result = cache.put(1, 1)
    assert result is None, "Test 20 failed: put should return None"

    # Test 21: [Idempotency - same cache state after repeated gets]
    # Why: Getting a key should never modify its value.
    cache = LRUCache(2)
    cache.put(1, 99)
    cache.put(2, 88)
    assert cache.get(1) == 99
    assert cache.get(1) == 99, "Test 21 failed: repeated get should not modify value"

    # Test 22: [LRU is updated on put of existing key, affects eviction]
    # Why: Re-putting key 1 should make key 2 the LRU, so key 2 gets evicted not key 1.
    assert run_sequence(
        ["LRUCache", "put", "put", "put", "put", "get", "get"],
        [[2], [1, 1], [2, 2], [1, 10], [3, 3], [1], [2]]
    ) == [None, None, None, None, None, 10, -1], "Test 22 failed: put existing key should update LRU order"

    print("All tests passed!")