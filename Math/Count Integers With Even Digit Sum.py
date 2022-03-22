"""
2180. Count Integers With Even Digit Sum
Easy

Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.

Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.
Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

Constraints:

1 <= num <= 1000
"""
#99%
class Solution:
    def countEven(self, num: int) -> int:
        if (num%2 == 1) or (1000 > num > 100 and ((num//100)%2+((num//10)%10)%2+(num%10)%2)%2==0) or (100 > num > 10 and ((num//10)%2+(num%10)%2)%2==0) or (num < 10 and num%2 == 0):
            return num//2
        else:
            return num//2-1
"""
#96%
class Solution:
    def countEven(self, num: int) -> int:
        if num%2 == 0:
            if num < 10:
                return (num%10)//2
            elif num < 100:
                return 4+5*(num//10-1)+((num//10)%2==0)+(num%10)//2
            elif num < 1000:
                return 49+50*(num//100-1)+5*((num%100)//10)+(((num//100)%2==0 and (num//10)%2==0)or((num//100)%2==1 and (num//10)%2==1))+(num%10)//2
            else:
                return 499
        else:
            return 5*(num//10)+math.ceil((num%10)/2)-1
"""
"""
class Solution:
    def countEven(self, num: int) -> int:
        if num%2 == 0:
            if num < 10:
                return (num%10)//2
            elif num < 100:
                return 4+5*(num//10-1)+((num//10)%2==0)+(num%10)//2
            elif num < 1000:
                return 49+50*(num//100-1)+5*((num%100)//10)+(((num//100)%2==0 and (num//10)%2==0)or((num//100)%2==1 and (num//10)%2==1))+(num%10)//2
            else:
                return 499
        else:
            return int(num/2)
"""
"""
class Solution:
    def countEven(self, num: int) -> int:
        odd = [1 if int(d)%2 == 1 else 0 for d in str(num)]
        if num%2 == 1 or sum(odd)%2 == 0:
            return num//2
        else:
            return num//2-1
"""
"""
sample 16 ms submission
class Solution:
    def countEven(self, num: int) -> int:
        n, dSum = num, 0
        while n > 0: # Calculate digit sum of numbers
            dSum += n%10
            n = n//10
        if num % 2 == 0 and dSum % 2 == 1:
            return num//2 - 1
        return num//2
"""