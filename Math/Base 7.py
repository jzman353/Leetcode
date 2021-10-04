"""
504. Base 7
Easy

Given an integer num, return a string of its base 7 representation.

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"

Constraints:

-107 <= num <= 107
"""
#22%
class Solution:
    def convertToBase7(self, num: int) -> str:
        #powers = [5764801,823543,117649,16807,2401,343,49,7]
        if num == 0:
            return "0"
        if num < 0:
            ans = "-"
        else:
            ans = ""
        num = abs(num)
        start = False
        for i in range(8,-1,-1):
            count = 0
            while num >= 7**i:
                start = True
                num -= 7**i
                count += 1
            if start:
                ans = ans + str(count)
        return ans

"""
sample 12 ms submission
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        negative = False if num >= 0 else True
        num = abs(num)
        base7 = ""
        while num != 0:
            base7 = str(num%7) + base7
            num = num // 7
        return base7 if not negative else "-" + base7
"""