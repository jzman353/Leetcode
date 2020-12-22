"""
1037. Valid Boomerang
Easy

A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true

Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false

Note:

    points.length == 3
    points[i].length == 2
    0 <= points[i][j] <= 100
"""
#57%
import collections
import math
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        for i in points:
            if i[0] in d.keys() and i[1] in d[i[0]]:
                return False
            d[i[0]].append(i[1])
        try:
            slope1 = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0])
        except:
            slope1 = math.inf
        try:
            slope2 = (points[1][1] - points[2][1]) / (points[1][0] - points[2][0])
        except:
            slope2 = math.inf
        if slope1 == slope2:
            return False

        return True