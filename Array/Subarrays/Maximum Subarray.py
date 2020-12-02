"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-2147483647]
Output: -2147483647

Constraints:

    1 <= nums.length <= 2 * 104
    -231 <= nums[i] <= 231 - 1
"""

#Kadane's algorithm
#96%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float('-inf')
        current_sum = float('-inf')
        for x in nums:
            # If x is positive, the max will always be current_sum + x
            # If x is negative, keep the current_sum until current_sum is negative
            # and then it makes sense to just start current_sum over
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum