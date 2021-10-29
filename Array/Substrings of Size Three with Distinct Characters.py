"""
1876. Substrings of Size Three with Distinct Characters
Easy

A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
"""
#59%
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        ans = 0
        d = defaultdict(int)
        d[s[0]] += 1
        d[s[1]] += 1
        for i in range(2,len(s)):
            d[s[i]] += 1
            if max(d.values()) == 1:
                ans += 1
            d[s[i-2]] -= 1
        return ans
"""
#15%
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-2):
            c = Counter(s[i:i+3])
            if c.most_common(1)[0][1] == 1:
                ans += 1
        return ans
"""
"""
sample 12 ms submission
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        i,j,k = 0,1,2
        rst = 0
        while k < len(s):
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                rst += 1
            i+=1
            j+=1
            k+=1
        return rst
"""