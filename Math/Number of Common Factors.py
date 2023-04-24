"""
2427. Number of Common Factors
Easy

Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.

Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.

Constraints:

1 <= a, b <= 1000
"""

#65%
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        gcd = math.gcd(a, b)
        ans = 1
        for i in range(2, gcd+1):
            if a%i == 0 and b%i == 0:
                ans += 1
        return ans
"""
Sample 15 ms submission
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res, hcf = 0, math.gcd(a, b)
        for i in range(1, int(hcf ** 0.5) + 1):
            if hcf % i == 0: res += 1 + (hcf // i != i)
        return res

# 35%
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        minn = min(a,b)
        ans = 1
        for i in range(2, minn+1):
            if a%i == 0 and b%i == 0:
                ans += 1
        return ans
"""
import random
def test_cases():
    a, b = random.randint(1,1000), random.randint(1,1000)
    print(a)
    print(b)

for i in range(8):
    test_cases()