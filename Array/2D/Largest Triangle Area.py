"""
812. Largest Triangle Area
Easy

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.

Notes:

    3 <= points.length <= 50.
    No points will be duplicated.
     -50 <= points[i][j] <= 50.
    Answers within 10^-6 of the true value will be accepted as correct.
"""
#13%
import math
class Solution:
    def largestTriangleArea(self, points) -> float:
        ans = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    # height = max(max(points[i][1],points[j][1]),points[k][1])-min(min(points[i][1],points[j][1]),points[k][1])
                    # base = max(max(points[i][0],points[j][0]),points[k][0])-min(min(points[i][0],points[j][0]),points[k][0])
                    # area = .5*base*height
                    a = math.sqrt((points[i][1] - points[j][1]) ** 2 + (points[i][0] - points[j][0]) ** 2)
                    b = math.sqrt((points[j][1] - points[k][1]) ** 2 + (points[j][0] - points[k][0]) ** 2)
                    c = math.sqrt((points[k][1] - points[i][1]) ** 2 + (points[k][0] - points[i][0]) ** 2)
                    s = .5 * (a + b + c)
                    area = math.sqrt(abs(s) * abs(s - a) * abs(s - b) * abs(s - c))
                    if area > ans:
                        ans = area
        return ans

"""
#Optimize by trying to find upmost, leftmost, bottommost, rightmost and just using those points
import math
class Solution:
    def largestTriangleArea(self, points) -> float:
        right = [-math.inf,-math.inf]
        right_val = [0,0]
        left = [-math.inf,-math.inf]
        left_val = [0,0]
        up = [-math.inf,-math.inf]
        up_val = [0,0]
        down = [-math.inf,-math.inf]
        down_val = [0,0]
        for i in points:
            if i[0] > right[0]:
                right[0] = i[0]
                right_val[0] = i
            elif i[0] > right[1]:
                right[1] = i[0]
                right_val[1] = i
            if i[0] < left[0]:
                left[0] = i[0]
                left_val[0] = i
            elif i[0] < left[1]:
                left[1] = i[0]
                left_val[1] = i
            if i[1] > up[0]:
                up[0] = i[1]
                up_val[0] = i
            elif i[1] > up[1]:
                up[1] = i[1]
                up_val[1] = i
            if i[1] < down[0]:
                down[0] = i[1]
                down_val[0] = i
            elif i[1] < down[1]:
                down[1] = i[1]
                down_val[1] = i
        p = list({up_val[0], down_val[0], left_val[0], right_val[0]})
        if len(p) < 3:
            p = list({up_val[0], down_val[0], left_val[0], right_val[0], up_val[1], down_val[1], left_val[1], right_val[1]})
        ans = 0
        for i in range(len(p) - 2):
            for j in range(i + 1, len(p) - 1):
                for k in range(j + 1, len(p)):
                    # height = max(max(points[i][1],points[j][1]),points[k][1])-min(min(points[i][1],points[j][1]),points[k][1])
                    # base = max(max(points[i][0],points[j][0]),points[k][0])-min(min(points[i][0],points[j][0]),points[k][0])
                    # area = .5*base*height
                    a = math.sqrt((p[i][1] - p[j][1]) ** 2 + (p[i][0] - p[j][0]) ** 2)
                    b = math.sqrt((p[j][1] - p[k][1]) ** 2 + (p[j][0] - p[k][0]) ** 2)
                    c = math.sqrt((p[k][1] - p[i][1]) ** 2 + (p[k][0] - p[i][0]) ** 2)
                    s = .5 * (a + b + c)
                    area = math.sqrt(abs(s) * abs(s - a) * abs(s - b) * abs(s - c))
                    if area > ans:
                        ans = area
"""

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.largestTriangleArea(input1)
        print(ans)
        return ans

    assert math.isclose(test([[0,0],[0,1],[1,0],[0,2],[2,0]]), 2)
    assert math.isclose(test([[4, 6], [6, 5], [3, 1]]), 5.5)
    assert math.isclose(test([[-35,19],[40,19],[27,-20],[35,-3],[44,20],[22,-21],[35,33],[-19,42],[11,47],[11,37]]), 2) #24/57
"""  
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        print((itertools.combinations(points, 3)))
        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))
"""

"""


import math
class Solution:
    def largestTriangleArea(self, points):
        '''
        :type points: List[List[int]]
        :rtype: float
        '''
        return self.largestTriangeAreaInConvexHull(self.convex_hull(points))
        
        
        
        
    def largestTriangeAreaInConvexHull(self, points):
        
        max_area = 0
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    new_area = abs(0.5 * (points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][1]
                   - points[i][0] * points[k][1] - points[j][0] * points[i][1] - points[k][0] * points[j][1]))
                    max_area= max(max_area, new_area)
        return max_area
    
    
    def convex_hull(self, points):
        hull = []
        points = sorted(points,key=lambda l:l[1])
        ref_point= points[0]
        angle_points = []
        for p in points[1:]:
            angle = self.angle(ref_point, p)
            if angle < 0:
                angle = math.pi*2.0 + angle
            angle_points.append( [angle, p])
        
        
        angle_points.sort()
        hull.append(ref_point)
        hull.append(angle_points[0][1])

        for angle_point in angle_points[1:]:
            top = hull.pop()
            while len(hull) > 0 and self.ccw(hull[-1], top, angle_point[1]) < 0: #it is not <= because we want to keep all points in the convex hull, even if the are in a line
                top = hull.pop()
                
            hull.append(top)
            hull.append(angle_point[1])

        return hull
    
    def angle(self, reference, point):
        v1_x = point[0]-reference[0]
        v1_y = point[1] - reference[1]
        return math.atan2(v1_y, v1_x)
        
    def ccw(self, a, b, c):
        area2 = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        if area2 < 0:
            return -1 #clockwise
        if area2 >0 :
            return 1 #counter clock wise
        return 0 #linear
"""