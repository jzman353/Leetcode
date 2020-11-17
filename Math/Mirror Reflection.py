"""
12%
858. Mirror Reflection
Medium

There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)



Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Note:

    1 <= p <= 1000
    0 <= q <= p
"""

from fractions import Fraction

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        F = Fraction(q, p)
        #print(F)
        #print(F.numerator)
        pos = [0,0]
        self.x = 1
        self.y = 1
        def move(dx,dy):
            if dx>0:
                if pos[0] + self.x*dx >= p:
                    dx -= (p - pos[0])
                    pos[0] = p
                    self.x = -1
                elif pos[0] + self.x*dx <= 0:
                    dx -= pos[0]
                    pos[0] = 0
                    self.x = 1
                else:
                    pos[0] += self.x * dx
                    dx = 0
            if dy>0:
                if pos[1] + self.y*dy >= p:
                    dy -= (p - pos[1])
                    pos[1] = p
                    self.y = -1
                elif pos[1] + self.y*dy <= 0:
                    dy -= pos[1]
                    pos[1] = 0
                    self.y = 1
                else:
                    pos[1] += self.y * dy
                    dy = 0
            if dx > 0 or dy > 0:
                move(dx,dy)


        while pos != [p,0] and pos != [p,p] and pos != [0,p]:
            move(F.denominator, F.numerator)

        if pos == [p,0]:
            return 0
        if pos == [p,p]:
            return 1
        if pos == [0,p]:
            return 2

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.mirrorReflection(input1,input2)
        print(ans)
        return ans

    assert test(2, 1) == 2
    assert test(1, 1) == 1
    assert test(3, 2) == 0

"""
This solution only works if the values are strictly integers
import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:

        x = p // math.gcd(p, q)
        y = q // math.gcd(p, q)

        if x % 2 == 1 and y % 2 == 1:
            return 1
        elif x % 2 == 0 and y % 2 == 1:
            return 2
        else:
            return 0
"""