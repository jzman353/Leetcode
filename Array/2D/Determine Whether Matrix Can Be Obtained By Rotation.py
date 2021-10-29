"""
1886. Determine Whether Matrix Can Be Obtained By Rotation
Easy

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:

Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:

Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
"""

#88%
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 0 degrees
        if mat == target:
            return True

        # 90 degrees
        # This function unzips mat (it gives a list of mat's columns but reverses the order within the columns)
        rot1 = list(zip(*mat[::-1]))
        if rot1 == [tuple(i) for i in target]:
            return True

        # 180 degrees
        rot2 = list(zip(*rot1[::-1]))
        if rot2 == [tuple(i) for i in target]:
            return True

        # 270 degrees
        rot3 = list(zip(*rot2[::-1]))
        if rot3 == [tuple(i) for i in target]:
            return True

        return False

"""
sample 24 ms submission
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        import copy
        stop = False
        count = 0
        a = mat
        n = len(mat)
        #print(n)
        while stop == False and count < 4:
            a_new = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    a_new[j][n-1-i] = a[i][j]
            #print(a_new, a)
            a = a_new.copy()
            if a == target:
                stop = True
            else:
                count += 1
        return stop == True

sample 28 ms submission
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            mat=self.rotate(mat)
            if mat==target:
                return True
        return False
    
    def rotate(self,mat):
        return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0])-1,-1,-1)]
    
sample 32 ms submission
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotateRight(arr):
            return [list(i)[::-1] for i in zip(*arr)]
        
        if mat == target:
            return True
        
        for i in range(3):
            mat = rotateRight(mat)
            if mat == target:
                return True
        
        return False

sample 40 ms submission
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if(mat==target):
                return True
            mat=[list(x) for x in list(zip(*mat[::-1]))]
        return False
"""