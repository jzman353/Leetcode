"""
2133. Check if Every Row and Column Contains All Numbers
Easy

An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

Example 1:

Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
Example 2:

Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n
"""
#23%
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in matrix:
            for j in range(1,n+1):
                if j not in i:
                    return False
        cols = list(zip(*matrix[::-1]))
        for i in cols:
            for j in range(1,n+1):
                if j not in i:
                    return False
        return True

'''
sample 712 ms submission
class Solution:

    """    
    Create a set containing the integers from 1...n then check that each set of rows and columns is equal to this set.
    zip(*matrix) is a convenient way of obtaining the columns of a matrix
    """

    def checkValid(self, matrix: List[List[int]]) -> bool:
        set_ = set(range(1,len(matrix)+1))
        return all(set_ == set(x) for x in matrix+list(zip(*matrix)))
'''