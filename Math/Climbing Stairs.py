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
#76%
import collections
class Solution:
    def climbStairs(self, n: int) -> int:
        #stairs = [1,2,2+1,2+2+1]
        if n == 1:
            return 1
        stairs = collections.deque([1,2])
        for i in range(2,n):
            stairs.append(stairs[-1]+stairs[-2])
            stairs.popleft()
        return stairs[-1]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        #stairs = [1,2,2+1,2+2+1]
        if n == 1:
            return 1
        stairs = [1,2]
        for i in range(2,n):
            stairs.append(stairs[-1]+stairs[-2])
        return stairs[-1]
"""