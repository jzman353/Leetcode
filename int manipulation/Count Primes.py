"""
204. Count Primes
Easy

Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0



Constraints:

    0 <= n <= 5 * 106

Accepted
394.3K
Submissions
1.2M

Sieve of Erathosthenes algorithm
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1] * n

        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i] = [0] * ((n-1-i*i)//i+1)

        return max(0, sum(primes) - 2)