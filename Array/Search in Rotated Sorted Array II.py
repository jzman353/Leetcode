"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:

    This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
    Would this affect the run-time complexity? How and why?
"""

#24%
import bisect
class Solution:
    def search(self, nums, target: int) -> bool:
        if not nums:
            return False
        nums.sort()
        ind = bisect.bisect_left(nums, target)
        return ind < len(nums) and nums[ind] == target

"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0: return False
        end = n - 1
        start = 0
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if not nums[start] != nums[mid]:
                start += 1
                continue
            pivotArray = nums[start] <= nums[mid]
            targetArray = nums[start] <= target
            if pivotArray ^ targetArray:
                if pivotArray:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False
"""