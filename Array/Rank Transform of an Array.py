"""
48%
1331. Rank Transform of an Array
Easy

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

    Rank is an integer starting from 1.
    The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
    Rank should be as small as possible.



Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.

Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]



Constraints:

    0 <= arr.length <= 105
    -109 <= arr[i] <= 109

Hint1: Use a temporary array to copy the array and sort it.
The rank of each element is the number of elements smaller than it in the sorted array plus one.
"""

import collections
class Solution:
    def arrayRankTransform(self, arr):
        arr_set = list(set(arr))

        sorted_Arr = sorted(range(len(arr_set)), key=lambda k: arr_set[k])

        d = collections.defaultdict(int)
        ans = []

        for count, val in enumerate(sorted_Arr):
            d[arr_set[val]] = count + 1

        for i in range(len(arr)):
            ans.append(d[arr[i]])
        return ans

"""
class Solution:
    def arrayRankTransform(self, arr):
        rank = {ele: i + 1 for i, ele in enumerate(sorted(set(arr)))}
        return list(map(rank.get, arr))
"""