"""
54%
118. Pascal's Triangle
Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        length = 1
        for i in range(numRows):
            row = [1] * length
            for i in range(1, len(row) - 1):
                if ans[-2]:
                    row[i] = ans[-1][i - 1] + ans[-1][i]
            ans.append(row)
            length += 1
        return ans

"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        row = []
        
        def genRow(n, row):
            if n == 1:
                triangle.append([n])
                row = [1]
            elif n == 2:
                triangle.append([1,1])
                row = [1,1]
            else:
                newrow = [1]
                for i in range(0,len(row) - 1):
                    newrow.append(row[i] + row[i+1])
                newrow.append(1)
                row = newrow
                triangle.append(row)
            return row
            
        for i in range(1,numRows+1):
            row = genRow(i, row)
        return triangle
"""