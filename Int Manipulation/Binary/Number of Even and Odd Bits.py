"""
2595. Number of Even and Odd Bits
Easy

You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].

Example 1:

Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001.
It contains 1 on the 0th and 4th indices.
There are 2 even and 0 odd indices.
Example 2:

Input: n = 2
Output: [0,1]
Explanation: The binary representation of 2 is 10.
It contains 1 on the 1st index.
There are 0 even and 1 odd indices.

Constraints:

1 <= n <= 1000
"""
#37%
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        flag = False
        for i in str(bin(n)[len(bin(n)):1:-1]):
            if i == '1':
                if not flag:
                    even += 1
                else:
                    odd += 1
            flag = not flag
        return [even,odd]

"""
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        i, evens, odds = 0, 0, 0
        
        while n:
            if n%2:
                if i%2: odds += 1
                else: evens += 1
            n //= 2
            i += 1
        return evens, odds
        
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        n = str(bin(n)[2:][::-1])

        for i in range(len(n)):
            if n[i] == "1":
                ans[i % 2] += 1
            
        return ans
"""

"""
import random
def number_between_0_and_1000():
    for i in range(8):
        print(random.randint(0, 1000))

number_between_0_and_1000()
"""