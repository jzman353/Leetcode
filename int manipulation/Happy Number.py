"""
#80%
202. Happy Number
Easy

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        squares = [0,1,4,9,16,25,36,49,64,81]
        dict2 = {}
        num = n
        while 1:
            summ = 0
            for i in str(num):
                summ += squares[int(i)]
            if summ == 1:
                return True
            if summ in dict2.keys():
                return False
            dict2[summ] = 1
            num = summ

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.isHappy(input1)
        print(ans)

    input1 = 19
    test(input1) #True

    #import timit
    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))