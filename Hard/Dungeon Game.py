"""
174. Dungeon Game
Hard

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
Example 2:

Input: dungeon = [[0]]
Output: 1

Constraints:

m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
"""
#TLE
import math
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        self.maxx = -math.inf
        minPath = dungeon[0][0]
        pos = [0,0]
        def recursion(pos,minPath,worst):
            if pos == [len(dungeon) - 1, len(dungeon[0]) - 1]:
                self.maxx = max(self.maxx, worst)
                return
            else:
                if pos[1]+1 != len(dungeon[0]):
                    worst1 = min(worst,minPath+dungeon[pos[0]][pos[1]+1])
                    if worst1 < self.maxx:
                        pass
                    else:
                        recursion([pos[0],pos[1]+1],minPath+dungeon[pos[0]][pos[1]+1],worst1)
                if pos[0]+1 != len(dungeon):
                    worst1 = min(worst,minPath+dungeon[pos[0]+1][pos[1]])
                    if worst1 < self.maxx:
                        return
                    recursion([pos[0]+1,pos[1]],minPath+dungeon[pos[0]+1][pos[1]],worst1)
        worst = dungeon[0][0]
        recursion(pos,minPath,worst)
        if self.maxx <= 0:
            return abs(self.maxx) + 1
        else:
            return 1

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.calculateMinimumHP(input1)
        print(ans)
        return ans

    assert test([[-2,-3,3],[-5,-10,1],[10,30,-5]]) == 7
    assert test([[0]]) == 1
    assert test([[1,2,3,4]]) == 1
    assert test([[-10, -345], [55, -123]]) == 79
    assert test([[-10,-345,0],[55,-123,634],[160,310,-500]]) == 11
    assert test([[100]]) == 1
    assert test([[3,0,-3],[-3,-2,-2],[3,1,-3]]) == 1