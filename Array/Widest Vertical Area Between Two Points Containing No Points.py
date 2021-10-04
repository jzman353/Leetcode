"""
1637. Widest Vertical Area Between Two Points Containing No Points
Medium

Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Example 1:

​
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.
Example 2:

Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3

Constraints:

n == points.length
2 <= n <= 105
points[i].length == 2
0 <= xi, yi <= 109
"""
#50%
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        maxx = 0
        for i in range(len(points)-1):
            maxx = max(maxx,abs(points[i][0]-points[i+1][0]))
        return maxx

"""
sample 780 ms submission
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        xVals = sorted([row[0] for row in points])
        
        return max(map(lambda x,y: x-y, xVals + [xVals[-1]], [xVals[0]] + xVals))
        
sample 796 ms submission
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted([x for x, y in points])
        return max(b-a for a, b in zip(xs, xs[1:]))
"""