"""
99%
189. Rotate Array
Easy

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]



Constraints:

    1 <= nums.length <= 2 * 10^4
    It's guaranteed that nums[i] fits in a 32 bit-signed integer.
    k >= 0

Accepted
555.2K
Submissions
1.6M
"""

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1st attempt: rotate it one cell to the right for each k (Time limit exceeded)
        """
        length = len(nums)
        if length == 1:
            return nums
        count = 0
        while count < k % length:
            temp = nums[length-1]
            for i in range(length-2,-1,-1):
                nums[i+1] = nums[i]
            nums[0] = temp
            count += 1
        """
        #next try: only rotate one time
        length = len(nums)
        if length == 1:
            return nums
        k = k % length
        temp = nums[length-k:]
        nums[k:] = nums[:length-k]
        nums[:k] = temp