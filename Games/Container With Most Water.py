#59%
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
import timeit

class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height)-1
        maxx = 0
        while left <= right:
            area = (right-left)*min(height[right],height[left])
            maxx = max(maxx,area)
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
        return maxx

if __name__ == '__main__':
    def test(height):
        Test = Solution()
        ans = Test.maxArea(height)
        #print(ans)

    height = [1,8,6,2,5,4,8,3,7]  #1 49
    test(height)

    print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))