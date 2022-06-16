"""
784. Letter Case Permutation
Medium

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""
#13%
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.answer = []
        def helper(idx=0, curr=''):
            while idx < len(s) and s[idx] in string.digits:
                curr += s[idx]
                idx += 1
            if idx == len(s):
                self.answer.append(curr)
            else:
                helper(idx+1, curr+s[idx].upper())
                helper(idx+1, curr+s[idx].lower())
        helper()
        return self.answer

"""
sample 31 ms submission
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = ['#']
        for char in s:
            new_results = []
            
            if char.isalpha():
                a, b = char.lower(), char.upper()
                for x in results:
                    new_results.append(x + a)
                    new_results.append(x + b)
            else:
                a = char
                for x in results:
                    new_results.append(x + a)
            
            results = new_results
        
        return [v[1:] for v in results]
"""