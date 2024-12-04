"""
491. Non-decreasing Subsequences
Solved
Medium
Topics
Companies
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]

Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100

48%
"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        s = set()
        def helper(curr, remaining):
            s.add(tuple(curr))
            for i in range(len(remaining)):
                if not curr or (remaining[i] >= curr[-1] and tuple(curr+[remaining[i]]) not in s):
                    helper(curr+[remaining[i]], remaining[i+1:])
        helper([], nums)
        res = list([i for i in s if len(i)>=2])
        return res