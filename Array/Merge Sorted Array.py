"""
88. Merge Sorted Array
Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Constraints:

    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1.length == m + n
    nums2.length == n
"""
#88%
import bisect
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1)-1
        while i >= m:
            nums1.pop()
            i -= 1
        for i in nums2:
            bisect.insort(nums1, i)

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums1)==0:
            return nums2
        elif len(nums2)==0:
            return nums1
        
        res = []
        end = 0
    
        for i in range(m):
            res.append(nums1[i])
        
        for i in range(len(nums2)):
            res.append(nums2[i])
            
        
        res.sort()
        for i in range(len(nums1)):
            nums1[i] = res[i]
"""