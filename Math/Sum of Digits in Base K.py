"""
1837. Sum of Digits in Base K
Easy

Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.

Example 1:

Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
Example 2:

Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1.

Constraints:

1 <= n <= 100
2 <= k <= 10
"""

#84%
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        answer = 0
        while n>0:
            answer += n%k
            n=n//k
        return answer

"""
#divmod combines divide and modulus into one line of code
sample 16 ms submission
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sum = 0
        while n > 0:
            n, remainder = divmod(n, k)
            sum += remainder
        return sum
"""