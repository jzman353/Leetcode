"""
67%
832. Flipping an Image
Easy

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Notes:

    1 <= A.length = A[0].length <= 20
    0 <= A[i][j] <= 1

Accepted
186,483
Submissions
243,436
"""


class Solution:
    def flipAndInvertImage(self,A):
        import math
        length = len(A)
        for i in range(length):
            for j in range(math.ceil(length/2)):
                temp = 1-A[i][j]
                A[i][j] = 1-A[i][length-1-j]
                A[i][length - 1 - j] = temp
        return A

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.flipAndInvertImage(input1)
        print(ans)
        return ans


    input1 = [[1,1,0],[1,0,1],[0,0,0]]
    assert test(input1) == [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

    input1 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    assert test(input1) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]