"""
Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"



Constraints:

    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""

import string
class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        stack = []
        temp = ""
        tempn = ""
        for i in range(len(s)):
            if not stack and s[i] in string.ascii_lowercase:
                ans = ans + s[i]
            elif s[i] in string.digits:
                if s[i+1] in string.digits:
                    tempn = tempn + s[i]
                elif tempn != "":
                    stack.append([int(tempn + s[i])])
                else:
                    stack.append([int(s[i])])
            elif stack and s[i] in string.ascii_lowercase:
                temp += s[i]
            elif stack and temp and s[i] == "[":
                stack[-2].append(temp)
                temp = ""
            elif stack and s[i] == "]":
                stack[-1].append(temp)
                temp = stack.pop()
                if stack and len(stack[-1]) > 1:
                    stack[-1][1] = stack[-1][1] + temp[1]*temp[0]
                elif stack:
                    stack[-1].append(temp[1] * temp[0])
                else:
                    ans = ans + temp[1]*temp[0]
                temp = ""
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.decodeString(input1)
        print(ans)
        return ans

    assert test("3[a]2[bc]") == "aaabcbc"
    assert test("3[a2[c]]") == "accaccacc"
    assert test("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert test("abc3[cd]xyz") =="abccdcdcdxyz"
    assert test("100[leetcode]") == "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"
    assert test("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
