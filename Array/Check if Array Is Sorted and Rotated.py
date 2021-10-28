"""
1752. Check if Array Is Sorted and Rotated
Easy

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
Example 4:

Input: nums = [1,1,1]
Output: true
Explanation: [1,1,1] is the original sorted array.
You can rotate any number of positions to make nums.
Example 5:

Input: nums = [2,1]
Output: true
Explanation: [1,2] is the original sorted array.
You can rotate the array by x = 5 positions to begin on the element of value 2: [2,1].

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

class Solution:
    def check(self, nums: List[int]) -> bool:
        s_nums = sorted(nums)
        for i in range(len(nums)):
            rotated = nums[i:]+nums[:i]
            if s_nums == rotated:
                return True
        return False

"""
sample 16 ms submission
class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        left, right = 0, len(nums) - 1
        while left < len(nums) - 2 and nums[left + 1] >= nums[left]:
            left += 1
        while right > 0 and nums[right - 1] <= nums[right]:
            right -= 1
        
        if left == len(nums) - 2 and right == 0:
            return True
        if left + 1 == right and nums[-1] <= nums[0]:
            return True
        return False

same as my solution:
sample 20 ms submission
class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        cp = copy.deepcopy(nums)
        
        while True:
            if cp == sorted_nums:
                return True
            
            temp = cp.pop()
            cp.insert(0, temp)
            
            if cp == nums:
                return False
"""