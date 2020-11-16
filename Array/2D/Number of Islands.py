"""
86%
200. Number of Islands
Medium

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        y_len = len(grid)
        x_len = len(grid[0])
        edit = [[0 for i in range(x_len)] for j in range(y_len)]
        def expand(pos):
            stack = [pos]
            edit[pos[1]][pos[0]] = 1
            while stack:
                temp = stack.pop()
                x = temp[0]
                y = temp[1]
                edit[y][x] = 1
                if x+1 < x_len and grid[y][x+1] == "1" and edit[y][x+1] == 0:
                    stack.append([x+1,y])
                if y+1 < y_len and grid[y+1][x] == "1" and edit[y + 1][x] == 0:
                    stack.append([x,y+1])
                if y - 1 >= 0 and grid[y - 1][x] == "1" and edit[y - 1][x] == 0:
                    stack.append([x, y - 1])
                if x - 1 >= 0 and grid[y][x - 1] == "1" and edit[y][x - 1] == 0:
                    stack.append([x - 1, y])
        ans = 0
        for i in range(y_len):
            for j in range(x_len):
                if grid[i][j] == "1" and edit[i][j] == 0:
                    ans += 1
                    expand([j,i])
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.numIslands(input1)
        print(ans)
        return ans

    assert test([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1
    assert test([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3
    assert test([["1","1","1"],["0","1","0"],["1","1","1"]]) == 1