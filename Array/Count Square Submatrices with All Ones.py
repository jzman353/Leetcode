'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1

Create an additive table that counts the sum of elements of submatrix with the superior corner at (0,0).

Loop over all subsquares in O(n^3) and check if the sum make the whole array to be ones, if it checks then add 1 to the answer.

Runtime: 884 ms Beats 20%
Memory Usage: 16 MB
'''
# def countSquares(self, matrix: List[List[int]]) -> int:


def countSquares(matrix) -> int:

    def square(matrix, row, col, k):
        if matrix[row][col + k] == 1 and matrix[row + k][col] == 1:
            for i in range(1, k + 1):
                if matrix[row + i][col + k] == 1 and matrix[row + k][col + i] == 1:
                    continue
                else:
                    return False
            return True
        else:
            return False

    output = 0
    for count1, row in enumerate(matrix):
        for count2, item in enumerate(row):
            if item == 1:
                output += 1
                for k in range(1, len(row) + 1):
                    try:
                        if square(matrix, count1, count2, k):
                            output += 1
                        else:
                            break
                    except:
                        pass
    return output


matrix =[[0,1,1,1],
         [1,1,1,1],
         [0,1,1,1]]

print(countSquares(matrix))

'''
Runtime: 636 ms
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        squares = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    if (i == 0 or j == 0):
                        squares[i][j] = 1
                    else:
                        squares[i][j] = min(
                            squares[i - 1][j - 1],
                            squares[i - 1][j],
                            squares[i][j - 1]
                        ) + 1

        return sum(map(sum, squares))
        
Runtime: 660 ms
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        col= len(matrix)
        row= len(matrix[0])
        res=0
        for i in range(col):
            
            for j in range(row):
                # if matrix[i][j]==0:
                #     continue
                    
                if(i*j > 0 and matrix[i][j]):
                    min_edge = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])
                    matrix[i][j]+=min_edge
                res+=matrix[i][j]
        return res
'''



