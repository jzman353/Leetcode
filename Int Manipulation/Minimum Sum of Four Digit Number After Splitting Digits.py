"""
2160. Minimum Sum of Four Digit Number After Splitting Digits
Easy

You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

Example 1:

Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
Example 2:

Input: num = 4009
Output: 13
Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc.
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.

Constraints:

1000 <= num <= 9999
"""
#75%
class Solution:
    def minimumSum(self, num: int) -> int:
        num1 = ""
        num2 = ""
        count = 0
        for i in sorted(list(str(num))):
            if count == 0:
                num1 += i
                count = 1
            else:
                num2 += i
                count = 0
        return int(num1)+int(num2)

"""First get the digits of num. Then sort the digits. Then without even making two different numbers, just multiply 
the two smaller ones by ten and add them to the two larger numbers. sample 12 ms submission class Solution: 
def minimumSum(self, num: int) -> int: digit = [] for i in range(1, 5): temp = num % 10 digit.append(temp) num -= 
temp num = num // 10 digit.sort() res = (digit[0] + digit[1]) * 10 + digit[2] + digit[3] return res """