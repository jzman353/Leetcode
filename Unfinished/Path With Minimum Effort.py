"""
1631. Path With Minimum Effort
Medium

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.



Constraints:

    rows == heights.length
    columns == heights[i].length
    1 <= rows, columns <= 100
    1 <= heights[i][j] <= 106
"""
import math

def isLeft(pos):
    return pos[1] == 0

def isRight(pos, heights):
    return pos[1] == len(heights) - 1

def isTop(pos):
    return pos[0] == 0

def isBot(pos, heights):
    return pos[0] == len(heights[0]) - 1

def options1(pos, heights, past):
    options = ["L", "R", "U", "D"]
    if isLeft(pos) or past[pos[1] - 1][pos[0]] == 1:
        options.remove("L")
    if isRight(pos, heights) or past[pos[1] + 1][pos[0]] == 1:
        options.remove("R")
    if isTop(pos) or past[pos[1]][pos[0] - 1] == 1:
        options.remove("U")
    if isBot(pos, heights) or past[pos[1]][pos[0] + 1] == 1:
        options.remove("D")
    return options

class Solution:
    def minimumEffortPath(self, heights) -> int:
        past = [[0 for i in range(len(heights))] for j in range(len(heights[0]))]

        def test(past, pos, effort):
            if pos == [len(heights) - 1, len(heights[0]) - 1]:
                self.minn = min(self.minn, effort)
            past[pos[1]][pos[0]] = 1
            options = options1(pos, heights, past)
            for i in options:
                if i == "L":
                    pos1 = [pos[1] - 1, pos[0]]
                    effort = max(effort, heights[pos1[1]][pos1[0]] - heights[pos[1]][pos[0]])
                elif i == "R":
                    pos1 = [pos[1] + 1, pos[0]]
                    effort = max(effort, heights[pos1[1]][pos1[0]] - heights[pos[1]][pos[0]])
                elif i == "D":
                    pos1 = [pos[1], pos[0] + 1]
                    effort = max(effort, heights[pos1[1]][pos1[0]] - heights[pos[1]][pos[0]])
                elif i == "U":
                    pos1 = [pos[1], pos[0] - 1]
                    effort = max(effort, heights[pos1[1]][pos1[0]] - heights[pos[1]][pos[0]])
                return [past, pos1, effort]

        stack = [[past, [0, 0], 0]]
        self.minn = math.inf

        while stack:
            temp = stack.pop()
            ans = test(temp[0], temp[1], temp[2])
            if ans:
                stack.append(ans)
        return self.minn

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.minimumEffortPath(input1)
        print(ans)
        return ans


    #assert test([[1,1],[1,1]]) == 0
    assert test([[1,2,2],[3,8,2],[5,3,5]]) == 2
    assert test([[1,2,3],[3,8,4],[5,3,5]]) == 1
    assert test([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0