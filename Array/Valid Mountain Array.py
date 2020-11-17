"""
#34%
941. Valid Mountain Array
Easy

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < A[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true



Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 104
"""

class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) < 3:
            return False

        up = True
        curr = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1] and up and curr == 0:
                curr = 1
            elif arr[i] < arr[i + 1] and up:
                continue
            elif arr[i] > arr[i + 1] and not up:
                continue
            elif arr[i] > arr[i + 1] and up and curr > 0:
                up = False
            else:
                return False
        return not up
"""
class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) < 3:
            return False

        up = True
        curr = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1] and up and curr == 0:
                curr = 1
            elif arr[i] < arr[i + 1] and up:
                continue
            elif arr[i] > arr[i + 1] and not up:
                continue
            elif arr[i] > arr[i + 1] and up and curr > 0:
                up = False
            elif arr[i] > arr[i + 1] and up and curr == 0:
                return False
            elif arr[i] < arr[i + 1] and not up:
                return False
            elif arr[i] == arr[i + 1]:
                return False
        return not up
"""
"""    
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
        
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3: return False
        inc = A[0] < A[1]
        k = 0
        for i in range(1, n):
            if inc and A[i-1] >= A[i]: 
                k += 1
                inc = False
            if not inc and A[i-1] <= A[i]:
                return False
        return k == 1
"""