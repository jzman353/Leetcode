"""
2455. Average Value of Even Numbers That Are Divisible by Three
Easy

Companies
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
Example 2:

Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""
#100%
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        summ = 0
        count = 0
        for i in nums:
            if i % 6 == 0:
                summ += i
                count += 1
        try:
            return summ//count
        except:
            return 0

"""
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        task_list = [i for i in nums if not i % 3 and not i % 2]
        if not len(task_list):
            return 0
        return int(sum(task_list) / len(task_list))
"""

import random
def test_cases():
    print(random.choices(range(1,1001),k=random.randint(1,1000)))

for i in range(8):
    test_cases()