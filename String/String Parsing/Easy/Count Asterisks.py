"""
2315. Count Asterisks
Easy

You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.

Example 1:

Input: s = "l|*e*et|c**o|*de|"
Output: 2
Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
The characters between the first and second '|' are excluded from the answer.
Also, the characters between the third and fourth '|' are excluded from the answer.
There are 2 asterisks considered. Therefore, we return 2.
Example 2:

Input: s = "iamprogrammer"
Output: 0
Explanation: In this example, there are no asterisks in s. Therefore, we return 0.
Example 3:

Input: s = "yo|uar|e**|b|e***au|tifu|l"
Output: 5
Explanation: The considered characters are underlined: "yo|uar|e**|b|e***au|tifu|l". There are 5 asterisks considered. Therefore, we return 5.

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters, vertical bars '|', and asterisks '*'.
s contains an even number of vertical bars '|'.
"""

#95%
class Solution:
    def countAsterisks(self, s: str) -> int:
        looking = True
        ans = 0
        for i in s:
            if i == "|":
                looking = not looking
            elif looking and i == "*":
                ans += 1
        return ans

"""
class Solution:
    def countAsterisks(self, s: str) -> int:
        ans=0
        x=s.split("|")
        for i in range(0,len(x),2):
            ans += x[i].count('*')
        return ans
"""