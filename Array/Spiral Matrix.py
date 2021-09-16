"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix):
        length = len(matrix)
        ans = []
        row = 0
        col = 1
        while length > 0:
            for i in range(length):
                ans.append(matrix[row][i])
            length -= 1
            for i in range(length):
                ans.append(matrix[i][-col])

        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.spiralOrder(input1)
        print(ans)
        return ans

    assert test([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert test([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]

"""
64%

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 1
        bot = len(matrix)
        left = 0
        right = len(matrix[0])
        matrix_flattened_size = len(matrix)*len(matrix[0])
        
        ans = []
        pos = [0,0]
        
        def go_right(right):
            while pos[0] < right-1 and len(ans)<matrix_flattened_size:
                ans.append(matrix[pos[1]][pos[0]])
                pos[0] += 1
            right -= 1
            #print(ans)
        
        def go_left(left):
            while pos[0] > left and len(ans)<matrix_flattened_size:
                ans.append(matrix[pos[1]][pos[0]])
                pos[0] -= 1
            left += 1
            #print(ans)
        
        def go_down(bot):
            while pos[1] < bot-1 and len(ans)<matrix_flattened_size:
                ans.append(matrix[pos[1]][pos[0]])
                pos[1] += 1
            bot -= 1
            #print(ans)
            
        def go_up(top):
            while pos[1] > top and len(ans)<matrix_flattened_size:
                ans.append(matrix[pos[1]][pos[0]])
                pos[1] -= 1
            top += 1
            
        if len(matrix[0]) == 1:
            i=0
            while len(ans)<matrix_flattened_size:
                ans.append(matrix[i][0])
                i += 1
            return ans
        
        while len(ans) < matrix_flattened_size:
                go_right(right)
                go_down(bot)
                go_left(left)
                go_up(top)
        
        return ans
"""