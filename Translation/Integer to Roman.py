"""
12. Integer to Roman
Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1:

Input: num = 3
Output: "III"

Example 2:

Input: num = 4
Output: "IV"

Example 3:

Input: num = 9
Output: "IX"

Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

    1 <= num <= 3999
"""
#68%
class Solution:
    def intToRoman(self, num: int) -> str:
        rules = (
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        )

        ans = ""
        for suffix, value in rules:
            while num >= value:
                num -= value
                ans += suffix

        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.intToRoman(input1)
        print(ans)
        return ans

    assert test(3) == "III"
    assert test(4) == "IV"
    assert test(9) == "IX"
    assert test(19) == "XIX"
    assert test(30) == "XXX"
    assert test(58) == "LVIII"
    assert test(1994) == "MCMXCIV"

"""
100%
class Solution:
    def intToRoman(self, num: int) -> str:
        ans =''
        while num>0:
            if num>=1000:
                ans += "M"
                num -= 1000
            elif num>=900:
                ans += "CM"
                num -= 900
            elif num>=500:
                ans += "D"
                num -= 500
            elif num>=400:
                ans += "CD"
                num -= 400
            elif num>=100:
                ans += "C"
                num -= 100
            elif num>=90:
                ans += "XC"
                num -= 90
            elif num>=50:
                ans += "L"
                num -= 50
            elif num>=40:
                ans += "XL"
                num -= 40
            elif num>=10:
                ans += "X"
                num -= 10
            elif num>=9:
                ans += "IX"
                num -= 9
            elif num>=5:
                ans += "V"
                num -= 5
            elif num>=4:
                ans += "IV"
                num -= 4
            elif num>=1:
                ans += "I"
                num -= 1
        return ans
"""