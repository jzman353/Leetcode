"""
205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
#44%
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def mapp(st):
            d = {}
            l = []
            count = 0
            for letter in st:
                if letter not in d.keys():
                    d[letter] = count
                    count += 1
                l.append(d[letter])
            return l
        return mapp(s) == mapp(t)

"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # hashmap that stores the mapping, s->t
        # iterate through s and t 
            # check if violate curr mapping
                # return False
            # add to mapping
        # True
        
        mapping = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            # no char map to 2 diff chars
            if s[i] in mapping and mapping[s[i]] != t[i]:
                return False
            # no 2 char map to the same char
            if s[i] not in mapping and t[i] in mapping.values():
                return False
            mapping[s[i]] = t[i]
        return True

"""