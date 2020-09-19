'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

Runtime: 168 ms Beats 87%
Memory Usage: 15.3 MB
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ruled_out=[]
        for i in nums:
            if i not in ruled_out:
                if nums.count(i)>len(nums)/2:
                    return i
                else:
                    ruled_out.append(i)

'''
Runtime: 148ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
'''