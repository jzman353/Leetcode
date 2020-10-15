"""
90%
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000



Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

Accepted
766,141
Submissions
2,540,905
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        import math
        def median(n):
            if len(n)%2 != 0:
                return n[len(n)//2]
            else:
                return (n[len(n)//2-1]+n[(len(n)//2)])/2
        m = len(nums1)
        n = len(nums2)
        stop1 = stop2 = False
        if not nums1:
            return median(nums2)
        if not nums2:
            return median(nums1)
        mid = (m+n)/2
        left = right = 0
        ans = -math.inf
        for i in range(m+n):
            if (not stop2 and nums1[left] > nums2[right]) or stop1:
                ans = max(ans, nums2[right])
                right += 1
                if right == n:
                    stop2 = True
                    right -= 1
            elif not stop1:
                ans = max(ans, nums1[left])
                left += 1
                if left == m:
                    stop1 = True
                    left -= 1
            if i == math.floor(mid) and (m+n)%2 != 0: # Odd
                return ans
            elif float(i) == mid-1 and (m+n)%2 == 0: # even
                if not stop1 and not stop2:
                    if nums1[left] < nums2[right]:
                        ans2 = nums1[left]
                    else:
                        ans2 = nums2[right]
                else:
                    if nums1[left] > nums2[right]:
                        ans2 = nums1[left]
                    else:
                        ans2 = nums2[right]
                return (ans+ans2)/2


if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.findMedianSortedArrays(input1,input2)
        print(ans)
        return ans

    assert test([1,3], [2]) == 2
    assert test([1, 2], [3,4]) == 2.5
    assert test([0,0], [0,0]) == 0
    assert test([], [1]) == 1
    assert test([2], []) == 2
    assert test([1, 2], [3, 4,5]) == 3
    assert test([1, 2,3,4,5], []) == 3
    assert test([1, 2, 3, 4], []) == 2.5
    assert test([1,3], [2,7]) == 2.5
    assert test([100000], [100001]) == 100000.5
    assert test([1], [2,3,4,5,6]) == 3.5

"""
#Also 90% but much more intuitive
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1
        c.extend(nums2)
        c = sorted(c)

        if len(c) == 1:
            return c[0]

        if len(c) % 2 == 0:
            val_ind = int(len(c) / 2)

            median = (c[val_ind - 1] + c[val_ind]) / 2

        else:
            median = c[int(len(c) / 2)]

        return median
"""

