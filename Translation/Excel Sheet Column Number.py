"""
171. Excel Sheet Column Number
Easy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701

Constraints:

    1 <= s.length <= 7
    s consists only of uppercase English letters.
    s is between "A" and "FXSHRXW".
"""

#86%
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        count = 0
        for i in range(len(s) - 1, -1, -1):
            ans += (ord(s[i]) - 65 + 1) * 26 ** count
            count += 1
        return ans
