"""
72%
Summary Ranges

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b



Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Example 3:

Input: nums = []
Output: []

Example 4:

Input: nums = [-1]
Output: ["-1"]

Example 5:

Input: nums = [0]
Output: ["0"]



Constraints:

    0 <= nums.length <= 20
    -231 <= nums[i] <= 231 - 1
    All the values of nums are unique.
"""


class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        minn = nums[0]
        ans = []
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                if minn != nums[i]:
                    ans.append(str(minn)+"->"+str(nums[i]))
                else:
                    ans.append(str(minn))
                minn = nums[i+1]
        if minn != nums[-1]:
            ans.append(str(minn) + "->" + str(nums[-1]))
        else:
            ans.append(str(minn))
        return ans


if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.summaryRanges(input1)
        print(ans)
        return ans

    assert test([0,1,2,4,5,7]) == ["0->2","4->5","7"]
    assert test([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
    assert test([]) == []
    assert test([-1]) == ["-1"]
    assert test([0]) == ["0"]
