"""
2395. Find Subarrays With Equal Sum
Easy

Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.

Return true if these subarrays exist, and false otherwise.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [4,2,4]
Output: true
Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.
Example 2:

Input: nums = [1,2,3,4,5]
Output: false
Explanation: No two subarrays of size 2 have the same sum.
Example 3:

Input: nums = [0,0,0]
Output: true
Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0.
Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.

Constraints:

2 <= nums.length <= 1000
-109 <= nums[i] <= 109
"""
#87%
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        new = []

        for i in range(len(nums)-1):
            new.append(nums[i]+nums[i+1])

        d = defaultdict(int)
        for i in new:
            if d[i] == 1:
                return True
            else:
                d[i] += 1
"""
Sample 18 ms submission
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n_set = set()
        for i in range(1, len(nums)):
            n = nums[i-1]+nums[i]
            if n in n_set:
                return True
            else:
                n_set.add(n)
        return False

6%
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[i] + nums[i+1] == nums[j]+nums[j+1]:
                    return True
"""

import random
def test_cases():
    print(random.choices(range(-10**9,10**9),k=random.randint(2,1000)))

for i in range(8):
    test_cases()