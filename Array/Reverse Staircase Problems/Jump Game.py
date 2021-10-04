"""
55. Jump Game
Medium

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
#36%
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #The whitelist will contain the last index to start and then every index that can reach the last index will be added.
        white_list = [len(nums)-1]
        #This is a quick check to skip logic when unnecessary
        if len(nums)>1 and nums[0] == 0:
            return False
        #We will iterate backwards from len(nums)-2 to 0
        for i in range(2,len(nums)+1):
            #print(i,j,nums[-i],len(nums)-i+j,len(nums)-i,white_list)
            for j in range(len(white_list)-1,-1,-1):
                #check if a number already in the whitelist is in the range allowed by the current index
                if len(nums)-i< white_list[j] <=len(nums)-i+nums[-i]:
                    white_list.append(len(nums)-i)
                    break
        #print(white_list)
        return 0 in white_list

"""
sample 436 ms submission
def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        elif len(nums)==2:
            return nums[0]>=1
        
        lastPos = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if (i + nums[i]) >= lastPos:
                lastPos = i
        return lastPos == 0
"""