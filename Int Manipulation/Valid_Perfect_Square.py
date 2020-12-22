'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1

Runtime: 32 ms Beats 54%
Memory Usage: 13.8 MB
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k=num**(1/2)
        if k.is_integer():
            return True
        else:
            return False

print(isPerfectSquare(16))
print(isPerfectSquare(14))