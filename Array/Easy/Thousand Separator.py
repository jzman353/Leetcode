"""
1556. Thousand Separator
Easy

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Example 1:

Input: n = 987
Output: "987"

Example 2:

Input: n = 1234
Output: "1.234"

Example 3:

Input: n = 123456789
Output: "123.456.789"

Example 4:

Input: n = 0
Output: "0"

Constraints:
    0 <= n < 2^31
"""

#7%
class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ""
        count = 0
        n = str(n)
        for i in range(len(n)-1,0,-1):
            ans = n[i]+ans
            count += 1
            if count == 3:
                ans = "."+ans
                count = 0
        ans = n[0]+ans
        return ans

"""
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1]
        return '.'.join([n[i:i + 3] for i in range(0, len(n), 3)])[::-1]
"""