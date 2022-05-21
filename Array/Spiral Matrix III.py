"""
885. Spiral Matrix III
Medium

You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:

Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:

Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
"""
#52%
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        left = 0
        top = 0
        right = cols-1
        bot = rows-1
        inc = 0
        answer = []
        answer.append([rStart,cStart])
        while len(answer) < rows*cols:
            inc += 1
            #right
            for i in range(1,inc+1):
                cStart += 1
                if 0 <= rStart <= rows-1 and 0 <= cStart <= cols-1:
                    answer.append([rStart,cStart])
                    #print(answer)
            #down
            for i in range(1,inc+1):
                rStart += 1
                if 0 <= rStart <= rows-1 and 0 <= cStart <= cols-1:
                    answer.append([rStart,cStart])
                    #print(answer)
            inc += 1
            #left
            for i in range(1,inc+1):
                cStart -= 1
                if 0 <= rStart <= rows-1 and 0 <= cStart <= cols-1:
                    answer.append([rStart,cStart])
                    #print(answer)
            #up
            for i in range(1,inc+1):
                rStart -= 1
                if 0 <= rStart <= rows-1 and 0 <= cStart <= cols-1:
                    answer.append([rStart,cStart])
                    #print(answer)
        return answer

"""
sample 94 ms submission
class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        i, j = rStart, cStart
        coordinates = [[rStart,cStart]]
        
        step, sign = 1, 1
        
        while len(coordinates) < rows*cols:
            for _ in range(step):
                j += sign
                if i < rows and j < cols and i >= 0 and j >= 0:
                    coordinates.append([i,j])
                    
            for _ in range(step):
                i += sign
                if i < rows and j < cols and i >= 0 and j >= 0:
                    coordinates.append([i,j])
                    
            step += 1
            sign *= -1
    
        return coordinates

Solution:
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        ans = [(r0, c0)]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in xrange(1, 2*(R+C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):

                # For each of dk units in the current direction ...
                for _ in xrange(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans
"""