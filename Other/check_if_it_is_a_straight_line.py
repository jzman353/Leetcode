'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

If there're only 2 points, return true.
Check if all other points lie on the line defined by the first 2 points.
Use cross product to check collinearity.

Runtime: 92 ms Beats nobody
Memory Usage: 14.1 MB
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = [None]*len(coordinates)
        for count in range(len(coordinates)-1):
            if (coordinates[count+1][0]-coordinates[count][0]) != 0:
                slope[count] = (coordinates[count+1][1]-coordinates[count][1])/(coordinates[count+1][0]-coordinates[count][0])
            else:
                slope[count] = "inf"
        set1=set(slope)
        set1.remove(None)
        if len(set1)>1:
            return False
        return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))

'''
Runtime: 64 ms
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1,y1),(x2,y2) = coordinates[:2]
        for i in range(2,len(coordinates)):
            (x,y) = coordinates[i]
            if ((y-y1)*(x2-x1))!=((y2-y1)*(x-x1)):
                return False
        return True  

Runtime: 52ms
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(2, len(coordinates)):
            if coordinates[0][0]*(coordinates[1][1] - coordinates[i][1]) + \
                coordinates[1][0]*(coordinates[i][1] - coordinates[0][1]) + \
                coordinates[i][0]*(coordinates[0][1] - coordinates[1][1]) == 0:
                continue
            else:
                return False
        return True
'''