"""
18. 4Sum
Medium

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

#5%
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for i in d.keys():
            if d[i] > 4:
                for j in range(d[i] - 4):
                    nums.remove(i)

        self.answer = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if target - nums[i] - nums[j] - nums[k] in nums:
                        idx_m = [m for m in range(len(nums)) if nums[m] == target - nums[i] - nums[j] - nums[k]]
                        if i in idx_m:
                            idx_m.remove(i)
                        if j in idx_m:
                            idx_m.remove(j)
                        if k in idx_m:
                            idx_m.remove(k)
                        if idx_m and sorted([nums[i], nums[j], nums[k], nums[idx_m[0]]]) not in self.answer:
                            self.answer.append(sorted([nums[i], nums[j], nums[k], nums[idx_m[0]]]))
        return self.answer

"""
sample 61 ms submission
from itertools import combinations
from collections import defaultdict, Counter

class Solution(object):


    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        half_target = target // 2
        counter = Counter(nums)
        uniques = sorted(counter)
        x_min, x_max = target - 3 * uniques[-1], target - 3 * uniques[0]
        uniques = [ x for x in uniques if x_min <= x <= x_max]
        uniques = sorted(uniques + [x for x in uniques if counter[x] > 1])

        target_minus_sums = set(target - (x + y) for x, y in combinations(uniques, 2))

        ab_sum_pairs, cd_sum_pairs = defaultdict(set), defaultdict(set)
        for (x, y) in combinations(uniques, 2):
            s = x + y
            if s in target_minus_sums:
                if s <= half_target:
                    ab_sum_pairs[s].add((x, y))
                if s >= half_target:
                    cd_sum_pairs[s].add((x, y))
                    
        return {
            (a, b, c, d) for ab in ab_sum_pairs
                for (a, b) in ab_sum_pairs[ab]
                    for (c, d) in cd_sum_pairs[target - ab]
                        if b < c or b == c and [a, b, c, d].count(b) <= counter[b]
        }
"""