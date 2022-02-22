"""
45. Jump Game II
Medium

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""
#12.4%
class Solution:
    def jump(self, nums: List[int]) -> int:
        self.seen = {len(nums)-1:0}
        for i in range(len(nums)-2,-1,-1):
            if len(nums)-1-i <= nums[i]:
                self.seen[i] = 1
            else:
                self.seen[i] = math.inf
                for j in range(i+nums[i],i,-1):
                    if j in self.seen:
                        self.seen[i] = min(self.seen[i],self.seen[j]+1)
        return self.seen[0]
"""
#TLE
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        self.min = math.inf
        def helper(steps, curr):
            if len(nums)-1-curr <= nums[curr]:
                self.min = min(self.min,steps)
            else:
                for i in range(nums[curr],0,-1):
                    if curr+i<len(nums)-1:
                        helper(steps+1, curr+i)
                    else:
                        break
        helper(1, 0)
        return self.min
"""

"""
sample 112 ms submission
class Solution:
    def jump(self, nums: List[int]) -> int:
        times = 0
        l=r=0
        
        while(r<len(nums)-1):
            times+=1
            farthest = max(i+nums[i] for i in range(l,r+1))
            l,r = r+1,farthest
        return times
"""