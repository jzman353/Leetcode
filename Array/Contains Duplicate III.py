#Solved brute force but not enough

'''
Given an array of integers, find out whether there are two distinct indices i and j
in the array such that the absolute difference between nums[i] and nums[j] is
at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false



Constraints:

    0 <= nums.length <= 2 * 104
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 104
    0 <= t <= 231 - 1

Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked.
When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary
to sort next overlapping set of k numbers again.
'''

#better than N^2 solution
def containsNearbyAlmostDuplicate(nums, k: int, t: int) -> bool:
    for count1, i in enumerate(nums):
        if k==0:
            return False
        if count1 < len(nums)-1:
            if count1+k < len(nums)-1:
                k_list = nums[count1:count1+1+k]
            else:
                k_list = nums[count1:]
            k_list.sort()
            i_index = k_list.index(i)
            if i_index == 0:
                if abs(i - k_list[i_index+1]) <= t:
                    return True
            elif i_index == len(k_list)-1:
                if abs(i - k_list[i_index-1]) <= t:
                    return True
            else:
                if abs(i - k_list[i_index+1]) <= t or abs(i - k_list[i_index-1]) <= t:
                    return True
    return False
'''
#N^2 solution
def containsNearbyAlmostDuplicate(nums, k: int, t: int) -> bool:
    for count1, i in enumerate(nums):
        if count1 < len(nums)-1:
            for count2,j in enumerate(nums[count1+1:count1+1+k]):
                if abs(i-j) > t:
                    continue
                return True
    return False
'''
print(containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)) #True
print(containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)) #True
print(containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)) #False
print(containsNearbyAlmostDuplicate([8,7,15,1,6,1,9,15],1,3)) #True 51/53 #51 / 53 test cases passed.- Time Limit Exceeded
print(containsNearbyAlmostDuplicate([-3,3,-6],2,3))#True 19/53
print(containsNearbyAlmostDuplicate([1,2,2,3,1],3,0))#True 20/53
print(containsNearbyAlmostDuplicate([1,2],0,1))#False 21/53

'''
from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])   
            pos1 = SortedList.bisect_left(SList, nums[i] - t)
            pos2 = SortedList.bisect_right(SList, nums[i] + t)
            
            if pos1 != pos2 and pos1 != len(SList): return True
            
            SList.add(nums[i])
        
        return False
'''