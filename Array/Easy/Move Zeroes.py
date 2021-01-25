"""
283. Move Zeroes
Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""

#49%
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        remove = []
        for i in range(len(nums)):
            if nums[i] == 0:
                remove.append(i)
        for i in remove:
            del nums[i-count]
            count += 1
            nums.append(0)

"""
        Do not return anything, modify nums in-place instead.
        p=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                if (i!=p):
                    nums[p]=nums[i]
                    nums[i]=0 
                p+=1      
"""
