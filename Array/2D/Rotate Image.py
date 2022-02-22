"""
48. Rotate Image
Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix [::] = list(zip(*matrix[::-1]))

"""
Approach 1: Rotate Groups of Four Cells
Intuition

Observe how the cells move in groups when we rotate the image.

The corners all move

We can iterate over each group of four cells and rotate them.

Implementation

Here is a visualization of the algorithm in action.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
                
Complexity Analysis

Let MM be the number of cells in the matrix.

Time complexity : \mathcal{O}(M)O(M), as each cell is getting read once and written once.

Space complexity : \mathcal{O}(1)O(1) because we do not use any other additional data structures.


Approach 2: Reverse on Diagonal and then Reverse Left to Right
Intuition

The most elegant solution for rotating the matrix is to firstly reverse the matrix around the main diagonal, and then reverse it from left to right. These operations are called transpose and reflect in linear algebra.

Here is a visualization to help you see why this works.


Bonus Question: What would happen if you reflect and then transpose? Would you still get the correct answer?

Even though this approach does twice as many reads and writes as approach 1, most people would consider it a better approach because the code is simpler, and it is built with standard matrix operations that can be found in any matrix library.

Implementation

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


Complexity Analysis

Let MM be the number of cells in the grid.

Time complexity : \mathcal{O}(M)O(M). We perform two steps; transposing the matrix, and then reversing each row. Transposing the matrix has a cost of \mathcal{O}(M)O(M) because we're moving the value of each cell once. Reversing each row also has a cost of \mathcal{O}(M)O(M), because again we're moving the value of each cell once.

Space complexity : \mathcal{O}(1)O(1) because we do not use any other additional data structures.
"""