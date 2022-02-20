"""
31. Next Permutation
Medium

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
#80%
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                s = sorted(nums[i-1:])
                nextt = bisect.bisect_right(s, nums[i-1])
                nums[::] = nums[:i-1]+[s[nextt]]+s[:nextt]+s[nextt+1:]
                return
        else:
            nums[::]=nums[::-1]

"""
sample 20 ms submission
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:  
        def findNextNum(arr,leng,i):
            j=leng-1
            while j>i:
                if arr[j]>arr[i]:
                    return j
                j-=1
        
        le=len(nums)        
        i=le-2        
        
        #find first decreasing number
        while i>=0: 
            if nums[i]<nums[i+1]:
                break
            i-=1
        
        #no next perm
        if i==-1:
            nums[::]=nums[::-1]
            return      
        
            
        #swap with next higher element to the right
        nxt=findNextNum(nums,le,i)
        nums[i],nums[nxt]=nums[nxt],nums[i]
        #print(nums)
    
        #reverse [i+1:]
        nums[::] = nums[:i+1]+sorted(nums[i+1:])
"""