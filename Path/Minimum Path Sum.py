"""
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.squares = defaultdict(lambda:math.inf)
        self.m = len(grid)
        self.n = len(grid[0])
        self.stack = deque()
        def helper(grid,pos,curr):
            if curr < self.squares[pos[0]*self.n+pos[1]]:
                self.squares[pos[0]*self.n+pos[1]] = curr
                for i in [[pos[0]+1,pos[1]],[pos[0],pos[1]+1]]:
                    if i[0] < self.m and i[1] < self.n:
                        loc = -1
                        for j in range(len(self.stack)):
                            if self.stack[j][2] > curr+grid[i[0]][i[1]]:
                                loc = j
                                break
                        self.stack.insert(loc,(grid,i,curr+grid[i[0]][i[1]]))
        helper(grid,[0,0],grid[0][0])
        while self.stack:
            params = self.stack.popleft()
            helper(params[0],params[1],params[2])
        return self.squares[self.m*self.n-1]
"""
#TLE
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.squares = defaultdict(lambda:math.inf)
        self.m = len(grid)
        self.n = len(grid[0])
        self.stack = deque()
        def helper(grid,pos,curr):
            if curr < self.squares[pos[0]*self.n+pos[1]]:
                self.squares[pos[0]*self.n+pos[1]] = curr
                for i in [[pos[0]+1,pos[1]],[pos[0],pos[1]+1]]:
                    if i[0] < self.m and i[1] < self.n:
                        if pos[0]+pos[1] > len(self.stack):
                            loc = -1
                        else:
                            loc = pos[0]+pos[1]
                        self.stack.insert(loc,(grid,i,curr+grid[i[0]][i[1]]))
        helper(grid,[0,0],grid[0][0])
        while self.stack:
            params = self.stack.popleft()
            helper(params[0],params[1],params[2])
        return self.squares[self.m*self.n-1]
"""
"""
TLE
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.squares = defaultdict(lambda:math.inf)
        self.m = len(grid)
        self.n = len(grid[0])
        def helper(grid,pos,curr):
            if curr < self.squares[pos[0]*self.n+pos[1]]:
                self.squares[pos[0]*self.n+pos[1]] = curr
                for i in [[pos[0]+1,pos[1]],[pos[0],pos[1]+1]]:
                    if i[0] < self.m and i[1] < self.n:
                        helper(grid,i,curr+grid[i[0]][i[1]])
        helper(grid,[0,0],grid[0][0])
        return self.squares[self.m*self.n-1]
"""

"""
sample 73 ms submission
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [grid[i] for i in range(m)]
        
        for i in range(1,n):
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= min(dp[i][j-1],dp[i-1][j])+grid[i][j]
        
        return dp[m-1][n-1]
"""