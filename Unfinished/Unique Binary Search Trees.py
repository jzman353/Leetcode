"""
96. Unique Binary Search Trees
Medium

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:

Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

Constraints:

1 <= n <= 19
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 2]
        for i in range(3, n+1):
            pass
        return dp[n-1]


if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.numTrees(input1)
        print(ans)
        return ans

    assert test(3) == 5
    assert test(1) == 1