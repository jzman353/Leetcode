"""
463. Island Perimeter
Easy

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""

#79%
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        self.ans += 1
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        self.ans += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        self.ans += 1
                    if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                        self.ans += 1

        return self.ans

"""
sample 424 ms submission
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row_idx, row in enumerate(grid):
            for col_idx, land in enumerate(row):
                if not land:
                    continue
                perimeter +=4
                
                if col_idx and row[col_idx-1]: #check for land in the prev cell of the same row (horizontally behind)
                    perimeter -=2
                
                if row_idx and grid[row_idx-1][col_idx]: #check for land just above
                    perimeter -=2
        return perimeter
"""