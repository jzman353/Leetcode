"""
13. Roman to Integer
Easy

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

Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3

Example 2:

Input: s = "IV"
Output: 4

Example 3:

Input: s = "IX"
Output: 9

Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Accepted
781,524
Submissions
1,393,608
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        #d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        length = len(s)
        for i in range(length):
            if s[i] == "I" and i+1 < length and s[i+1] != "V" and s[i+1] != "X":
                ans += 1
            elif s[i] == "I" and i+1 < length and (s[i+1] == "V" or s[i+1] == "X"):
                ans -= 1
            elif s[i] == "I" and i+1 == length:
                ans += 1
            elif s[i] == "V":
                ans += 5
            elif s[i] == "X" and i+1 < length and s[i+1] != "L" and s[i+1] != "C":
                ans += 10
            elif s[i] == "X" and i+1 < length and (s[i+1] == "L" or s[i+1] == "C"):
                ans -= 10
            elif s[i] == "X" and i+1 == length:
                ans += 10
            elif s[i] == "L":
                ans += 50
            elif s[i] == "C" and i + 1 < length and s[i + 1] != "D" and s[i + 1] != "M":
                ans += 100
            elif s[i] == "C" and i + 1 < length and (s[i + 1] == "D" or s[i + 1] == "M"):
                ans -= 100
            elif s[i] == "C" and i+1 == length:
                ans += 100
            elif s[i] == "D":
                ans += 500
            elif s[i] == "M":
                ans += 1000
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.romanToInt(input1)
        print(ans)
        return ans

    input1 = "III"
    assert test(input1) == 3
    input1 = "IV"
    assert test(input1) == 4
    input1 = "IX"
    assert test(input1) == 9
    input1 = "LVIII"
    assert test(input1) == 58
    input1 = "C"
    assert test(input1) == 100
    input1 = "D"
    assert test(input1) == 500
    input1 = "M"
    assert test(input1) == 1000
    input1 = "MMMMDCIX"
    assert test(input1) == 4609
    input1 = "MMMMIXCD"
    assert test(input1) == 4389

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dct ={'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        comp_dct ={'I':['V','X'],
                  'X':['L','C'],
                  'C':['D','M']}
        total=0
        prevch=''
        for ch in s[::-1]:
            if ch in comp_dct:
                
                if prevch in comp_dct[ch]:
                    #priint(dct[ch])
                    total -=dct[ch]
                    #print(total)
                else:
                    total +=dct[ch]
                    #print(total)
            else:
                total +=dct[ch]
            prevch =ch
        return total
"""