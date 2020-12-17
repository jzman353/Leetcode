"""
1287. Element Appearing More Than 25% In Sorted Array
Easy

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6



Constraints:

    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^5

"""
#41%
class Solution:
    def findSpecialInteger(self, arr) -> int:
        d = collections.defaultdict(int)
        target = len(arr)/4
        for i in arr:
            d[i] += 1
            if d[i] > target:
                return i

#19%
import collections
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = collections.Counter(arr)
        return c.most_common(1)[0][0]

"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        def findIndexOfFirst(x):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        for q in range(1, 4):
            idx = int(q * len(arr) / 4)
            start = findIndexOfFirst(arr[idx])
            if arr[start] == arr[start + int(len(arr)/4)]:  #  check the length is at least 25%
                return arr[start]
"""