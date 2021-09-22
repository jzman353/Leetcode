"""
2006. Count Number of Pairs With Absolute Difference K
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.


Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
Example 2:

Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.
Example 3:

Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
1 <= k <= 99
"""
import collections
class Solution:
    def countKDifference(self, nums, k: int) -> int:
        d = collections.Counter()
        ans = 0
        for i in nums:
            d[i] += 1
            if i+k in d.keys():
                ans += d[i+k]
            if i-k in d.keys():
                ans += d[i-k]
        return ans

"""
class Solution:
    def countKDifference(self, a: List[int], k: int) -> int:
        a.sort()
        c=Counter()
        z=0
        for i,x in enumerate(a):
            z+=c[x-k]
            c[x]+=1
        return z

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums = collections.Counter(nums)
        
        keys = sorted(nums.keys())
        
        res = 0
        for key in keys:
            val0 = nums[key]
            val1 = nums.get(key+k, 0)
            res += val0*val1
        return res
"""