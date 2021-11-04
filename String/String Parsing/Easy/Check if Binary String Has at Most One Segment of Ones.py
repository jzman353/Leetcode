"""
1784. Check if Binary String Has at Most One Segment of Ones
Easy

Given a binary string s without leading zeros, return true if s contains at most one contiguous segment of ones.
Otherwise, return false.

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true

Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
s[0] is '1'.
"""

#85%
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        switched = False
        for i in range(1,len(s)):
            if s[i] != "1" and not switched:
                switched = True
            elif s[i] == "1" and switched:
                return False
        return True

"""
#This solution is probably faster by two lines: creating and switching the switched variable
sample 12 ms submission
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 1
        while i < len(s) and s[i]=='1':
            i+=1
        if i == len(s):
            return True
        while i < len(s) and s[i]=='0':
            i+=1
        if i == len(s):
            return True
        return False
"""