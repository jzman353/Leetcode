"""
67%
168. Excel Sheet Column Title
Easy

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"
"""

import math
class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""
        while n > 0:
            r, n = (n-1) % 26, (n-1)//26
            ans = str(chr(65+r) + ans)
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.convertToTitle(input1)
        print(ans)
        return ans

    assert test(1) == "A"
    assert test(28) == "AB"
    assert test(650) == "XZ"
    assert test(701) == "ZY"
    assert test(703) == "AAA"