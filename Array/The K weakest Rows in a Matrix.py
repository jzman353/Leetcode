"""
1337. The K Weakest Rows in a Matrix
Easy

Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.



Example 1:

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers for each row is:
row 0 -> 2
row 1 -> 4
row 2 -> 1
row 3 -> 2
row 4 -> 5
Rows ordered from the weakest to the strongest are [2,0,3,1,4]

Example 2:

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers for each row is:
row 0 -> 1
row 1 -> 4
row 2 -> 1
row 3 -> 1
Rows ordered from the weakest to the strongest are [0,2,3,1]



Constraints:

    m == mat.length
    n == mat[i].length
    2 <= n, m <= 100
    1 <= k <= m
    matrix[i][j] is either 0 or 1.
"""
#97%
import collections
class Solution:
    def kWeakestRows(self, mat, k: int):
        d = collections.defaultdict(list)
        for i in range(len(mat)):
            #if len(d[0]) > k: #These two lines could potentially save you from a case where k is small and some rows have only 0s
            #   break
            count = 0
            for j in mat[i]:
                if j == 1:
                    count += 1
                else:
                    break
            d[count].append(i)
        ans = []
        for key in sorted(d):
            ans.extend(d[key])
            if len(ans)>k:
                return ans[:k]
            if len(ans)==k:
                return ans

        """
        pair = []
        for i in range(len(mat)):
            pair.append((i, mat[i].count(1)))
        pair = sorted(pair, key=lambda x:x[1])
        return [x[0] for x in pair[:k]]
        """


if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.kWeakestRows(input1, input2)
        print(ans)
        return ans

    assert test([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3) == [2,0,3]
    assert test([[1, 0, 0, 0],[1, 1, 1, 1],[1, 0, 0, 0],[1, 0, 0, 0]],2) == [0,2]
    assert test([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]], 1) == [0]