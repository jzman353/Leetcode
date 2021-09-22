"""
392. Is Subsequence
Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
#76%
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        head = 0
        for i in range(len(s)):
            while head<len(t) and t[head] != s[i]:
                if head >= len(t):
                    return False
                head += 1
            if head < len(t):
                head += 1
            else:
                return False
        return True

"""
sample 12 ms submission
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = 0
        for i in range(0,len(s),1):
            if s[i] in t:
                p = t.index(s[i])
                t = t[p+1:]
                x+=1
            #I think it may be faster to include an else return false statement here
        if x==len(s):
            return True
        else:
            return False 
"""