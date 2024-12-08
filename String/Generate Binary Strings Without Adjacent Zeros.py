"""
3211. Generate Binary Strings Without Adjacent Zeros
Solved
Medium
Topics
Companies
Hint
You are given a positive integer n.

A binary string x is valid if all
substrings
 of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.

Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".

Constraints:

1 <= n <= 18
"""
class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.possibilities = []
        def helper(path):
            if len(path) == n:
                self.possibilities.append(path)
            else:
                if not path or path[-1] == '1':
                    helper(path + "0")
                    helper(path + "1")
                else:
                    helper(path + "1")
        helper("")
        return self.possibilities
"""
class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ['0', '1']
        for _ in range(n-1):
            nextRes = []
            for s in res:
                if s[-1] == '1':
                    nextRes.append(s + '0')
                nextRes.append(s + '1')
            res = nextRes
        return res
"""