"""
405. Convert a Number to Hexadecimal
Easy

Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"

Constraints:

-231 <= num <= 231 - 1
"""
#84%
class Solution:
    def toHex(self, num: int) -> str:
        return str(hex((num + (1 << 32)) % (1 << 32)))[2:]

"""
class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += (1 << 32)
        return hex(num)[2:]

sample 16 ms submission
class Solution:
    def toHex(self, num: int) -> str:
        if num<0:
            num = 2**32 + num
        elif num ==0:
            return '0'
        
        list1 = deque([])
        while num>0:
            n = num%16
            if n>9:
                n=chr(97+n-9-1)
            list1.appendleft(n)
            num = num//16
            
        # list1.appendleft(num)
        
        list1 = list(list1)
        list1 = ''.join([str(x) for x in list1])

class Solution:
    def toHex(self, num: int) -> str:
        if num==0: return '0'
        maps='0123456789abcdef'
        ans=""
        for i in range(8) :
            c=maps[num%16]            
            ans=c+ans
            num=num>>4
        return ans.lstrip("0")

class Solution:
    def toHex(self, num: int) -> str:
        hmap = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', \
           9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    
        result = []
        for _ in range(8):
            result.append(hmap[num%16])
            num = num >> 4
            if num == 0:
                break
        result.reverse()
        return ''.join(result)
"""