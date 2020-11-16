"""
#97%
665. Non-decreasing Array
Easy

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.



Constraints:

    1 <= n <= 10 ^ 4
    - 10 ^ 5 <= nums[i] <= 10 ^ 5
"""

#Got this answer with some help from useful comments
#Was not able to get this logic on my own: return nums[skip-1] <= nums[skip+1] or nums[skip] <= nums[skip+2]
#You need to either skip the first point that is a problem or the element immidiately after that point (which is a contributor to the problem for being a high number)
class Solution:
    def checkPossibility(self, nums) -> bool:
        skip = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if skip == None:
                    skip = i
                else:
                    return False
        return skip is None or skip == 0 or skip == len(nums)-2 or nums[skip-1] <= nums[skip+1] or nums[skip] <= nums[skip+2]

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.checkPossibility(input1)
        print(ans)
        return ans

    assert test([4,2,3]) == True
    assert test([4,2,1]) == False
    assert test([1,2,3]) == True
    assert test([1, 3,2]) == True
    assert test([3,4,2,3]) == False
    assert test([5, 7, 1, 8]) == True
