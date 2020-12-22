"""
594. Longest Harmonious Subsequence
Easy

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]
Output: 2

Example 3:

Input: nums = [1,1,1,1]
Output: 0

Constraints:

    1 <= nums.length <= 2 * 104
    -109 <= nums[i] <= 109
"""
"""
#First attempt: nested loops O(2*n^2) Time limit exceeded
class Solution:
    def findLHS(self, nums) -> int:
        ans = 0
        for i in range(len(nums)):
            count = 0
            j = i+1
            one = False
            while j < len(nums):
                if nums[j] == nums[i] or nums[j] == nums[i] + 1:
                    count += 1
                    if nums[j] == nums[i] + 1:
                        one = True
                j += 1
            if one:
                ans = max(ans,count+1)
            count = 0
            j = i+1
            one = False
            while j < len(nums):
                if nums[j] == nums[i] or nums[j] == nums[i] - 1:
                    count += 1
                    if nums[j] == nums[i] - 1:
                        one = True
                j += 1
            if one:
                ans = max(ans, count+1)
        return ans
"""
"""
#Second attempt: counter #30%
import collections
class Solution:
    def findLHS(self, nums) -> int:
        ans = 0
        tracking = collections.defaultdict(int)
        for i in nums:
            tracking[i] += 1
        for i in sorted(tracking.keys()):
            if tracking[i+1] != 0:
                ans = max(ans,tracking[i]+tracking[i+1])
            if tracking[i-1] != 0:
                ans = max(ans,tracking[i]+tracking[i-1])
        return ans
"""
"""
#Third attempt: counter using actual counter #36%
import collections
class Solution:
    def findLHS(self, nums) -> int:
        ans = 0
        tracking = collections.Counter(nums)
        for i in tracking:
            if tracking[i+1] != 0:
                ans = max(ans,tracking[i]+tracking[i+1])
            if tracking[i-1] != 0:
                ans = max(ans,tracking[i]+tracking[i-1])
        return ans
"""
#Fourth attempt: counter using actual counter without counting twice #58% (100% was the same code)
import collections
class Solution:
    def findLHS(self, nums) -> int:
        ans = 0
        tracking = collections.Counter(nums)
        for i in tracking:
            if tracking[i+1] != 0:
                ans = max(ans,tracking[i]+tracking[i+1])
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.findLHS(input1)
        print(ans)
        return ans

    assert test([1,3,2,2,5,2,3,7]) == 5
    assert test([1,2,3,4]) == 2
    assert test([1,1,1,1]) == 0