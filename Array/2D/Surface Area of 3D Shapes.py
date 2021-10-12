"""
892. Surface Area of 3D Shapes
Easy

You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.

Example 1:

Input: grid = [[2]]
Output: 10
Example 2:

Input: grid = [[1,2],[3,4]]
Output: 34
Example 3:

Input: grid = [[1,0],[0,2]]
Output: 16
Example 4:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50
"""
#34%
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        """
        Notes: Each cell populated with a positive value will contribute at least 2 to the surface area: the top and the bottom
        All 4 sides of each cube will need to be checked to see if the neighbor is taller or shorter
        If a neighbor is taller, the current position's side is not added to the surface area
        If a neighbor is shorter, the neighbor-current height is added to the surface area
        """
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #checkUp
                if i == 0:
                    answer += grid[i][j]
                elif grid[i-1][j] < grid[i][j]:
                    answer += grid[i][j]-grid[i-1][j]
                #print(answer)
                #checkLeft
                if j == 0:
                    answer += grid[i][j]
                elif grid[i][j-1] < grid[i][j]:
                    answer += grid[i][j]-grid[i][j-1]
                #print(answer)
                #CheckRight
                if j == len(grid[0])-1:
                    answer += grid[i][j]
                elif grid[i][j+1] < grid[i][j]:
                    answer += grid[i][j]-grid[i][j+1]
                #print(answer)
                #checkDown
                if i == len(grid)-1:
                    answer += grid[i][j]
                elif grid[i+1][j] < grid[i][j]:
                    answer += grid[i][j]-grid[i+1][j]
                #print(answer)
                #add 2 to the result
                if grid[i][j] > 0:
                    answer += 2
                #print(f"{i=} {j=} {grid[i][j]=} {answer=}")
        return answer

"""
sample 70 ms submission
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total = 0
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    total += (4 * grid[i][j] + 2)
                    
        for i in range(n):
            for j in range(n):
                if i > 0 and grid[i][j] <= grid[i-1][j]:
                    total -= 2 * grid[i][j]
                elif i > 0 and grid[i][j] > grid[i-1][j]:
                    total -= 2 * grid[i-1][j]
                    
                if j > 0 and grid[i][j] <= grid[i][j-1]:
                    total -= 2 * grid[i][j]
                elif j > 0 and grid[i][j] > grid[i][j-1]:
                    total -= 2 * grid[i][j-1]
                    
        return total
"""