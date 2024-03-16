"""
357. Count Numbers with Unique Digits
Solved
Medium
Topics
Companies
Hint
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:

Input: n = 0
Output: 1

Constraints:

0 <= n <= 8

Hints:
Hint 1

To find unique patterns with r digits over n places we use permutation i.e nPr which is equal to r * (r-1) * ... n times. This is what our answer could have been but the digits we are using are not truly unique since for n = 4, i.e num <=9999 we can use 0 again and again, example: 0009, 0099 use 0 again and again but are valid. So here's the hint: Leading zeroes are the real deal, handle leading zeroes somehow, and then after that we can use zero only once

Hint 2:

How about first considering cases that have no leading zeroes, how many digits can be used in first place? How many can be used in second place and so on?

Hint 3:

If we have leading zeroes taken care of, the first place can use only 9 digits (excluding zero), the second place can use one lesser digit since one digit got used previously, but we have one extra digit too(since we can use zero now) so we can use 9 again. The third place can use only 8 digits since 2 digits got used. The 4rth place can use only 7. So the answer is turning out to be 9*9*8*7...

Hint 4:

For a number, add all answers for cases with no leading zeroes, one leading zeroes, ..and so on. For n = 4 answer would be sum of these

No leading zeroes i.e xxxx - 9 * 9 * 8 * 7
One leading zero i.e 0xxx - 9 * 9 * 8
Two leading zeroes i.e 00xx - 9 * 9
Three leading zeroes i.e 000x - 9
Four leading zeroes i.e 0000 - 1
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = [1]
        i = 1
        while n >= len(res):
            res.append(9*int(math.factorial(9)/math.factorial(8-(i-2))))
            i += 1
        return sum(res)