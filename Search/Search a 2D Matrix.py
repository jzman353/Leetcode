"""
99%
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.



Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false

Example 3:

Input: matrix = [], target = 0
Output: false



Constraints:

    m == matrix.length
    n == matrix[i].length
    0 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""
import bisect
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row_length = len(matrix)
        col_length = len(matrix[0])
        if target < matrix[0][0]:
            return False
        if target > matrix[row_length-1][col_length-1]:
            return False
        i = 0
        while i < row_length and target >= matrix[i][0]:
            i += 1
        x = bisect.bisect_left(matrix[i-1],target)
        return x<col_length and target == matrix[i-1][x]

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.searchMatrix(input1,input2)
        print(ans)
        return ans

    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13) == False
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 1) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 5) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 50) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 34) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 30) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 23) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 10) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 20) == True
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 60) == False
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 22) == False
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 8) == False
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 4) == False
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 0) == False
    assert test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], -1) == False
    assert test([[]], -1) == False
    assert test([], -1) == False

"""
binary search

class Solution:
    def searchMatrix(self, ma: List[List[int]], target: int) -> bool:
        if len(ma)>0:
            n=len(ma)
            m=len(ma[0])

            low=0
            high=n*m-1
            while low<=high:
                mid=low+(high-low)//2
                if ma[mid//m][mid%m]==target:
                    return True
                elif ma[mid//m][mid%m]>target:
                    high=mid-1
                elif ma[mid//m][mid%m]<target:
                    low=mid+1
            else:
                return False
        else:
            return False

"""