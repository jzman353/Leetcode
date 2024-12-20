"""
75. Sort Colors
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

"""
sample 8 ms submission
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = [0 for _ in range(3)]
        for i in nums:
            freq[i] += 1
        count = 0
        for k in range(len(freq)):
            v = freq[k]
            for i in range(count, count+v):
                nums[i] = k
            count += v

sample 12 ms submission
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr = [0, 0, 0]
        
        for num in nums:
            arr[num] += 1
        
        nums[:arr[0]] = [0] * arr[0]
        nums[arr[0]:arr[0] + arr[1]] = [1] * arr[1]
        nums[arr[0] + arr[1]:] = [2] * arr[2]
"""