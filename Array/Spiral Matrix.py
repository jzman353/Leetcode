"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix):
        length = len(matrix)
        ans = []
        row = 0
        col = 1
        while length > 0:
            for i in range(length):
                ans.append(matrix[row][i])
            length -= 1
            for i in range(length):
                ans.append(matrix[i][-col])

        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.spiralOrder(input1)
        print(ans)
        return ans

    assert test([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert test([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]