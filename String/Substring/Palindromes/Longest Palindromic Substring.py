"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters (lower-case and/or upper-case),
"""

#5%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        maxx = 0
        for i in range(len(s)-1):
            for j in range(len(s)-1,i,-1):
                word = s[i:j+1]
                if word == word[::-1]:
                    maxx = max(maxx, j+1-i)
                    if j+1-i == maxx:
                        ans = word
                    break
        return ans

"""
#Expand from the center 87%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        max_l, offset = 0, 1
        # expand a window from the center at each position
        for i in range(len(s)):
            l, r = i, i
            # special case: repeated center
            while r < len(s) - 1 and s[l] == s[r+1]:
                r += 1
			# expand
            while 0 <= l and r < len(s) and s[l] == s[r]:
                # update max seen so far
                if r+1 - l > offset:
                    offset, max_l = r+1 - l, l
                r += 1
                l -= 1
        return s[max_l: max_l + offset]
"""


if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.longestPalindrome(input1)
        print(ans)
        return ans

    assert test("babad") == "aba"
    assert test("cbbd") == "bb"
    assert test("a") == "a"
    assert test("ac") == "a"