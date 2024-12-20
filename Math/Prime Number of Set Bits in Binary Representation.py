"""
762. Prime Number of Set Bits in Binary Representation
Easy

Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101, which has 3 set bits.

Example 1:

Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.
Example 2:

Input: left = 10, right = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.

Constraints:

1 <= left <= right <= 10^6
0 <= right - left <= 10^4
"""
#70%
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left,right+1):
            temp = str(bin(i))[2:]
            c1 = temp.count("1")
            ans += c1 in [2, 3, 5, 7, 11, 13, 17, 19] #note that 10^6 can have 19 1s max
        return ans
#60%
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left,right+1):
            temp = str(bin(i))[2:]
            c1 = temp.count("1")
            #print(f"{temp=} {c1=}")
            prime = True
            if c1 != 1:
                for j in range(2,(c1//2 + 1)):
                    if c1 % j == 0:
                        prime = False
                        break
                #print(f"{c1=} {prime=}")
                ans += prime
        return ans

"""
sample 152 ms submission
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(1 for i in range(left, right+1) if bin(i).count('1') in primes)
"""