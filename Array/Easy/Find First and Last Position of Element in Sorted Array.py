"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
#54%
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = bisect.bisect_left(nums,target)
        y = bisect.bisect_right(nums,target)
        if x == y:
            return [-1,-1]
        else:
            return [x,y-1]

"""
sample 68 ms submission
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target > nums[-1] or target < nums[0]:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                l, r = mid, mid
                while l >= left and nums[l] == target:
                    l -= 1
                while r <= right and nums[r] == target:
                    r += 1
                return [l+1, r-1]
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        if nums[left] == target:
            return [left, left]
        
        return [-1, -1]

def searchRange(self, nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x > A[mid]: left = mid + 1
            else: right = mid - 1
        return left

    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x >= A[mid]: left = mid + 1
            else: right = mid - 1
        return right
        
    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]
"""