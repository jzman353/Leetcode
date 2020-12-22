"""
Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Constraints:

    0 <= nums.length <= 2000
    -106 <= nums[i] <= 106
"""
import bisect

class Solution:
    def findNumberOfLIS(self, nums) -> int:
        ans = [[nums[0]]]
        todo = []
        for i in range(1, len(nums)):
            if nums[i] > ans[-1][-1]:
                ans[-1].append(nums[i])
            elif nums[i] == ans[-1][-1]:
                ans.append(ans[-1])
            else:
                x = bisect.bisect_left(ans[-1], i)
                todo.append(ans[-1][:x + 1])
                #todo[-1].append(nums[i])
                todo[-1].append(i)
        while todo:
            ind = todo[-1].pop()
            for i in range(ind+1, len(nums)):
                ans.append(todo.pop())
                if nums[i] >= ans[-1][-1]:
                    ans[-1].append(nums[i])
                elif nums[i] == ans[-1][-1]:
                    ans.append(ans[-1])
                else:
                    x = bisect.bisect_left(ans[-1], i)
                    todo.append(ans[-1][:x + 1])
                    #todo[-1].append(nums[i])
                    todo[-1].append(i)
        print(ans)
        return len(ans)

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.findNumberOfLIS(input1)
        print(ans)
        return ans

    assert test([1,3,5,4,7]) == 2
    assert test([2,2,2,2,2]) == 5
    assert test([1, 2, 4, 3, 5, 4, 7, 2]) == 5
