"""
350. Intersection of Two Arrays II
Easy

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

class Solution:
    def intersect(self, nums1, nums2):
        import collections
        c = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        c = c&c2
        return list(c.elements())

"""
nums1 = sorted(nums1)
nums2 = sorted(nums2)

ptr1 = 0
ptr2 = 0
intersection = []
while ptr1 < len(nums1) and ptr2 < len(nums2):
    if nums1[ptr1] == nums2[ptr2]:
        intersection.append(nums1[ptr1])
        ptr1 += 1
        ptr2 += 1
    elif nums1[ptr1] < nums2[ptr2]:
        ptr1 += 1
    else:
        ptr2 += 1

return intersection
"""