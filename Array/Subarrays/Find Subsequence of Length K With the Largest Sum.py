"""
2099. Find Subsequence of Length K With the Largest Sum
Easy

You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation:
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7.
Another possible subsequence is [4, 3].

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
"""
#74%
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        l = []
        for i in nums:
            if len(l) < k:
                l.append(i)
            else:
                m = min(l)
                if i > m:
                    l.remove(m)
                    l.append(i)
        return l

"""
sample 40 ms submission
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        a = []
        d = {}
        h = []
        heapq.heapify(h)
        
        for i in nums:
            heapq.heappush(h, -i)
        
        while k > 0:
            v = heapq.heappop(h)
            
            if v > 0:
                if -v in d:
                    d[-v] += 1
                else:
                    d[-v] = 1
            else:
                if abs(v) in d:
                    d[abs(v)] += 1
                else:
                    d[abs(v)] = 1
            k -= 1
        
        for i in nums:
            if i in d and d[i] > 0:
                a.append(i)
                d[i] -= 1
            
        return a
        
sample 44 ms submission
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = list(enumerate(nums))
        arr.sort(key = lambda x: x[1])
        idx = [i for i, j in arr[-k:]]
        idx.sort()
        return [nums[i] for i in idx]
"""