"""
1422. Maximum Score After Splitting a String
Easy

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:

Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3


Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
"""
#90%
class Solution:
    def maxScore(self, s: str) -> int:
        if s[0] == "0":
            zeros = 1
            ones = s.count("1")
        else:
            zeros = 0
            ones = s.count("1")-1
        maxx = zeros + ones
        for i in range(1,len(s)-1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            maxx = max(maxx,zeros+ones)
        return maxx

"""
This solution is the same as mine except it doesn't have to count the first digit in the ones
sample 16 ms submission
class Solution:
    def maxScore(self, s: str) -> int:
        zero = 1 if s[0]=='0' else 0
        one = s[1:].count('1')
        score=one+zero
        for i in range(1,len(s)-1):
            if s[i]=='0':
                zero+=1
            else:
                one-=1
            score=max(one+zero, score)
        return score
"""