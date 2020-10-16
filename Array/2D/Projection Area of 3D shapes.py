"""
883. Projection Area of 3D Shapes
Easy

On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.



Example 1:

Input: [[2]]
Output: 5

Example 2:

Input: [[1,2],[3,4]]
Output: 17
Explanation:
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

Example 3:

Input: [[1,0],[0,2]]
Output: 8

Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14

Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21



Note:

    1 <= grid.length = grid[0].length <= 50
    0 <= grid[i][j] <= 50
"""

#73%
class Solution:
    def projectionArea(self, grid) -> int:
        x = 0
        y = 0
        z = 0
        for i,row in enumerate(grid):
            y += max(row)
            for j in grid[i]:
                if j>0:
                    z += 1
        for j in range(len(grid[0])):
            x += max([sub[j] for sub in grid])
        return x+y+z

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.projectionArea(input1)
        print(ans)
        return ans

    assert test([[2]]) == 5
    assert test([[1,2],[3,4]]) == 17
    assert test([[1,0],[0,2]]) == 8
    assert test([[1,1,1],[1,0,1],[1,1,1]]) == 14
    assert test([[2,2,2],[2,1,2],[2,2,2]]) == 21

"""
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            res += max(row)
        res += sum([max([i[x] for i in grid]) for x in range(len(grid[0]))])
        res += len(grid) * len(grid[0]) - sum([row.count(0) for row in grid])
        return res   
"""