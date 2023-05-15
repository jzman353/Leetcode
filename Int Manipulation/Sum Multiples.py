"""
2652. Sum Multiples
Easy

Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

Example 1:

Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
Example 2:

Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.
Example 3:

Input: n = 9
Output: 30
Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.

Constraints:

1 <= n <= 103
"""

#26%
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s = 0
        for i in range(1,n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                s += i
        return s

"""
https://www.cuemath.com/algebra/arithmetic-progressions/
Algorithmic progressions
(amt//2) * (2 * v + (amt - 1) * v)
(v*amt//2) * (2+amt-1)
(v//2)*(amt+amt*amt)


Sample 11 ms submission

def calc(n, d):
    amt = n // d
    v = (amt + amt * amt) // 2
    return d * v

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        out = calc(n, 3) + calc(n, 5) + calc(n, 7)
        out -= calc(n, 15) + calc(n, 21) + calc(n, 35)
        out += calc(n, 105)
        return out
"""