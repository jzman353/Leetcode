'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

Runtime: 112 ms Beats 25%
Memory Usage: 16.1 MB
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #return 2*sum(set(nums))-sum(nums)
'''