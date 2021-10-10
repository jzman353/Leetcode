"""
747. Largest Number At Least Twice of Others
Easy

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
Example 3:

Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
"""
#89%
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0]>nums[1]:
            max1 = nums[0]
            max2 = nums[1]
            ind = 0
        else:
            max2 = nums[0]
            max1 = nums[1]
            ind = 1
        for i in range(2,len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
                ind = i
            elif nums[i] > max2:
                max2 = nums[i]
        if max1 >= 2*max2:
            return ind
        else:
            return -1

"""
#I think my solution is better than this actually because this solution searches through the list like 3 times and mine only does once
#The second place solution is the same as mine so I will just say assume my solution is 100% or close to it
sample 20 ms submission
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
        for i in nums:
            if i == maxNum:
                continue
            if maxNum < 2*i:
                return -1
        
        return nums.index(maxNum)
"""