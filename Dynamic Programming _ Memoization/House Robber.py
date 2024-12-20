"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.



Constraints:

    0 <= nums.length <= 100
    0 <= nums[i] <= 400

"""

class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            dp.append(max(dp[i-1],dp[i-2]+nums[i]))
        return dp[-1]
"""
def rob(nums) -> int:
    # edge cases:
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums)

    # dynamic programming - decide each problem by its sub-problems:
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]
"""
"""def rob(nums) -> int:
    dp1, dp2 = 0, 0
    for num in nums:
        dp1, dp2 = dp2, max(dp1 + num, dp2)
    return dp2"""

#print(rob([1,2,3,1]))
#print(rob([2,7,9,3,1]))
print(rob([1,9,9,3,5,7,7,7,2,1,45,99,7,8,5,3,2,4,5,99]))