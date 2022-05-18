"""
78. Subsets
Medium

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
#40%
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(1,len(nums)+1):
            ans.extend(list(itertools.combinations(nums,i)))
        return ans

"""
sample 18 ms submission
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(nums,subset):
            nonlocal ans
            ans.append(subset)
            for i,n in enumerate(nums):
                bt(nums[i+1:],subset+[n])
        bt(nums,[])
        return ans
"""