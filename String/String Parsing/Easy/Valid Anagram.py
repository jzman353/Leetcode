"""
242. Valid Anagram
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
#100%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        keys = set(c1.keys()).union(c2.keys())
        
        for key in keys:
            if key not in c1 or key not in c2 or c1[key] != c2[key]:
                return False
            
        return True
"""