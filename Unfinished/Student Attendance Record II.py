"""
552. Student Attendance Record II
Hard

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.



Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316


Constraints:

1 <= n <= 105
"""

#NOT WORKING (LOGIC ERROR)
import math
class Solution:
    def checkRecord(self, n: int) -> int:
        # 1 -> 3
        # 2 -> 8
        # P L
        # PP LP PL LL
        # PPP PPL PLP PLL LPL LLP
        # PPPP PPPL PPLP PPLL PLPP ...
        if n == 1:
            return 3

        self.total = 0
        a_count = 0
        l_count = 0
        i = 0

        def recursive(l, i, a_count, l_count):
            if i < n:
                if len(l) == n:
                    print(l)
                    self.total += 1
                if l[-1] == 'P':
                    l_count = 0
                    i += 1
                    temp = l + 'L'
                    recursive(temp, i, a_count, l_count)
                    temp = l + 'P'
                    recursive(temp, i, a_count, l_count)
                elif l[-1] == 'L':
                    l_count += 1
                    i += 1
                    if l_count < 2:
                        temp = l + 'L'
                        recursive(temp, i, a_count, l_count)
                    temp = l + 'P'
                    recursive(temp, i, a_count, l_count)

        for start in ['L', 'P']:
            recursive(start, i, a_count, l_count)
        return (self.total*(n)) % (10 ** 9 + 7)


def test(input1):
    Test = Solution()
    print(input1)
    res = Test.checkRecord(input1)
    print(res)
    return res

assert test(1) == 3
assert test(2) == 8
assert test(3) == 19
assert test(4) == 43
assert test(10101) == 183236316
"""
#TLE
class Solution:
    def checkRecord(self, n: int) -> int:
        # 1 -> 3
        # 2 -> 8
        # P L
        # PP LP PL LL
        # PPP PPL PLP PLL LPL LLP
        # PPPP PPPL PPLP PPLL PLPP ...
        self.total = 0
        a_count = 0
        l_count = 0
        i = 0

        def recursive(l, i, a_count, l_count):
            if i < n:
                if len(l) == n:
                    # print(l)
                    self.total += 1
                if l[-1] == 'P':
                    l_count = 0
                    i += 1
                    if a_count < 1:
                        temp = l + 'A'
                        recursive(temp, i, a_count, l_count)
                    temp = l + 'L'
                    recursive(temp, i, a_count, l_count)
                    temp = l + 'P'
                    recursive(temp, i, a_count, l_count)
                elif l[-1] == 'L':
                    l_count += 1
                    i += 1
                    if a_count < 1:
                        temp = l + 'A'
                        recursive(temp, i, a_count, l_count)
                    if l_count < 2:
                        temp = l + 'L'
                        recursive(temp, i, a_count, l_count)
                    temp = l + 'P'
                    recursive(temp, i, a_count, l_count)
                elif l[-1] == 'A':
                    l_count = 0
                    a_count += 1
                    temp = l + 'L'
                    recursive(temp, i, a_count, l_count)
                    temp = l + 'P'
                    recursive(temp, i, a_count, l_count)

        for start in ['L', 'A', 'P']:
            recursive(start, i, a_count, l_count)
        return self.total % (10 ** 9 + 7)
"""