"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict
#82%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        d = defaultdict(int)
        d[s[0]] = 1
        maxx = 1
        curr = 1
        prev = 0
        for i in range(1, len(s)):
            if d[s[i]] != 1:
                curr += 1
                d[s[i]] = 1
            else:
                maxx = max(maxx,curr)
                for j in range(prev,len(s)):
                    if s[j] != s[i]:
                        d[s[j]] = 0
                        curr -= 1
                    else:
                        prev = j+1
                        break
        return max(maxx,curr)

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.lengthOfLongestSubstring(input1)
        print(ans)
        return ans


    assert test("") == 0
    assert test("abcabcbb") == 3
    assert test("bbbbb") == 1
    assert test("pwwkew") == 3
    assert test("aabaab!bb") == 3

"""
sample 24 ms submission
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        word = ""
        for c in s:
            if c not in word:
                word += c
                if len(word) > res:
                    res = len(word)
            else:
                word = word[word.find(c) + 1:] + c
        return res
"""