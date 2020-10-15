"""
#57%
65. Valid Number
Hard

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

    Numbers 0-9
    Exponent - "e"
    Positive/negative sign - "+"/"-"
    Decimal point - "."

Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        '''import collections
        c = collections.Counter(s)
        if c["e"] > 1 or c["."] > 1:
            return False
        if c["-"] > 1:
            i1 = s.index("-")
            i2 = s.index("-",i1+1)
            if s[i2-1] != "e":
                return False
        if c["+"] > 1:
            i1 = s.index("+")
            i2 = s.index("+", i1+1)
            if s[i2 - 1] != "e":
                return False
        if c["-"] > 0 and c["+"] > 0:
            i1 = s.index("+")
            i2 = s.index("-")
            if (i2 - 1 > 0 and s[i2 - 1] != "e") or (i1 - 1 > 0 and s[i1-1] != "e"):
                return False
        s = s.strip()
        for i in """abcdfghijklmnopqrstuvwxyz!"#$%&'()*,/:;<=>?@[\]^_`{|}~ """:
            if i in s:
                return False'''
        try:
            s = float(s)
            return True
        except:
            return False

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.isNumber(input1)
        print(ans)
        return ans

    assert test("0") == True
    assert test("0.1") == True
    assert test("abc") == False
    assert test("1 a") == False
    assert test("2e10") == True
    assert test(" -90e3   ") == True
    assert test(" 1e") == False
    assert test("e3") == False
    assert test(" 6e-1") == True
    assert test(" 99e2.5 ") == False
    assert test("53.5e93") == True
    assert test(" --6 ") == False
    assert test("-+3") == False
    assert test("95a54e53") == False
    assert test("-.7e+0435") == True
    assert test("+42e+76125") == True


"""
using isdigit()

class Solution:
    def isNumber(self, s: str) -> bool: 
        l, r = 0, len(s)
        # remove left/right empty space
        while l < r and s[l] == " ": l += 1
        while r > l and s[r-1] == " ": r -= 1
        
        seen = [0, 0, 0] # ".", "e", digit
        for i in range(l, r):
            if s[i].isdigit():
                seen[2] = 1
            
            elif s[i] == "+" or s[i] == "-":
                if not (i == l or s[i-1] == "e") or i == r - 1:
                    return False
            
            elif s[i] == ".":
                if seen[0] or seen[1]:
                    return False
                seen[0] = 1
            
            elif s[i] == "e":
                if seen[1] or not seen[2] or i == r - 1:
                    return False
                seen[1] = 1
            
            else: # invalid characters
                return False
        if not seen[2]: return False
        else: return True
"""