#8%
"""
Random Flip Matrix (Medium)

You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

Note:

    1 <= n_rows, n_cols <= 10000
    0 <= row.id < n_rows and 0 <= col.id < n_cols
    flip will not be called when the matrix has no 0 values left.
    the total number of calls to flip and reset will not exceed 1000.

Example 1:

Input:
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]

Example 2:

Input:
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.manual = False
        if self.n_rows * self.n_cols < 1000:
            self.manual = True
            self.matrix = [[0 for i in range(n_cols)] for j in range(n_rows)]
            self.possibilities = [[i,j] for i in range(n_rows) for j in range(n_cols)]
        else:
            self.off_limits = []

    def flip(self):
        import random
        if self.manual and self.possibilities:
            row, col = random.choice(self.possibilities)
            self.matrix[row][col] = 1
            self.possibilities.remove([row,col])
            return [row,col]
        if not self.manual:
            while(1):
                row = random.randint(0,self.n_rows-1)
                col = random.randint(0,self.n_cols-1)
                if [row,col] not in self.off_limits:
                    self.off_limits.append([row,col])
                    return [row, col]


    def reset(self) -> None:
        if self.manual:
            self.matrix = [[0 for i in range(self.n_cols)] for j in range(self.n_rows)]
            self.possibilities = [[i, j] for i in range(self.n_rows) for j in range(self.n_cols)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()

if __name__ == '__main__':
    def test(input1,input2):
        Test = Solution(input1, input2)
        ans = Test.flip()
        print(ans)
        ans = Test.flip()
        print(ans)
        ans = Test.flip()
        print(ans)
        ans = Test.flip()
        print(ans)
        Test.reset()
        ans = Test.flip()
        print(ans)


    n_rows = 1
    n_cols = 1
    test(n_rows,n_cols)
    n_rows = 2
    n_cols = 2
    test(n_rows, n_cols)
    n_rows = 2
    n_cols = 3
    test(n_rows, n_cols)
    n_rows = 3
    n_cols = 2
    test(n_rows, n_cols)
    n_rows = 4
    n_cols = 4
    test(n_rows, n_cols)
    n_rows = 1000
    n_cols = 750
    test(n_rows, n_cols)

import timeit
print(timeit.timeit("test(10000,10000)", setup="from __main__ import test", number=3))

"""
class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.c = n_cols
        self.t = n_rows * n_cols - 1
        self.s = 0
        self.d = {}

    def flip(self) -> List[int]:
        r = random.randint(self.s, self.t)
        res = self.d.get(r, r)
        self.d[r] = self.d.get(self.s, self.s)
        self.d[self.s] = res
        self.s += 1
        return divmod(res, self.c)

    def reset(self) -> None:
        self.s = 0
"""