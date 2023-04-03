"""
2609. Find the Longest Balanced Substring of a Binary String
Easy

You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.
Example 2:

Input: s = "00111"
Output: 4
Explanation: The longest balanced substring is "0011", which has length 4.
Example 3:

Input: s = "111"
Output: 0
Explanation: There is no balanced substring except the empty substring, so the answer is 0.

Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '1'
"""
#100%
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        count_zeros = 0
        count_ones = 0
        for i in s:
            if i == '0':
                if count_ones:
                    count_zeros = 0
                    count_ones = 0
                count_zeros += 1
            else:
                count_ones += 1
                if count_ones <= count_zeros:
                    ans = max(ans, count_ones*2)
        return ans
"""
import random

def generate_random_string():
    length = random.randint(30, 50)
    return ''.join(random.choices(['0', '1'], k=length))

random_string = generate_random_string()
print(random_string)
"""