#61%
"""
Maximum Width Ramp (Medium)
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.



Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.

Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation:
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.



Note:

    2 <= A.length <= 50000
    0 <= A[i] <= 50000
"""

import timeit
class Solution:
    def maxWidthRamp(self, A) -> int:
        if not A:
            return 0
        length = len(A)
        sorted_A = sorted(range(length), key=lambda k: A[k])
        maxx = 0
        minval = sorted_A[0]
        for i in range(1, length):
            minval = min(minval, sorted_A[i])
            maxx = max(maxx, sorted_A[i] - minval)
        return maxx

"""
#Optimized brute force: 96/98
class Solution:
    def maxWidthRamp(self, A) -> int:
        length = len(A)
        left = 0
        right = length - 1
        maxx = 0
        while left < right:
            while left < right:
                if A[left] <= A[right]:
                    maxx = max(maxx, right - left)
                right -= 1
                if right <= maxx:
                    break
            right = length - 1
            left += 1
            if maxx >= right-left:
                break
        return maxx
"""

if __name__ == '__main__':
    def test(input):
        Test = Solution()
        ans = Test.maxWidthRamp(input)
        print(ans)

    A = [6,0,8,2,1,5]  #1 4
    test(A)
    A = [9,8,1,0,1,9,4,0,4,1]  # 2 7
    test(A)
    A = [7,1,5,3,6,4]  #Made up 4
    test(A)
    A = [7, 6, 4, 3, 1] #Made up 0
    test(A)
    A = [30, 77, 2, 4, 3, 1]  # Made up 2
    test(A)
    A = []  # Made up 0
    test(A)


    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))