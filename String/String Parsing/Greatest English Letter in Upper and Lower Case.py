"""
2309. Greatest English Letter in Upper and Lower Case
Easy

Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
An English letter b is greater than another letter a if b appears after a in the English alphabet.

Example 1:

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.
Example 2:

Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
Example 3:

Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case.

Constraints:

1 <= s.length <= 1000
s consists of lowercase and uppercase English letters.
"""
#77.14%
class Solution:
    def greatestLetter(self, s: str) -> str:
        l = set()
        m = -1
        for i in s:
            l.add(i)
            if i.upper() in s and i.lower() in s:
                m = max(m,ord(i))
        if m == -1:
            return ""
        else:
            return chr(m).upper()

"""
Sample 22 ms submission

class Solution:
    def greatestLetter(self, s: str) -> str:
        l=set(s)
        m=97
        for i in sorted(l,reverse=True):
            if i.isupper() and i.lower() in l:
                return i.upper()
        return ''
"""