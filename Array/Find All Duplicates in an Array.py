"""
442. Find All Duplicates in an Array
Medium

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""
#10%
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [i for i in c if c[i]==2]

"""
sample 312 ms submission
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict = collections.defaultdict()
        res = []
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                res.append(num)
        return res
"""