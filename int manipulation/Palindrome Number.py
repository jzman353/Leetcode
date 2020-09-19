'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
Beware of overflow when you reverse the integer.

Runtime: 72 ms Beats 20%
Memory Usage: 14 MB
'''

import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        Right=len(string)-1
        Left=0
        if(len(string)%2==1):    #odd # of characters
            Midpoint_index=int((len(string)-1)/2)
            for i in range(Midpoint_index):
                if string[Right]!=string[Left]:
                    return False
                else:
                    Right-=1
                    Left+=1
            return True
                
        else:                   #Even # of characters
            Right_of_Midpoint=math.ceil((len(string)-1)/2)
            for i in range(Right_of_Midpoint):
                if string[Right]!=string[Left]:
                    return False
                else:
                    Right-=1
                    Left+=1
            return True

'''
Runtime: 32 ms

class Solution:
    def isPalindrome(self, x: int) -> bool:       
        
#         if ((x < 0) or ((x % 10 == 0) and (x != 0))):
#             return False
        
#         reverse = 0
        
#         while (x > reverse):
#             reverse = reverse * 10 + x % 10
#             x = x // 10
        
#         return x == reverse or x == reverse // 10

        s = str(x)
        return s == s[::-1]

Runtime: 28 ms

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s==s[::-1]:
            return(True)
        else:
            return(False)
'''





