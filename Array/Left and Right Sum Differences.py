"""
2574. Left and Right Sum Differences
Easy

Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105
"""

#49%
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        right = [0]*len(nums)
        answer = [0]*len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1] + nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] + nums[i+1]
            answer[i] = abs(left[i]-right[i])
        answer[-1] = abs(left[-1]-right[-1])
        return answer

"""
Sample 58 ms submission
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ls= sum(nums)
        s=0
        t=0
        ans=[]
        for i in range(len(nums)):
            t=ls-s
            s=s+nums[i]
            ans.append(abs(t-s))
        
        return ans
"""

import random
def testCases():
    nums = random.choices(range(1,10**3),k=random.randint(1,1000))
    print(nums)

for i in range(8):
    testCases()