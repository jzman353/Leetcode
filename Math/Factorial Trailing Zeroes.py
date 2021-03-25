"""
24%
172. Factorial Trailing Zeroes
Easy

Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0

Constraints:

0 <= n <= 104
"""
import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        sol = math.factorial(n)
        ans = reversed(str(sol))
        count = 0
        for i in ans:
            if i == '0':
                count += 1
            else:
                break
        return count

"""
class Solution:
    def trailingZeroes(self, n: int) -> int:        
        return sum(n // (5 **i) for i in range(1, 7))]
        
def trailingZeroes(self, n: int) -> int:
	result = n//5
	if result < 5:
		return result
	else:
		return self.trailingZeroes(result) + result
		
    count = 0
 
def trailingZeroes(self, n: int) -> int:
    # Initialize result
    count = 0
    # Keep dividing n by
    # 5 & update Count
    while(n >= 5):
        n //= 5
        count += n
 
    return count

Given an integer n, write a function that returns count of trailing zeroes in n!. 
Examples : 

Input: n = 5
Output: 1 
Factorial of 5 is 120 which has one trailing 0.

Input: n = 20
Output: 4
Factorial of 20 is 2432902008176640000 which has
4 trailing zeroes.

Input: n = 100
Output: 24
We strongly recommend that you click here and practice it, before moving on to the solution.
Approach:
A simple method is to first calculate factorial of n, then count trailing 0s in the result (We can count trailing 0s by repeatedly dividing the factorial by 10 till the remainder is 0).
 
The above method can cause overflow for slightly bigger numbers as the factorial of a number is a big number (See factorial of 20 given in above examples). The idea is to consider prime factors of a factorial n. A trailing zero is always produced by prime factors 2 and 5. If we can count the number of 5s and 2s, our task is done. Consider the following examples.
n = 5: There is one 5 and 3 2s in prime factors of 5! (2 * 2 * 2 * 3 * 5). So a count of trailing 0s is 1.
n = 11: There are two 5s and eight 2s in prime factors of 11! (2 8 * 34 * 52 * 7). So the count of trailing 0s is 2.
 
We can easily observe that the number of 2s in prime factors is always more than or equal to the number of 5s. So if we count 5s in prime factors, we are done. How to count the total number of 5s in prime factors of n!? A simple way is to calculate floor(n/5). For example, 7! has one 5, 10! has two 5s. It is not done yet, there is one more thing to consider. Numbers like 25, 125, etc have more than one 5. For example, if we consider 28! we get one extra 5 and the number of 0s becomes 6. Handling this is simple, first, divide n by 5 and remove all single 5s, then divide by 25 to remove extra 5s, and so on. Following is the summarized formula for counting trailing 0s.
Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
"""