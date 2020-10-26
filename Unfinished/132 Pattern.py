"""
456. 132 Pattern
Medium

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?



Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].



Constraints:

    n == nums.length
    1 <= n <= 104
    -109 <= nums[i] <= 109
"""

class Solution:
    def find132pattern(self, nums) -> bool:
        if len(nums)<3:
            return False
        minn = [nums[0]]
        for i in range(1, len(nums)):
            minn.append(min(minn[i - 1], nums[i]))
        for j in range(len(nums)):
            if nums[j] > minn[i]:
                k = j + 1
                while (k < len(nums)) and ((nums[k] <= minn[j]) or (nums[k] > nums[j])):
                    k += 1
                if k < len(nums) and nums[k] < nums[j]:
                    return True
        return False

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.find132pattern(input1)
        print(ans)
        return ans

    assert test([1,2,3,4]) == False
    assert test([3,1,4,2]) == True
    assert test([-1,3,2,0]) == True
    assert test([1, 0, 1, -4, -3]) == False
    assert test([1]) == False
    assert test([]) == False
    assert test([1, 0]) == False
    assert test([1, 0, 1]) == False