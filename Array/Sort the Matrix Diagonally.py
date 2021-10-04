"""
1329. Sort the Matrix Diagonally
Medium

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
Example 2:

Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""
#20%
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                bisect.insort(d[i-j],mat[i][j])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = d[i-j].pop(0)
        return mat
"""
Hints:
Use a data structure to store all values of each diagonal.
How to index the data structure with the id of the diagonal?
All cells in the same diagonal (i,j) have the same difference so we can get the diagonal of a cell using the difference i-j.

Pops from the end of the list as it is sorted backwards
sample 76 ms submission
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        
        for r in d:
            d[r].sort(reverse=True)
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop()
        
        return mat
"""