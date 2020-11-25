"""
#25%
1544. Make The String Great
Easy

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.



Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:

Input: s = "s"
Output: "s"



Constraints:

    1 <= s.length <= 100
"""
import string
class Solution:
    def makeGood(self, s: str) -> str:
        for i in range(len(s)-1):
            if s[i].lower() == s[i+1].lower() and ((s[i] in string.ascii_lowercase and s[i+1] in string.ascii_uppercase) or (s[i] in string.ascii_uppercase and s[i+1] in string.ascii_lowercase)):
                s = self.makeGood(s[:i]+s[i+2:])
                break
        return s

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.makeGood(input1)
        print(ans)
        return ans

    assert test("leEeetcode") == "leetcode"
    assert test("abBAcC") == ""


    class Solution:
        def makeGood(self, s: str) -> str:
            stack = []
            for char in s:
                # upper char
                if stack and stack[-1].isupper() and stack[-1].lower() == char:
                    stack.pop()
                # lower char
                elif stack and stack[-1].islower() and stack[-1].upper() == char:
                    stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)