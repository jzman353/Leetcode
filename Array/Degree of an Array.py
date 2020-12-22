"""
697. Degree of an Array
Easy

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:

    nums.length will be between 1 and 50,000.
    nums[i] will be an integer between 0 and 49,999.
"""
#17%
import math
import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        x = c.most_common()
        # print(x)

        maxx = x[0][1]
        values = []
        for i in x:
            if i[1] == maxx:
                values.append(i[0])
            else:
                break
        # print(values)

        diff = {}
        for i in values:
            diff[i] = len(nums) - nums[::-1].index(i) - 1 - nums.index(i)
        # print(diff)

        minn = math.inf
        ans = 0
        for i in diff.keys():
            minn = min(diff[i], minn)
        return minn + 1

"""
Below is a genius solution. He appends the index of all locations and then sorts the result by length. O(2n)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        vi = {}
        for i,n in enumerate(nums):
            if n in vi:
                vi[n].append(i)
            else:
                vi[n] = [i]
        lst = sorted(vi.values(), key=len, reverse=True)
        minlen = math.inf
        degree = len(lst[0])
        for sublst in lst:
            if len(sublst) != degree:
                break
            minlen = min(sublst[-1]-sublst[0]+1, minlen)
        return minlen
"""