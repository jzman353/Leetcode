"""
598. Range Addition II
Easy

You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
Example 2:

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
Example 3:

Input: m = 3, n = 3, ops = []
Output: 9
Constraints:

1 <= m, n <= 4 * 104
0 <= ops.length <= 104
ops[i].length == 2
1 <= ai <= m
1 <= bi <= n
"""
#100%
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        minx = ops[0][0]
        miny = ops[0][1]
        for i in range(1,len(ops)):
            minx = min(minx,ops[i][0])
            miny = min(miny,ops[i][1])
        return  minx*miny
#TLE
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]
        for i in ops:
            for j in range(i[0]):
                for k in range(i[1]):
                    grid[j][k] += 1
        flatten_list = list(chain.from_iterable(grid))
        c = Counter(flatten_list)
        return c[grid[0][0]]