"""
On a 2-dimensional grid, there are 4 types of squares:

    1 represents the starting square.  There is exactly one starting square.
    2 represents the ending square.  There is exactly one ending square.
    0 represents empty squares we can walk over.
    -1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.



Note:

    1 <= grid.length * grid[0].length <= 20

"""


class Solution:
    def uniquePathsIII(self, grid) -> int:
        row_num = len(grid)
        col_num = len(grid[0])
        self.neighbors = []

        # Find starting and ending points
        for row in range(row_num):
            for col in range(col_num):
                if grid[row][col] == 1:
                    self.start = [row, col]
                if grid[row][col] == 2:
                    self.end = [row, col]

        seen = [[0 for i in range(col_num)] for j in range(row_num)]

        #loc is list. loc[0] is row # and loc[1] is col #
        def find_neighbors(loc):
            neighbors = self.neighbors.pop()
            if loc[0]-1 >= 0 and seen[loc[0]-1][loc[1]] == 0:
                neighbors.append([loc[0]-1,loc[1]])
            if loc[0]+1 <= row_num - 1 and seen[loc[0]+1][loc[1]] == 0:
                neighbors.append([loc[0]+1,loc[1]])
            if loc[1]-1 >= 0 and seen[loc[0]][loc[1]-1] == 0:
                neighbors.append([loc[0],loc[1]-1])
            if loc[1]+1 <= col_num - 1 and seen[loc[0]][loc[1]+1] == 0:
                neighbors.append([loc[0],loc[1]+1])
            seen[loc[0]][loc[1]] = 1
            return neighbors

        self.neighbors.append(find_neighbors(self.start))
        def pathsrecursive(loc, grid):
            pass


if __name__ == '__main__':
    def test(input):
        Test = Solution()
        ans = Test.uniquePathsIII(input)
        print(ans)


    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    test(grid)  # 2
    """
    grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    test(grid) #4
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    test(grid) #2
    grid = [[0,1],[2,0]]
    test(grid) #2
    """

    # print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))
