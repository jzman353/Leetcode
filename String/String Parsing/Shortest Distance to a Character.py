"""
821. Shortest Distance to a Character
Easy

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]



Note:

    S string length is in [1, 10000].
    C is a single character, and guaranteed to be in string S.
    All letters in S and C are lowercase.
"""

class Solution:
    def shortestToChar(self, S: str, C: str):
        import collections
        indexes = collections.deque([i for i, c in enumerate(S) if c == C])
        ans = []
        for i in range(len(S)):
            temp1 = abs(i-indexes[0])
            if len(indexes) > 1 and temp1 > abs(i-indexes[1]):
                indexes.popleft()
                temp1 = abs(i-indexes[0])
            ans.append(temp1)
        return ans