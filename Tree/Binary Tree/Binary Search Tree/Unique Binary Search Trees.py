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

100%
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]
        for i in range(1, n+1):
            tmp = 0
            for j in range(1, i+1):
                tmp += dp[j-1] * dp[i-j]
            dp.append(tmp)
        return dp[n]


if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.numTrees(input1)
        print(ans)
        return ans


    # N=1: only one tree possible
    assert test(1) == 1, "Test 1 failed: n=1"

    # N=2: two trees possible (root=1 or root=2)
    assert test(2) == 2, "Test 2 failed: n=2"

    # N=3: example from problem
    assert test(3) == 5, "Test 3 failed: n=3"

    # N=4: verify against known value
    assert test(4) == 14, "Test 4 failed: n=4"

    # N=5: verify against known Catalan number
    assert test(5) == 42, "Test 5 failed: n=5"

    # N=6
    assert test(6) == 132, "Test 6 failed: n=6"

    # N=10: larger known Catalan number
    assert test(10) == 16796, "Test 7 failed: n=10"

    # N=19: maximum constraint
    assert test(19) == 1767263190, "Test 8 failed: n=19 max constraint"

    # Return type check
    assert isinstance(test(1), int), "Test 9 failed: should return int"

    # Idempotency
    assert test(5) == 42
    assert test(5) == 42, "Test 10 failed: idempotency"

    print("All tests passed!")