"""
67%
258. Add Digits
Easy

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
Accepted
325.7K
Submissions
561.8K
https://en.wikipedia.org/wiki/Digital_root
"""

class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + ((num-1) % 9) if num !=0 else 0

        """
        n = num
        while len(n)>=10:
            summ = 0
            for i in str(n):
                summ += int(i)
            if sum < 10:
                return summ
            else:
                n = summ
        """