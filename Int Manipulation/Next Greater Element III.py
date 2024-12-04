"""
556. Next Greater Element III
Solved
Medium
Topics
Companies
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1

Constraints:

1 <= n <= 231 - 1
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        if len(s) == 1:
            return -1
        alt = None
        if s[-1] > s[-2] and int(s[:-2]+s[-1]+s[-2]) <= 2147483647:
            return int(s[:-2]+s[-1]+s[-2])
        for i in range(len(s)-2,-1,-1):
            if s[i] < s[i+1]:
                for j in range(len(s)-1,i,-1):
                    if s[j] > s[i]:
                        alt = int(s[:i]+s[j]+"".join(sorted(s[i:j]+s[j+1:])))
                        if alt and alt > n and alt <= 2147483647:
                            return alt
                        else:
                            return -1
        return -1

"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 1

        while i - 1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
        if i == 0:
            return -1
        j = i
        while j + 1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        res = int(''.join(digits))
"""