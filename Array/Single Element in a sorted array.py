'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

Runtime: 108 ms Beats 6%
Memory Usage: 16 MB
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            if i==len(nums)-1:
                return nums[i]
            elif nums[i] == nums[i+1]:
                i+=2
            else:
                return nums[i]

'''
Runtime: 60 ms

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # ans = nums[0]
        # for i in range(1, len(nums)):
        #     ans ^= nums[i]
        # return ans
        if len(nums) < 2:
            return nums[0]
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left+right)//2    
            if nums[mid] == nums[mid+1]:
                if mid%2 == 0:
                    left = mid
                else:
                    right = mid
            else:
                if mid%2 != 0:
                    left = mid 
                else:
                    right = mid
        
        if left-1 >= 0:
            if nums[left-1] != nums[left]:
                return nums[left]
            return nums[right]
        if right+1 < len(nums):
            if nums[right] != nums[right+1]:
                return nums[right]
            return nums[left]
'''