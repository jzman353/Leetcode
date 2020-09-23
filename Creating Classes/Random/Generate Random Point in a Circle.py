"""
(x-2)^2+(y-4)^2=81 is the equation for a circle with radius 81 and shift of +2 on x axis, +4 on y axis

Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

    input and output values are in floating-point.
    radius and x-y position of the center of the circle is passed into the class constructor.
    a point on the circumference of the circle is considered to be in the circle.
    randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

Example 1:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""

#Problem with this implimentation (rectangular coordinates)
# randX has uniform distribution, but in a circle, the X distribution is actually not uniform. It should be denser closer to the center.
#Passes 7/8
"""
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        import random
        x = random.uniform(-self.radius+self.x_center,self.radius+self.x_center)
        #from sympy import symbols, solve

        #y = symbols('y')
        #expr = (x-self.x_center)**2+(y-self.y_center)**2-self.radius**2
        #sol = solve(expr)
        print(x)
        sol = [math.sqrt(abs(-self.x_center**2+2*self.x_center*x+self.radius**2-x**2))+self.y_center,-math.sqrt(abs(-self.x_center**2+2*self.x_center*x+self.radius**2-x**2))+self.y_center]
        y = random.choice(sol)
        return [x,y]
"""

import math
import random

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        #This line will make r more likely to be close to the radius tather than close to the center
        r = math.sqrt(random.random()) * self.radius
        theta = 2 * random.random() * math.pi

        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)

        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
if __name__ == '__main__':
    def test(input1,input2,input3):
        Test = Solution(input1,input2,input3)
        ans = Test.randPoint()
        print(ans)

    #radius, x_center, y_center
    points = [1,0,0]
    test(points[0],points[1],points[2])
    points = [1, 0, 0]
    test(points[0], points[1], points[2])
    points = [1, 0, 0]
    test(points[0], points[1], points[2])

    points = [10, 0, 0]
    test(points[0], points[1], points[2])

    points = [10,5,-7.5]
    test(points[0], points[1], points[2])

# print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))

"""
https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly
Why sqrt(random())?

Let's look at the math that leads up to sqrt(random()). Assume for simplicity that we're working with the unit circle, i.e. R = 1.

The average distance between points should be the same regardless of how far from the center we look. This means for example, that looking on the perimeter of a circle with circumference 2 we should find twice as many points as the number of points on the perimeter of a circle with circumference 1.


                

Since the circumference of a circle (2πr) grows linearly with r, it follows that the number of random points should grow linearly with r. In other words, the desired probability density function (PDF) grows linearly. Since a PDF should have an area equal to 1 and the maximum radius is 1, we have


                

So we know how the desired density of our random values should look like. Now: How do we generate such a random value when all we have is a uniform random value between 0 and 1?

We use a trick called inverse transform sampling

    From the PDF, create the cumulative distribution function (CDF)
    Mirror this along y = x
    Apply the resulting function to a uniform value between 0 and 1.

Sounds complicated? Let me insert a blockquote with a little side track that conveys the intuition:

    Suppose we want to generate a random point with the following distribution:

                    

    That is

        1/5 of the points uniformly between 1 and 2, and
        4/5 of the points uniformly between 2 and 3.

    The CDF is, as the name suggests, the cumulative version of the PDF. Intuitively: While PDF(x) describes the number of random values at x, CDF(x) describes the number of random values less than x.

    In this case the CDF would look like:

                    

    To see how this is useful, imagine that we shoot bullets from left to right at uniformly distributed heights. As the bullets hit the line, they drop down to the ground:

                    

    See how the density of the bullets on the ground correspond to our desired distribution! We're almost there!

    The problem is that for this function, the y axis is the output and the x axis is the input. We can only "shoot bullets from the ground straight up"! We need the inverse function!

    This is why we mirror the whole thing; x becomes y and y becomes x:

                    

    We call this CDF-1. To get values according to the desired distribution, we use CDF-1(random()).

…so, back to generating random radius values where our PDF equals 2x.

Step 1: Create the CDF:

Since we're working with reals, the CDF is expressed as the integral of the PDF.

CDF(x) = ∫ 2x = x2

Step 2: Mirror the CDF along y = x:

Mathematically this boils down to swapping x and y and solving for y:

CDF:     y = x2
Swap:   x = y2
Solve:   y = √x
CDF-1:  y = √x

Step 3: Apply the resulting function to a uniform value between 0 and 1

CDF-1(random()) = √random()

Which is what we set out to derive :-)
"""