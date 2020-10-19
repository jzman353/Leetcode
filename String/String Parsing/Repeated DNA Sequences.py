"""
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.



Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]



Constraints:

    0 <= s.length <= 105
    s[i] is 'A', 'C', 'G', or 'T'.
"""
import collections
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        c = collections.Counter()
        for i in range(len(s)-9):
            word = s[i:i+10]
            c[word] += 1
        ans = []
        for i in c.keys():
            if c[i] > 1:
                ans.append(i)
        return ans
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if s is None or len(s)==0:
            return []
        
        n= len(s)
        result = set()
        hashset =set()
        for i in range(n-10+1):
            sub = s[i:i+10]
            if sub in hashset:
                result.add(sub)
                
            hashset.add(sub)
        
        return list(result)
"""