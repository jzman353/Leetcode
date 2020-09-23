#27%
"""
Random Point in Nonoverlapping Rectangles (Medium)
Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

    An integer point is a point that has integer coordinates.
    A point on the perimeter of a rectangle is included in the space covered by the rectangles.
    ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
    length and width of each rectangle does not exceed 2000.
    1 <= rects.length <= 100
    pick return a point as an array of integer coordinates [p_x, p_y]
    pick is called at most 10000 times.

Example 1:

Input:
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output:
[null,[4,1],[4,1],[3,3]]

Example 2:

Input:
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output:
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""


class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.length = len(self.rects)
    def pick(self):
        num_points = [0 for i in range(self.length)]
        for count, rect in enumerate(self.rects):
            num_points[count] = (rect[3]-rect[1]+1)*(rect[2]-rect[0]+1)
        import random
        rect_index = random.choices(range(self.length),weights = num_points)[0]
        #print(self.rects[rect_index])
        y = random.randint(self.rects[rect_index][1], self.rects[rect_index][3])
        x = random.randint(self.rects[rect_index][0], self.rects[rect_index][2])
        return [x,y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

if __name__ == '__main__':
    def test(input1):
        Test = Solution(input1)
        ans = Test.pick()
        print(ans)

    rects = [[1,1,5,5]]
    test(rects)

    rects = [[-2,-2,-1,-1],[1,0,3,0]]
    test(rects)

# print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))

"""
class Solution:
    def __init__(self, rects):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [i/sum(w) for i in accumulate(w)]
        self.rects = rects

    def pick(self):
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)]
"""