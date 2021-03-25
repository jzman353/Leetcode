"""
87%
1175. Prime Arrangements

Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015

Constraints:

1 <= n <= 100
"""
import math
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def countPrimes(n: int) -> int:
            primes = [1] * n

            for i in range(2, int(n**0.5)+1):
                if primes[i]:
                    primes[i*i:n:i] = [0] * ((n-1-i*i)//i+1)

            return max(0, sum(primes) - 2)
        num_primes = countPrimes(n+1)
        print(num_primes)
        return (math.factorial(num_primes)*math.factorial(n-num_primes))%(10**9+7)

"""

from math import factorial as f
class Solution:
    def numPrimeArrangements(self, n):
        if n < 3: return 1
        def prime(n):
            isP = [True] * (n + 1)
            isP[0], isP[1] = False, False
            upper = int(n**0.5)
            for i in range(2, upper+1):
                if isP[i] is True:
                    isP[i*i::i] = [False] * len(isP[i*i::i])
            return sum(isP)
        v = prime(n)
        return (f(v) * f(n-v)) % 1000000007
"""