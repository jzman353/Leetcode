"""
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
    1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        self.ans = 1
        def recursive(n):
            if n == 1:
                return
            elif n == 2:
                self.ans += 1
                return
            else:
                self.ans += 1
                recursive(n-1)
                recursive(n-2)
        recursive(n)
        return self.ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.climbStairs(input1)
        print(ans)
        return ans

    assert test(1) == 1
    assert test(2) == 2
    assert test(3) == 3
    assert test(4) == 5
    assert test(10) == 89