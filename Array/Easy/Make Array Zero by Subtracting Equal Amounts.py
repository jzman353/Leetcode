"""
2357. Make Array Zero by Subtracting Equal Amounts
Easy

You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

Example 1:

Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

#81%
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = set(nums)
        ans.remove(0)
        return len(ans) if ans else 0

"""
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})
"""

"""
import random
def test_cases():
    for i in range(8):
        test = []
        for j in range(random.randint(1,100)):
            test.append(random.randint(0,100))
        print(test)

test_cases()
"""