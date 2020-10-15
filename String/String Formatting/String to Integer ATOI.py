"""
80%
8. String to Integer (atoi)
Medium

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

    Only the space character ' ' is considered a whitespace character.
    Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.



Example 1:

Input: str = "42"
Output: 42

Example 2:

Input: str = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: str = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: str = "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.



Constraints:

    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-' and '.'.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        try:
            import string
            for i in string.ascii_letters:
                if i in s: #would have to be while if index didn't return lowest index
                    s = s[0:s.index(i)]
            for i in """!"#$%&'()*,/:;<=>?@[\]^_`{|}~ """:
                if i in s: #would have to be while if index didn't return lowest index
                    s = s[0:s.index(i)]
            for i in '-+':
                if i in s[1:]:
                    s = s[0:s.index(i,1)]
            print(s)
            s = int(float(s))
            if s<-2147483648:
                s = -2147483648
            if s>2147483647:
                s = 2147483647
        except:
            s = 0
        return s

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.myAtoi(input1)
        print(ans)
        return ans

    assert test("42") == 42
    assert test("   -42") == -42
    assert test( "4193 with words") == 4193
    assert test("words and 987") == 0
    assert test("-91283472332") == -2147483648
    assert test("3.14159") == 3
    assert test("  -0012a42") == -12
    assert test("   +0 123") == 0
    assert test("+1") == 1
    assert test("-5-") == -5

"""
class Solution:
    def myAtoi(self, s: str) -> int:
        if type(s) != str:
            return 0
        s = s.strip()
        if len(s) < 1:  # string is empty or only contains whitespace
            return 0

        sign = 1
        if not s[0].isnumeric():  #not number
            if s[0] == '+':
                s = s[1:]
            elif s[0] == '-':
                sign = -1
                s = s[1:]
            else:
                return 0

        result = 0
        int_max = (1<<31) - 1
        int_min = (-1<<31)
        for i in range(len(s)):
            ch = s[i]
            if not ch.isnumeric():
                break
            ch_num = ord(ch) - ord('0')
            if sign == 1 and result+ch_num/10 >= int_max / 10:
                return int_max
            if sign == -1 and result+ch_num/10 >= -int_min / 10:
                return int_min

            result = result * 10 + ch_num
        return result * sign
"""