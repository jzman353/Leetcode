"""
766. Toeplitz Matrix
Easy

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""
#41%
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j not in d.keys():
                    d[i-j] = matrix[i][j]
                else:
                    if matrix[i][j] != d[i-j]:
                        return False
        return True
"""
sample 68 ms submission
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for i in range(row_len-1):
            
            if matrix[i][0:col_len-1] != matrix[i+1][1:]:
                return False
        
        return True

Approach #1: Group by Category [Accepted]
Intuition and Algorithm

We ask what feature makes two coordinates (r1, c1) and (r2, c2) belong to the same diagonal?

It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.

This leads to the following idea: remember the value of that diagonal as groups[r-c]. If we see a mismatch, the matrix is not Toeplitz; otherwise it is.

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
    
Complexity Analysis

Time Complexity: O(M*N)O(M∗N). (Recall in the problem statement that M, NM,N are the number of rows and columns in matrix.)

Space Complexity: O(M+N)O(M+N).

Approach #2: Compare With Top-Left Neighbor [Accepted]
Intuition and Algorithm

For each diagonal with elements in order a_1, a_2, a_3, \dots, a_ka 
 . The matrix is Toeplitz if and only if all of these conditions are true for all (top-left to bottom-right) diagonals.

Every element belongs to some diagonal, and it's previous element (if it exists) is it's top-left neighbor. Thus, for the square (r, c), we only need to check r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c].

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))

Complexity Analysis

Time Complexity: O(M*N)O(M∗N), as defined in the problem statement.

Space Complexity: O(1)O(1).
"""
