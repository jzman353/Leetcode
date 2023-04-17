"""
2367. Number of Arithmetic Triplets
Easy
830
39
Companies
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

Example 1:

Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.
Example 2:

Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

Constraints:
3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums is strictly increasing.
"""

#100%
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        length = len(nums)
        answer = 0
        for i in range(length-2):
            for j in range(i+1, length-1):
                if nums[j] - nums[i] < diff:
                    continue
                for k in range(j+1, length):
                    if nums[k] - nums[j] < diff:
                        continue
                    if nums[k]-nums[j] == nums[j]-nums[i] == diff:
                        #print(i,j,k,nums[i],nums[j],nums[k])
                        answer += 1
                    elif nums[k]-nums[j] > diff:
                        break
                if nums[j]-nums[i] > diff:
                    break
        return answer

import random
def test_cases():
    nums = []
    length = random.randint(3, 200)
    for i in range(length):
        if not nums:
            start = 0
        else:
            start = nums[-1]+1
        nums.append(random.randint(start,200-length+i))
    diff = random.randint(1,50)
    print(nums)
    print(diff)

for i in range(8):
    test_cases()

"""
Sample 50 ms submission
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        dicu = {}
        res = 0
        
        for i,e in enumerate(nums):
            dicu[e] = i+1
        
        for e in nums :
            if dicu.get(e-diff) and dicu.get(e+diff):
                res += 1
        return res
"""