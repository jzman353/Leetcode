#https://www.math.net/circle-formula
"""
1828. Queries on Number of Points Inside a Circle
Medium

You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.

Example 1:
Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
Output: [3,2,2]
Explanation: The points and circles are shown above.
queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.
Example 2:

Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
Output: [2,3,2,4]
Explanation: The points and circles are shown above.
queries[0] is green, queries[1] is red, queries[2] is blue, and queries[3] is purple.

Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= x​​​​​​i, y​​​​​​i <= 500
1 <= queries.length <= 500
queries[j].length == 3
0 <= xj, yj <= 500
1 <= rj <= 500
All coordinates are integers.
"""

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = [0]*len(queries)
        for i, circ in enumerate(queries):
            for j in points:
                #if j inside i then add 1 to answers[i]
                if sqrt((j[0]-circ[0])**2+(j[1]-circ[1])**2)<=circ[2]:
                    answer[i] += 1
        return answer

"""
sample 504 ms submission
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        P = [complex(x,y) for x,y in points]
        Q = [(complex(x,y),r) for x,y,r in queries]
        return [sum(1 for p in P if abs(p-q) <= r) for q, r in Q]

#Note that the sqrt function is slower than the **2 function
sample 876 ms submission
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for x,y,r in queries:
            count = 0
            for a,b in points:
                if ((x-a)*(x-a) + (y-b)*(y-b) - r*r) <= 0:
                    count += 1
            answer.append(count)
        return answer
"""