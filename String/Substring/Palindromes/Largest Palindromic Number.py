"""
2384. Largest Palindromic Number
Medium

You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:

You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.

Example 1:

Input: num = "444947137"
Output: "7449447"
Explanation:
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.
Example 2:

Input: num = "00009"
Output: "9"
Explanation:
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.

Constraints:

1 <= num.length <= 105
num consists of digits.
"""

#63%
import string
from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        ans = ""
        middle = False

        for i in sorted(c.keys(), reverse = True):
            if c[i] % 2 == 1 and not middle:
                middle = i
            if c[i] >= 2:
                ans = ans + i*(c[i]//2)
        if ans and ans[0] == '0' and not middle:
            return '0'
        elif ans and ans[0] == '0' and middle:
            return middle
        else:
            reverse = ans[::-1]
            if middle:
                return ans + middle + reverse
            else:
                return ans + reverse

import random
def testCases():
    print('"'+"".join(random.choices(string.digits, k=random.randint(1,10**5)))+'"')

for i in range(8):
    testCases()

"""
Sample 45 ms submission

class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = collections.Counter(num)
        ans = ''
        digit = False
        for num in range(9, -1, -1):
            if not num and not ans:
                if digit:
                    return digit
                else:
                    return '0'
            ans += cnt[str(num)] // 2 * str(num)
            if not digit and cnt[str(num)] % 2:
                digit = str(num)
        if digit:
            return ans + digit + ans[::-1]
        else:
            return ans + ans[::-1]
"""