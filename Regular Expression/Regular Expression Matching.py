"""
NOT COMPLETE

10. Regular Expression Matching
Hard

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false



Constraints:

    0 <= s.length <= 20
    0 <= p.length <= 30
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
"""
"""
#Attempt #1 - Doesn't work
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        index = 0
        for i in range(len(p)):
            if i != "." and i != "*":
                if s[index] != p[i]:
                    if i+1<len(p) and p[i+1] != '*':
                        return False
                    else:
                        temp = s[index]
                        while s[index] == temp:
                            index += 1
                else:
                    prev = s[index]
                    index += 1
            elif i == '.':
                prev = s[index]
                index += 1
                #prev = -1 #This statement could be used if .* could result in any number of variety of chars instead of just one repeated char
            elif i == "*":
                pass
            return True
"""
#35%
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        Regex = re.compile(p)
        mo1 = Regex.search(s)
        #print(mo1)
        #print(mo1.group())
        return mo1 and mo1.group() == s


if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.isMatch(input1,input2)
        print(ans)
        return ans

    assert test("aa", "a") == False
    assert test("aa", "a*") == True
    assert test("ab", ".*") == True
    assert test("aab", "c*a*b") == True
    assert test("mississippi", "mis*is*p*") == False
    assert test("ab", ".*c") == False




