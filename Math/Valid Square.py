"""
98%
Valid Square

Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).



Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

Example 3:

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true



Constraints:

    p1.length == p2.length == p3.length == p4.length == 2
    -104 <= xi, yi <= 104
"""
import collections
class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:


        def distance(po1,po2):
            return ((po1[0]-po2[0])**2+(po1[1]-po2[1])**2)**(1/2) #You dont need the sqrt function

        l = [p1,p2,p3,p4]
        if l.count(p1) > 1 or l.count(p2) > 1 or l.count(p3) > 1:
            return False
        c = collections.Counter()
        for i in range(len(l)-1):
            for j in range(i+1,len(l)):
                c[distance(l[i],l[j])] += 1
        return c.most_common()[0][1] == 4 and c.most_common()[1][1] == 2

if __name__ == '__main__':
    def test(input1, input2, input3, input4):
        Test = Solution()
        ans = Test.validSquare(input1,input2,input3,input4)
        print(ans)
        return ans

    assert test([0,0], [1,1], [1,0], [0,1]) == True
    assert test([0, 0], [1, 1], [1, 0], [0, 12]) == False
    assert test([1, 0], [-1, 0], [0, 1], [0, -1]) == True
    assert test([1, 1], [5, 3], [3, 5], [7, 7]) == False
    assert test([0,1], [1,1], [0,0], [1,1]) == False

"""
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # distance between 2 points
        def dist(p1, p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    
	    # all possible lines
        l = sorted([dist(p1,p2),dist(p1,p3),dist(p1,p4),dist(p2,p3),dist(p2,p4),dist(p3,p4)])
    
	    # check 4 equal sides & 2 equal diagonals
        return l[0]==l[1]==l[2]==l[3] and l[3]!=l[4] and l[4]==l[5]
    
"""