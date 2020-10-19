"""
85%
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.



Example 1:

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.



Constraints:

    2 <= A.length == B.length <= 2 * 104
    1 <= A[i], B[i] <= 6
"""

import collections
class Solution:
    def minDominoRotations(self, A, B) -> int:
        a = collections.Counter(A)
        b = collections.Counter(B)
        a1 = a.most_common(1)[0][0]
        b1 = b.most_common(1)[0][0]
        rotations1 = 0
        rotations2 = 0
        count1 = 0
        count2 = 0
        for i in range(len(A)):
            if A[i] != a1:
                if B[i] == a1:
                    rotations1 += 1
                else:
                    rotations1 = False
                    break
            else:
                count1 += 1
        if count1 == len(A):
            return 0

        for i in range(len(B)):
            if B[i] != b1:
                if A[i] == b1:
                    rotations2 += 1
                else:
                    rotations2 = False
                    break
            else:
                count1 += 1
        if count2 == len(B):
            return 0
        if rotations1 and rotations2:
            return min(rotations1,rotations2)
        elif rotations1:
            return rotations1
        elif rotations2:
            return rotations2
        else:
            return -1

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.minDominoRotations(input1,input2)
        print(ans)
        return ans

    assert test([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]) == 2
    assert test([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]) == -1
    assert test([2, 2, 2, 2, 2, 2], [5, 2, 6, 2, 3, 2]) == 0

    """
    

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        possible_sol = {A[0],B[0]}
        
        for i in possible_sol:
            A_swap = 0
            B_swap = 0
            flag = 0
            for j in range(len(A)):
                if A[j] == B[j] == i:
                    pass
                elif A[j] == i:
                    B_swap += 1
                elif B[j] == i:
                    A_swap += 1
                else:
                    flag = 1
                    break
                    
            if flag == 0:
                return min(A_swap,B_swap)
        return -1
    """