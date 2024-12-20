"""
441. Arranging Coins
Easy

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""
#35%
class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        while n >= 0:
            count += 1
            n -= count
        return count - 1

"""
Arithmetic sum formula:
sum = n/2(2a+(n-1)d)
a is the first term, which is 1
d is the increment, which is 1
n is the max term, which we are searching for
the sum is given

Approach 1: Binary Search
This question is easy in a sense that one could run an exhaustive iteration to obtain the result. That could work, except that it would run out of time when the input becomes too large. So let us take a step back to look at the problem, before rushing to the implementation.

Assume that the answer is kk, i.e. we've managed to complete kk rows of coins. These completed rows contain in total 1 + 2 + ... + k = \frac{k (k + 1)}{2}1+2+...+k= 
2
k(k+1)
​	
  coins.

We could now reformulate the problem as follows:

Find the maximum kk such that \frac{k (k + 1)}{2} \le N 
2
k(k+1)
​	
 ≤N.

The problem seems to be one of those search problems. And instead of naive iteration, one could resort to another more efficient algorithm called binary search, as we can find in another similar problem called search insert position.

Implementation
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right

Complexity Analysis
Time complexity : O(logN).
Space complexity : O(1).

Approach 2: Math
If we look deeper into the formula of the problem, we could actually solve it with the help of mathematics, without using any iteration.

As a reminder, the constraint of the problem can be expressed as follows:

k(k + 1) <= 2N
This could be solved by completing the square technique,
(k+0.5)**2-0.25<=2N
k=((2 * n + 0.25)**0.5 - 0.5)

Implementation
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)

Time complexity : O(1).
Space complexity : O(1).
"""