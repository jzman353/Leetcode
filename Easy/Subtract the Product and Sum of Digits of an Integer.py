'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5

How to compute all digits of the number ?
Use modulus operator (%) to compute the last digit.
Generalise modulus operator idea to compute all digits.

Runtime: 28 ms Beats 73%
Memory Usage: 12.7 MB
'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits=[]
        for i in str(n):
            digits.append(i)
        summ=0
        product=1
        for i in digits:
            summ=summ+int(i)
            product=product*int(i)
        return product-summ

'''
Runtime: 12 ms

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        l = [int(d) for d in str(n)]
        for i in l:
            p *= int(i)
            s += int(i)
        return p - s

Runtime: 8 ms

from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        A = list(map(int, str(n)))
        return reduce(lambda x,y : x*y, A) - sum(A)
'''



