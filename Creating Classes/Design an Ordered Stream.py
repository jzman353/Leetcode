"""
1656. Design an Ordered Stream
Easy

There are n (id, value) pairs, where id is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that takes the n pairs in an arbitrary order, and returns the values over several calls in increasing order of their ids.

Implement the OrderedStream class:

    OrderedStream(int n) Constructs the stream to take n values and sets a current ptr to 1.
    String[] insert(int id, String value) Stores the new (id, value) pair in the stream. After storing the pair:
        If the stream has stored a pair with id = ptr, then find the longest contiguous incrementing sequence of ids starting with id = ptr and return a list of the values associated with those ids in order. Then, update ptr to the last id + 1.
        Otherwise, return an empty list.

Example:

Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation
OrderedStream os= new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].

Constraints:

    1 <= n <= 1000
    1 <= id <= n
    value.length == 5
    value consists only of lowercase letters.
    Each call to insert will have a unique id.
    Exactly n calls will be made to insert.
"""

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [0 for i in range(n)]
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id - 1] = value
        ind = -1
        for i in range(self.ptr, len(self.stream)):
            if self.stream[i] == 0:
                ind = i
                break
        if self.ptr == len(self.stream):
            pass
        elif ind == -1:
            temp = self.ptr
            self.ptr = len(self.stream)
            return self.stream[temp:]
        elif self.stream[self.ptr] != 0:
            temp = self.ptr
            self.ptr = ind
            return self.stream[temp:ind]
        else:
            return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
"""
class OrderedStream:

    def __init__(self, n: int):
        self.d = {}
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        if id == self.ptr:
            ans = [value]
            while (id+1) in self.d:
                ans.append(self.d[id+1])
                id += 1
            self.ptr = id+1
            return ans 
        self.d[id] = value
"""