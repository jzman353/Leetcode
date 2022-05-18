"""
240. Search a 2D Matrix II
Medium

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
"""

#5%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.stack = []
        self.answer = False
        seen = []

        def helper(pos):
            for i in [[pos[0] + 1, pos[1]], [pos[0], pos[1] + 1]]:
                if i[0] < self.m and i[1] < self.n and matrix[i[0]][i[1]] <= target and i not in seen:
                    if matrix[i[0]][i[1]] == target:
                        self.answer = True
                        return
                    seen.append(i)
                    heappush(self.stack, (-abs(matrix[i[0]][i[1]] - target), i))
                    # print(self.stack)

        start = [0, 0]
        for i in range(min(self.m, self.n)):
            if matrix[i][i] <= target:
                start = [i, i]
        if start[0] + 1 < self.n and start != [0, 0]:
            startn = [0, start[0] + 1]
        else:
            startn = None
        if start[0] + 1 < self.m and start != [0, 0]:
            startm = [start[0] + 1, 0]
        else:
            startm = None

        for i in [start, startn, startm]:
            if i:
                if matrix[i[0]][i[1]] == target:
                    return True
                heappush(self.stack, (-abs(matrix[i[0]][i[1]] - target), i))

        while self.stack:
            if self.answer:
                return True
            helper(self.stack.pop()[1])
        return self.answer

"""
sample 144 ms submission
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False
"""