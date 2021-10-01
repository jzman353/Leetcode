"""
1952. Three Divisors
Easy

Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.

Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.

Constraints:

1 <= n <= 104
"""
class Solution:
    def isThree(self, n: int) -> bool:
        d = []
        for i in range(1,math.ceil(sqrt(n))+1):
            if n%i==0:
                d.append(i)
                if n//i is not i:
                    d.append(n//i)
        return len(d) == 3

"""
Finding: The number will have to be a perfect square to have 3 divisors
You can check if it is a perfect square to save some time in the for loop
1 and the number are always included so that is assumed to be the perfect case
Any other divisor can break the for loop
class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1 or n ==2 or n ==3:
            return False
        root = math.floor(math.sqrt(n))
        if root**2 != n:
            return False
        else:
            for i in range(2,root//2):
                if n % i ==0:
                    return False
        return True
"""