"""
1979. Find Greatest Common Divisor of Array
Easy

Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
Example 3:

Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""
#79%
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        high = nums[0]
        low = nums[0]
        for i in range(1,len(nums)):
            high = max(high,nums[i])
            low = min(low,nums[i])
        return math.gcd(high,low)
"""
This solution finds the min and max in two passes instead of one but writes its own logic to find GCD
I think it would be faster to set gcd equal to one initially and then iterate backwards down to 1 and break once one is found
sample 36 ms submission
class Solution:
    def computeGCD(self, x, y):
        if x > y:
            small = y
        else:
            small = x
        for i in range(1, small+1):
            if((x % i == 0) and (y % i == 0)):
                gcd = i

        return gcd



    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        return self.computeGCD(mn, mx)
       
       
 
Euclidean Algorithm(MUST GRASP!!!): https://en.wikipedia.org/wiki/Euclidean_algorithm
a, b = min(nums), max(nums)
while a:
	a, b = b % a, a
return b

class Solution:
    def findGCD(self, A: List[int]) -> int:
        gcd = lambda a, b: a if not b else (gcd(a, b % a) if a < b else gcd(b, a % b))
        return gcd(min(A), max(A))
"""