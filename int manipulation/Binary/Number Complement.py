'''
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
num >= 1
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
Runtime: 20 ms Beats 98%
Memory Usage: 13.6 MB
'''

class Solution:
    def findComplement(self, num: int) -> int:
        '''
        bin = []
        binaryString = ''
        def decimalToBinary(num,bin):
            if num > 1:
                decimalToBinary(num // 2,bin)
            bin.append(num % 2)
        decimalToBinary(num,bin)
        for count,i in enumerate(bin):
            if i==1:
                bin[count]=0
            if i==0:
                bin[count]=1
            binaryString = binaryString+str(bin[count])
        #Decimal = int(binaryString, 2)
        return int(binaryString, 2)
        '''
        binary = str(bin(num))
        binary = binary[2:]
        binaryString = ''
        for i in binary:
            if i=="1":
                binaryString=binaryString+"0"
            if i=="0":
                binaryString=binaryString+"1"
        return int(binaryString, 2)
        