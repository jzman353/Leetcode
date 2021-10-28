"""
1790. Check if One String Swap Can Make Strings Equal
Easy

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
Example 4:

Input: s1 = "abcd", s2 = "dcba"
Output: false

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""
#72%
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if set(s1) != set(s2):
            return False
        count1 = []
        count2 = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count1.append(s1[i])
                count2.append(s2[i])
            if len(count1) == 3:
                return False
        return len(count1) < 3 and set(count1)==set(count2)

"""
This solution is a bit more simple than mine. Note that the length check is not necessary given the input constraints

sample 12 ms submission
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        elif len(s1)!=len(s2):
            return False
        
        idx = []
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                continue
            else:
                idx.append((s1[i],s2[i]))
        if len(idx)>2:
            return False
        elif len(idx)==2:
            if idx[0][0]==idx[1][1] and idx[0][1]==idx[1][0] :
                return True
        else:
            return False
"""