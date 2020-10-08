"""
#84%
1572. Matrix Diagonal Sum
Easy

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.



Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:

Input: mat = [[5]]
Output: 5



Constraints:

    n == mat.length == mat[i].length
    1 <= n <= 100
    1 <= mat[i][j] <= 100

Accepted
18,572
Submissions
23,453
"""

class Solution:
    def diagonalSum(self, mat) -> int:
        length = len(mat)
        summ = 0
        if length % 2 != 0:
            mid = length // 2
            summ -= mat[mid][mid]
        for i in range(length):
            summ += mat[i][i]
            summ += mat[i][length-1-i]
        return summ

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.diagonalSum(input1)
        print(ans)


    input1 = [[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]
    test(input1)  # 55