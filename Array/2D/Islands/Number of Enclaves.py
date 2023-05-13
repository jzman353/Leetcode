"""
1020. Number of Enclaves
Medium

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""

#35%
class Solution:
    def numEnclaves(self, grid) -> int:
        y_len = len(grid)
        x_len = len(grid[0])
        self.seen = [[0 for i in range(x_len)] for j in range(y_len)]
        ans = 0

        def expand(pos):
            stack = set()
            stack.add(pos)
            island_value = 0
            edge_found = False
            while stack:
                island_value += 1
                temp = stack.pop()
                x = temp[0]
                y = temp[1]
                if x == 0 or x == x_len - 1 or y == 0 or y == y_len - 1:
                    edge_found = True
                self.seen[y][x] = 1
                if x + 1 < x_len and grid[y][x + 1] == 1 and self.seen[y][x + 1] == 0:
                    stack.add((x + 1, y))
                if y + 1 < y_len and grid[y + 1][x] == 1 and self.seen[y + 1][x] == 0:
                    stack.add((x, y + 1))
                if y - 1 >= 0 and grid[y - 1][x] == 1 and self.seen[y - 1][x] == 0:
                    stack.add((x, y - 1))
                if x - 1 >= 0 and grid[y][x - 1] == 1 and self.seen[y][x - 1] == 0:
                    stack.add((x - 1, y))
            return island_value if not edge_found else 0

        for i in range(y_len):
            for j in range(x_len):
                if grid[i][j] == 1 and self.seen[i][j] == 0:
                    ans += expand((j, i))
                    print(j,i,ans)

        return ans

"""
#This method zeros out everything connected to an edge and then sums up the remaining 1s
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j] = 0
            if i > 0 and grid[i-1][j]:
                dfs(i-1, j)
            if i < m-1 and grid[i+1][j]:
                dfs(i+1, j)
            if j > 0 and grid[i][j-1]:
                dfs(i, j-1)
            if j < n-1 and grid[i][j+1]:
                dfs(i, j+1)
        for i in range(m):
            if grid[i][0]:
                dfs(i, 0)
            if grid[i][n-1]:
                dfs(i, n-1)
        for j in range(1, n-1):
            if grid[0][j]:
                dfs(0, j)
            if grid[m-1][j]:
                dfs(m-1, j)
        
        return sum(sum(row) for row in grid)
"""

if __name__ == '__main__':

    def test(input1):
        Test = Solution()
        ans = Test.numEnclaves(input1)
        print(ans)
        return ans

    #assert test([[1, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1]]) == 1
    #assert test([[1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]) == 25

    import random
    def testCases():
        m = random.randint(10,200)
        n = random.randint(10,200)
        grid = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = random.choices([0,1], weights=[2,1], k=1)[0]
        print(grid)


    for i in range(8):
        testCases()
