"""
62. Unique Paths
Medium

8819

298

Add to List

Share
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100

100%
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        self.squares = [[0 for i in range(n)] for j in range(m)]
        self.squares[0][0] = 2

        def helper(row, col):
            if row == m - 1 and col == n - 1:
                self.squares[row][col] = self.squares[row - 1][col] + self.squares[row][col - 1]
            elif row == m - 1:
                self.squares[row][col] = self.squares[row][col - 1] + self.squares[row - 1][col] // 2
            elif col == n - 1:
                self.squares[row][col] = self.squares[row][col - 1] // 2 + self.squares[row - 1][col]
            else:
                self.squares[row][col] = self.squares[row][col - 1] + self.squares[row - 1][col]

        for d in range(1, m + n - 1):
            if d % 2 == 0:  # Even diagonal: up-right
                row = min(d, m - 1)
                col = d - row
                while row >= 0 and col < n:
                    #print(row, col)
                    helper(row, col)
                    row -= 1
                    col += 1
            else:  # Odd diagonal: down-left
                col = min(d, n - 1)
                row = d - col
                while col >= 0 and row < m:
                    #print(row, col)
                    helper(row, col)
                    col -= 1
                    row += 1

        #print(self.squares)
        return self.squares[m-1][n-1]


"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        for i in range(n):
            self.squares[0][i] = 2
        for i in range(m):
            self.squares[i][0] = 2
        self.squares[0][n-1] = 1
        self.squares[m-1][0] = 1

        def helper(pos):
            if pos[0] == m-1 and pos[1] == n-1:
                return self.squares[pos[0]-1][pos[1]]+self.squares[pos[0]][pos[1]-1]
            elif pos[0] == m-1:
                self.squares[pos[0]][pos[1]] = self.squares[pos[0]][pos[1]-1]+self.squares[pos[0]-1][pos[1]]/2
            elif pos[1] == n-1:
                self.squares[pos[0]][pos[1]] = self.squares[pos[0]][pos[1]-1]/2+self.squares[pos[0]-1][pos[1]]
            else:
                self.squares[pos[0]][pos[1]] = self.squares[pos[0]][pos[1]-1]+self.squares[pos[0]-1][pos[1]]

            pos[0] -= 1
            pos[1] += 1
            helper(pos[0])

        helper([1,1])
        return self.squares[-1][-1]"""

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]

        #Base case
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):
                goRight = dp[i][j+1]
                goBottom = dp[i+1][j]

                dp[i][j] += goRight + goBottom

        return dp[0][0]
"""

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.uniquePaths(input1,input2)
        print(ans)
        return ans


    assert test(3, 7) == 28
    assert test(3, 2) == 3
    assert test(1, 2) == 1
    assert test(10, 10) == 48620

"""
#TLE
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.squares = [[0 for i in range(n)] for j in range(m)]
        def helper(pos):
            for i in [[pos[0]+1,pos[1]],[pos[0],pos[1]+1]]:
                if i[0] < m and i[1] < n:
                    self.squares[i[0]][i[1]] += 1
                    helper([i[0],i[1]])
        helper([0,0])
        return self.squares[-1][-1]
"""