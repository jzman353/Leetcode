"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1



Note:

    You may assume that all elements in nums are unique.
    n will be in the range [1, 10000].
    The value of each element in nums will be in the range [-9999, 9999].
"""

class Solution:
    def search(self, nums, target: int) -> int:
        if nums[0] == target:
            return 0
        maxx = len(nums) - 1
        if nums[-1] == target:
            return maxx
        minn = 0
        mid = (maxx+minn)//2
        while maxx != mid and minn != mid:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                minn = mid
            else:
                maxx = mid
            mid = (maxx+minn)//2
        return -1


if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.search(input1, input2)
        print(ans)


    input1 = [-1, 0, 3, 5, 9, 12]
    input2 = 9
    test(input1, input2)  # 4

    input1 = [-1, 0, 3, 9, 12]
    input2 = 9
    test(input1, input2)  # 3

    input1 = [-1, 0, 9, 12]
    input2 = 9
    test(input1, input2)  # 2
