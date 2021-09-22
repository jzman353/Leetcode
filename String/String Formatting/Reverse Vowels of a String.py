"""
345. Reverse Vowels of a String
Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
#8%
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        head = 0
        tail = len(s)-1
        while head < tail:
            while s[head] not in vowels and head < tail:
                head += 1
            while s[tail] not in vowels and head < tail:
                tail -= 1
            if head < tail:
                s = s[:head]+s[tail]+s[head+1:tail]+s[head]+s[tail+1:]
            head += 1
            tail -= 1
        return s
"""
#5%
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s_v = []
        for i, ch in enumerate(s):
            if ch in vowels:
                s_v.append([i,ch])
        for i in range(len(s_v)//2):
            temp = s_v[i][0]
            s_v[i][0] = s_v[-(i+1)][0]
            s_v[-(i+1)][0] = temp
        for i in s_v:
            if i[0] < len(s):
                s = s[:i[0]]+i[1]+s[i[0]+1:]
            else:
                s = s[:i[0]]+i[1]
        return s
"""

"""
Apparently manipulating the list is must faster than rewriting the string every time you want to change it because in the string's case you are rebuilding the whole thing every time
class Solution:
    def reverseVowels(self, s: str) -> str:
        n, s = len(s), list(s)
        
        l, r = -1, n
        
        V = "aeiouAEIOU"
        
        while True:
            l, r = l+1, r-1
            while l < n and s[l] not in V :
                l += 1
            while r >= 0 and s[r] not in V:
                r -= 1
            if l >= r:
                break
            s[l], s[r] = s[r], s[l]
        
        return "".join(s)
"""