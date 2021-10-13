"""
1957. Delete Characters to Make Fancy String
Easy

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
"""
#5%
class Solution:
    def makeFancyString(self, s: str) -> str:
        l = list(s)
        counter = 1
        for i in range(len(s)-2,-1,-1):
            if s[i+1] == s[i]:
                counter += 1
                if counter >= 3:
                    del l[i]
            else:
                counter = 1
        return "".join(l)

"""
sample 460 ms submission
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[:2]
        for c in s[2:]:
            if c != res[-1] or c != res[-2]:
                res += c
        return res

sample 316 ms submission
class Solution:
    def makeFancyString(self, s: str) -> str:
        l1, l2 = 0, len(s)
        masks = [(c*3, c*2) for c in string.ascii_lowercase]
        while l1 != l2:
            l1 = l2
            for m in masks:
                s = s.replace(m[0], m[1])
            l2 = len(s)
            
        return s
"""