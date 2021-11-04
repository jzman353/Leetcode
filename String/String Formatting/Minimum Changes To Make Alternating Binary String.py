"""
1758. Minimum Changes To Make Alternating Binary String
Easy

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.
"""
#91%
class Solution:
    def minOperations(self, s: str) -> int:
        count0 = 0
        count1 = 0
        for i in range(len(s)):
            if i%2 == 0:
                if s[i] == "0":
                    count0 += 1
                else:
                    count1 += 1
            else:
                if s[i] == "0":
                    count1 += 1
                else:
                    count0 += 1
        return min(count0,count1)

"""
This solution is very elegant because it only calculates one of the two options and then it finds out if that is the 
best one and then it returns it otherwise it just subtracts from len(s
sample 16 ms submission
class Solution:
    def minOperations(self, s: str) -> int:
        alt_bits = s[0::2].count('1')+s[1::2].count('0')
        if alt_bits <= len(s)/2:
            return(alt_bits)
        else:
            return(len(s) - alt_bits)
"""