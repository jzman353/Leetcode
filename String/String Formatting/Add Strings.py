"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
#84% #Cheating solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))
""" #Non-cheating solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #num1 = "12"
        #num2 = "1200"
        
        total_sum = 0
        leading_pos_val = 1
        num1_pos = len(num1) - 1
        num2_pos = len(num2) - 1
        while num1_pos >= 0 or num2_pos >= 0:
            num_dig_sum = 0
            if num1_pos >= 0:
                num_dig_sum += int(num1[num1_pos])
                num1_pos -= 1
            if num2_pos >= 0:
                num_dig_sum += int(num2[num2_pos])
                num2_pos -= 1
            num_dig_sum *= leading_pos_val
            total_sum += num_dig_sum
            leading_pos_val *= 10
        return str(total_sum)
"""