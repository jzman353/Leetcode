"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
#TLE
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        intervals = []
        for i in nums:
            idx = 0
            for j in range(len(intervals)):
                if i == intervals[j][0]:
                    idx = -2
                    intervals[j][0] -= 1
                    if j-1 >= 0 and intervals[j-1][1] == i:
                        intervals[j][0] = intervals[j-1][0]
                        del intervals[j-1]
                    break
                elif i == intervals[j][1]:
                    idx = -2
                    intervals[j][1] += 1
                    if j+1 < len(intervals) and intervals[j+1][0] == i:
                        intervals[j][1] = intervals[j+1][1]
                        del intervals[j+1]
                    break
                elif i > intervals[j][0] and i < intervals[j][1]:
                    idx = -2
                    break
                elif i < intervals[j][0]:
                    idx = j
                    break
            else:
                idx = -1
            if idx == -1:
                intervals.append([i-1,i+1])
            elif idx == -2:
                pass
            else:
                intervals.insert(idx,[i-1,i+1])
        return max(i[1]-i[0]-1 for i in intervals)