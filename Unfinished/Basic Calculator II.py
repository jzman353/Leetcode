"""
Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
"""
#Improvements:
"""
Instead of using the two while loops that check if it has operators over and over again,
simply sweep through the expression one time and set the ind to be the current index if the current index is what we are looking for
"""

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        while "*" in s or "/" in s:
            if '*' in s and '/' in s:
                m = s.index('*')
                d = s.index('/')
                ind = min(m,d)
                if ind == m:
                    sign = "m"
                else:
                    sign = "d"
            elif '*' in s:
                sign = "m"
                ind = s.index('*')
            else:
                sign = "d"
                ind = s.index('/')
            before = ''
            i = ind-1
            while i >= 0 and s[i].isdigit():
                before = s[i]+before
                i -= 1
            if i==-1 or i >= 0 and s[i] != "-":
                begin = i+1
            elif s[i] == "-":
                before = '-' + before
                begin = i
            i = ind+1
            if s[i] == '-':
                after = '-'
                i+=1
            else:
                after = ''
            while i < len(s) and s[i].isdigit():
                after = after + s[i]
                i += 1
            end = i
            if before == '':
                before = 0
            if sign == "m":
                new = str(int(before)*int(after))
            else:
                temp = int(before)//int(after)
                if temp >= 0:
                    new = str(temp)
                else:
                    new = str(-(abs(int(before))//abs(int(after))))
            if new == '0':
                new = ''
            if new == '' and s[begin-1] == '+':
                begin -= 1
            s = s[:begin]+new+s[end:]
        if s and s[0] == '+':
            s = s[1:]
        while "+" in s or "-" in s:
            if '+' in s and '-' in s:
                a = s.index('+')
                ss = s.index('-')
                if ss != 0:
                    ind = min(a,ss)
                else:
                    ind = a
                if ind == a:
                    sign = "a"
                else:
                    sign = "s"
            elif '+' in s:
                sign = "a"
                ind = s.index('+')
            else:
                sign = "s"
                ind = s.index('-')
                if s.count('-') == 1 and ind == 0:
                    return s
                elif s.count('-') > 1 and ind == 0:
                    ind = s.index('-',1)
            before = ''
            i = ind-1
            while type(s) is str and i >= 0 and s[i].isdigit():
                before = s[i]+before
                i -= 1
            if i==-1 or i >= 0 and s[i] != "-":
                begin = i + 1
            elif s[i] == "-":
                before = '-'+before
                begin = i
            i = ind+1
            if s[i] == '-':
                after = '-'
                i += 1
            else:
                after = ''
            while type(s) is str and i < len(s) and s[i].isdigit():
                after = after + s[i]
                i += 1
            end = i
            if sign == "a":
                new = str(int(before)+int(after))
            else:
                new = str(int(before)-int(after))
            if new == '0' and begin == 0:
                new = ''
            if new == '' and s[begin-1] == '+':
                begin -= 1
            if new == '' and end+1<len(s) and s[end] == '+':
                end += 1
            s = s[:begin]+new+s[end:]
        return s if s else '0'

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.calculate(input1)
        print(ans)
        return ans

    assert test("3+2*2") == '7'
    assert test(" 3/2 ") == '1'
    assert test("3+5 / 2") == '5'
    assert test(" 3/2 +5 /4 - 0") == '2'
    assert test("0-2147483647") == '-2147483647'
    assert test("2-3+4") == '3'
    assert test("-2*3+4") == '-2'
    assert test("2*-3+4") == '-2'
    assert test("2-3-4") == '-5'
    assert test("14-3/2") == '13'
    assert test("1*2-3/4+5*6-7*8+9/10") == '-24'
    assert test("0+0") == '0'
    assert test("1-1+1") == '1'
    assert test("1/3/3/3/3/3/3/3/3/3") == '0'
    assert test("111/999+111+999") == '1110'

"""
Attempt at improving the code
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        ii = 0
        while ii < len(s):
            if ii >= len(s):
                break
            if s[ii] == '*':
                sign = "m"
                ind = ii
            elif s[ii] == '/':
                sign = "d"
                ind = ii
            else:
                ii += 1
                continue
            before = ''
            i = ind-1
            while i >= 0 and s[i].isdigit():
                before = s[i]+before
                i -= 1
            if i==-1 or i >= 0 and s[i] != "-":
                begin = i+1
            elif s[i] == "-":
                before = '-' + before
                begin = i
            i = ind+1
            if s[i] == '-':
                after = '-'
                i+=1
            else:
                after = ''
            while i < len(s) and s[i].isdigit():
                after = after + s[i]
                i += 1
            end = i
            if before == '':
                before = 0
            if sign == "m":
                new = str(int(before)*int(after))
            else:
                temp = int(before)//int(after)
                if temp >= 0:
                    new = str(temp)
                else:
                    new = str(-(abs(int(before))//abs(int(after))))
            if new == '0':
                new = ''
            if new == '' and s[begin-1] == '+':
                begin -= 1
            s = s[:begin]+new+s[end:]
        if s and s[0] == '+':
            s = s[1:]
        ii = 0
        while ii < len(s):
            if ii >= len(s):
                break
            if s[ii] == '+':
                sign = "a"
                ind = ii
            elif s[ii] == '-' and ii != 0:
                sign = "s"
                ind = ii
            else:
                ii += 1
                continue
            before = ''
            i = ind-1
            while type(s) is str and i >= 0 and s[i].isdigit():
                before = s[i]+before
                i -= 1
            if i==-1 or i >= 0 and s[i] != "-":
                begin = i + 1
            elif s[i] == "-":
                before = '-'+before
                begin = i
            i = ind+1
            if s[i] == '-':
                after = '-'
                i += 1
            else:
                after = ''
            while type(s) is str and i < len(s) and s[i].isdigit():
                after = after + s[i]
                i += 1
            end = i
            if sign == "a":
                new = str(int(before)+int(after))
            else:
                new = str(int(before)-int(after))
            if new == '0' and begin == 0:
                new = ''
            if new == '' and s[begin-1] == '+':
                begin -= 1
            if new == '' and end+1<len(s) and s[end] == '+':
                end += 1
            s = s[:begin]+new+s[end:]
        return s if s else '0'
"""