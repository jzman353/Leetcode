"""
2176. Count Equal and Divisible Pairs in an Array
Easy

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

Example 1:

Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 1
Output: 0
Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.

Constraints:

1 <= nums.length <= 100
1 <= nums[i], k <= 100
"""
#39%
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        answer = 0
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        for i in d.keys():
            if len(d[i]) > 1:
                for j in range(len(d[i])-1):
                    for m in range(j+1,len(d[i])):
                        if d[i][j]*d[i][m] % k == 0:
                            answer += 1
        return answer

"""
sample 56 ms submission
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        seen = defaultdict(lambda: defaultdict(int))
        pairs = 0
        
        for ix, num in enumerate(nums):
            div = math.gcd(k, ix)
            
            if num in seen:
                for jx in range(0, k, k // div):
                    pairs += seen[num][jx]
            
            seen[num][ix % k] += 1
            
        return pairs

This looks exactly like mine
sample 60 ms submission
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        cnt, d = 0, defaultdict(list)

        for i, n in enumerate(nums):

            d[n].append(i)

        for indices in d.values():    

            for i, a in enumerate(indices):

                for b in indices[: i]:

                    if a * b % k == 0:

                        cnt += 1

        return cnt
"""