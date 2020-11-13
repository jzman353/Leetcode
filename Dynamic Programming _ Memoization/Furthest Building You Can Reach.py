"""
1642. Furthest Building You Can Reach
Medium

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

    If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
    If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.



Example 1:

Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3



Constraints:

    1 <= heights.length <= 105
    1 <= heights[i] <= 106
    0 <= bricks <= 109
    0 <= ladders <= heights.length
"""

#Time limit Exeeded 11/73
#Memoisation with a tree for accountability
"""
class TreeNode:
    def __init__(self, val=[], left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        max_level = 0
        root = TreeNode([0,bricks,ladders])
        stack = [root]
        while stack:
            currRoot = stack.pop()
            lev = currRoot.val[0]
            while lev < len(heights)-1 and heights[lev]>heights[lev+1]:
                lev += 1
            max_level = max(max_level, lev)

            if lev < len(heights)-1 and currRoot.val[1]>=heights[lev+1]-heights[lev]:
                currRoot.left = TreeNode([lev+1,currRoot.val[1]-(heights[lev+1]-heights[lev]),currRoot.val[2]])
                stack.append(currRoot.left)
            if lev < len(heights)-1 and currRoot.val[2]>0:
                currRoot.right = TreeNode([lev+1,currRoot.val[1],currRoot.val[2]-1])
                stack.append(currRoot.right)
        return max_level
"""
"""
#Time limit Exeeded 11/73
#Memoisation without a tree
class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        max_level = 0
        stack = [[0,bricks,ladders]]
        while stack:
            curr = stack.pop()
            lev = curr[0]
            while lev < len(heights)-1 and heights[lev]>heights[lev+1]:
                lev += 1
            max_level = max(max_level, lev)
            bric = curr[1]
            lad = curr[2]

            if lev < len(heights)-1 and bric>=heights[lev+1]-heights[lev]:
                stack.append([lev+1,bric-(heights[lev+1]-heights[lev]),lad])
            if lev < len(heights)-1 and lad>0:
                stack.append([lev+1,bric,lad-1])
        return max_level
"""
#19%
import bisect
class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        h_diff = []
        level = 0
        for i in range(len(heights)-1):
            temp = heights[i+1]-heights[i]
            if temp <= 0:
                level += 1
            elif bricks >= temp:
                level += 1
                bisect.insort_right(h_diff, temp)
                bricks -= temp
            elif ladders and h_diff and temp < h_diff[-1]:
                bricks += h_diff.pop()
                bisect.insort_right(h_diff, temp)
                bricks -= temp
                level += 1
                ladders -= 1
            elif ladders:
                level += 1
                ladders -= 1
            else:
                return level
        return level



        """max_level = 0
        stack = [[0,bricks,ladders]]
        while stack:
            curr = stack.pop()
            lev = curr[0]
            while lev < len(heights)-1 and heights[lev]>heights[lev+1]:
                lev += 1
            max_level = max(max_level, lev)
            bric = curr[1]
            lad = curr[2]

            if lev < len(heights)-1 and bric>=heights[lev+1]-heights[lev]:
                stack.append([lev+1,bric-(heights[lev+1]-heights[lev]),lad])
            if lev < len(heights)-1 and lad>0:
                stack.append([lev+1,bric,lad-1])
        return max_level"""

if __name__ == '__main__':
    def test(input1, input2, input3):
        Test = Solution()
        ans = Test.furthestBuilding(input1, input2, input3)
        print(ans)
        return ans

    assert test([4, 2, 7, 6, 9, 14, 12],5,1) == 4
    assert test([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7
    assert test([14, 3, 19, 3], 17, 0) == 3
    assert test([14, 13, 12, 3], 17, 0) == 3
    assert test([1, 2, 3, 4], 17, 3) == 3
    assert test([1, 2, 3, 4], 17, 17) == 3
    assert test([1,13,1,1,13,5,11,11], 10, 8) == 7

    """
    class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        for i in range(1, len(heights)):
            height_diff = heights[i] - heights[i-1]
            if height_diff <= 0:
                continue
            
            if bricks > 0 and height_diff <= bricks:
                bricks -= height_diff
                heapq.heappush(h, -height_diff)
            elif ladders > 0:
                ladders -= 1
                if len(h) > 0 and -h[0] > height_diff:
                    bricks += -(h[0] + height_diff)
                    heapq.heappop(h)
            else:
                return i - 1
            
        return len(heights) - 1
    
    class Solution:
      def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
          diff = heights[i+1] - heights[i]
          if diff <= 0:
            continue
          heapq.heappush(heap, diff)
          if len(heap) > ladders:
            bricks -= heapq.heappop(heap)
            if bricks < 0:
              return i
        return len(heights) - 1
        
    #A faster alternitive to the above:
    class Solution:
      def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
          diff = heights[i+1] - heights[i]
          if diff <= 0:
            continue
          if len(heap) <= ladders:
            heapq.heappush(heap, diff)
          else:
            bricks -= heapq.heappushpop(heap, diff)
            if bricks < 0:
              return i
        return len(heights) - 1
    """