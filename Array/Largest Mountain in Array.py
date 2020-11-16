"""
Longest Mountain in Array

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000

Follow up:

    Can you solve it using only one pass?
    Can you solve it in O(1) space?
"""

class Solution:
    def longestMountain(self, A) -> int:
        up = True
        ans = 1
        curr = 0
        for i in range(len(A)-1):
            if A[i]<A[i+1] and up:
                curr += 1
            elif A[i]>A[i+1] and up and curr >= 1:
                curr += 1
                up = False
                ans = max(ans, curr)
            elif A[i]>A[i+1] and not up:
                curr += 1
                ans = max(ans, curr)
            elif (A[i]<A[i+1] and not up):
                curr = 1
                up = True
            elif A[i]==A[i+1]:
                curr = 0
                up = True
        if ans > 1:
            return ans+1
        else:
            return 0




if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.longestMountain(input1)
        print(ans)
        return ans

    assert test([2,1,4,7,3,2,5]) == 5
    assert test([2,2,2]) == 0
    assert test([5, 4, 3,2,1]) == 0
    assert test([1,2,3,4,5]) == 0
    assert test([1, 2, 3, 4, 5,4]) == 6
    assert test([1, 2, 1]) == 3
    assert test([1, 2, 3, 1]) == 4
    assert test([1, 3, 2, 1]) == 4
    assert test([2, 3, 3, 2, 0, 2]) == 0
    assert test([875,884,239,731,723,685]) == 4