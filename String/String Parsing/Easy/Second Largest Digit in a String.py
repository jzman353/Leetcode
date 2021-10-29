"""
1796. Second Largest Digit in a String
Easy

Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit.

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""
#84%
class Solution:
    def secondHighest(self, s: str) -> int:
        highest = -1
        s_highest = -1
        for i in s:
            if i in string.digits:
                if int(i) > highest:
                    s_highest = highest
                    highest = int(i)
                elif int(i) != highest and int(i) > s_highest:
                    s_highest = int(i)
        return s_highest

"""
Same as my solution except they dont convert to int, which saves a bit of time
sample 20 ms submission
class Solution:
    def secondHighest(self, s: str) -> int:
        x, y = '', ''
        for z in s:
            if z.isdigit():
                if z > x:
                    x, y = z, x
                    
                elif y < z < x:
                    y = z
        
        return int(y) if y else -1
"""