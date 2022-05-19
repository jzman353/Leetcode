"""
861. Score After Flipping Matrix
Medium

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Example 1:

Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
"""

#5%
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        # print(grid)
        grid1 = list(zip(*grid[::-1]))
        # print(grid1)
        for i in range(1, len(grid1)):
            if sum(grid1[i]) < (len(grid1[i])) / 2:
                for j in range(len(grid1[i])):
                    # print(i,grid1[i],j,grid[j][i])
                    if grid[j][i] == 0:
                        grid[j][i] = 1
                    else:
                        grid[j][i] = 0
        # print(grid)
        answer = 0
        for i in grid:
            number = 0
            for j in range(len(i)):
                number += i[len(i) - 1 - j] * (2 ** j)
            answer += number
        return answer

"""
Explantion
Assume A is M * N.

A[i][0] is worth 1 << (N - 1) points, more than the sum of (A[i][1] + .. + A[i][N-1]).
We need to toggle all A[i][0] to 1, here I toggle all lines for A[i][0] = 0.
A[i][j] is worth 1 << (N - 1 - j)
For every col, I count the current number of 1s.
After step 1, A[i][j] becomes 1 if A[i][j] == A[i][0].
if M - cur > cur, we can toggle this column to get more 1s.
max(cur, M - cur) will be the maximum number of 1s that we can get.

Complexity:
Time O(MN)
Space O(1)

def matrixScore(self, A):
    M, N = len(A), len(A[0])
    res = (1 << N - 1) * M
    for j in range(1, N):
        cur = sum(A[i][j] == A[i][0] for i in range(M))
        res += max(cur, M - cur) * (1 << N - 1 - j)
    return res
"""