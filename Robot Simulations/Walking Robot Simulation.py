"""
874. Walking Robot Simulation
Easy

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.



Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
"""

#36%
class Solution:
    def robotSim(self, commands, obstacles) -> int:
        # 0 : North, 1 : East, 2 : South, 3 : West
        self.pos = [0, 0]
        self.dir = 0
        obstacles = set(map(tuple, obstacles))

        def right():
            if self.dir == 3:
                self.dir = 0
            else:
                self.dir += 1

        def left():
            if self.dir == 0:
                self.dir = 3
            else:
                self.dir -= 1

        def move(distance):
            if self.dir == 0:
                axis = 1  # y
                direction = 1
            elif self.dir == 1:
                axis = 0  # x
                direction = 1
            elif self.dir == 2:
                axis = 1  # y
                direction = -1
            else:
                axis = 0  # x
                direction = -1
            for i in range(distance):
                if axis == 0:
                    potential_position = [self.pos[0] + direction, self.pos[1]]
                else:
                    potential_position = [self.pos[0], self.pos[1] + direction]
                if tuple(potential_position) not in obstacles:
                    self.pos = potential_position
                else:
                    break

        max_dist = 0
        for i in commands:
            if i == -2:
                left()
            elif i == -1:
                right()
            else:
                move(i)
                max_dist = max(max_dist, self.pos[0] ** 2 + self.pos[1] ** 2)

        return max_dist

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.robotSim(input1,input2)
        print(ans)
        return ans

    assert test([4,-1,3], []) == 25
    assert test([4,-1,4,-2,4], [[2,4]]) == 65

"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {(x, y) for x, y in obstacles}
        
        dist = 0
        x, y = 0, 0
        dx, dy = 0, 1
        
        for move in commands:
            if move == -2:
                dx, dy = -dy, dx
            elif move == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(move):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy
                
                dist = max(dist, x*x + y*y)
                
        return dist
"""