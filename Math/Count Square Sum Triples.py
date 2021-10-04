"""
1925. Count Square Sum Triples
Easy

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).
Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

Constraints:

1 <= n <= 250
"""

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(n-1):
            for j in range(i+1,n):
                    calc = sqrt(i**2 + j**2)
                    if calc.is_integer() and j+1<=calc<=n:
                        ans += 2
        return ans

"""
math.isqrt - Return the integer square root of the nonnegative integer n. This is the floor of the exact square root of n, or equivalently the greatest integer a such that a² ≤ n.
sample 20 ms submission
class Solution:
    def countTriples(self, n: int) -> int:
        return 2*sum(n//(x*x + y*y) for x in range(2, isqrt(n) + 1) for y in range(1, x) if (x&y&1) == 0 and gcd(x,y) == 1)

sample 204 ms submission
class Solution:
    def countTriples(self, n: int) -> int:
        squares = [i*i for i in range(1, n+1)]
        squares = set(squares)
        ans = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i*i + j*j in squares:
                    ans += 1
        return ans
"""