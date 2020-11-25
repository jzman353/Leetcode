"""
1582. Special Positions in a Binary Matrix
Easy

Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:

Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:

Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions.

Example 3:

Input: mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]
Output: 2

Example 4:

Input: mat = [[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
Output: 3

Constraints:

    rows == mat.length
    cols == mat[i].length
    1 <= rows, cols <= 100
    mat[i][j] is 0 or 1.
"""

#48%
import collections
class Solution:
    def numSpecial(self, mat) -> int:
        rows = []
        cols = []
        rowsc = collections.Counter()
        colsc = collections.Counter()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
                    rowsc[i] += 1
                    colsc[j] += 1

        ans = 0
        for i in range(len(rows)):
            if rowsc[rows[i]]==1 and colsc[cols[i]]==1:
                ans += 1

        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.numSpecial(input1)
        print(ans)
        return ans
    mat = [[1,0,0],[0,0,1],[1,0,0]]
    assert test(mat) == 1
    mat = [[1,0,0],[0,1,0],[0,0,1]]
    assert test(mat) == 3
    mat = [[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]
    assert test(mat) == 2
    mat = [[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
    assert test(mat) == 3
    mat = [[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]
    assert test(mat) == 1

"""
sample 140 ms submission

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cols = list(zip(*mat))
        count = 0
        for row in mat:
            if sum(row) == 1 and sum(cols[row.index(1)]) == 1:
                count += 1
        return count
"""