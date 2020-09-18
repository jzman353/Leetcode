#15%
"""
Robot Bounded in a Circle (Medium)
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

    "G": go straight 1 unit;
    "L": turn 90 degrees to the left;
    "R": turn 90 degress to the right.

The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:

Input: "GGLLGG"
Output: true
Explanation:
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input: "GG"
Output: false
Explanation:
The robot moves north indefinitely.

Example 3:

Input: "GL"
Output: true
Explanation:
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...



Note:

    1 <= instructions.length <= 100
    instructions[i] is in {'G', 'L', 'R'}

    Hide Hint #1
Calculate the final vector of how the robot travels after executing all instructions once - it consists of a change in position plus a change in direction.
   Hide Hint #2
The robot stays in the circle iff (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if instructions.count("L") == instructions.count("R") and instructions.count("G")>0:
            return False

        orig_pos, pos = [0,0], [0,0]
        orig_dir, dir = 0, 0
        for instructiion in instructions:
            if instructiion == "R":
                if dir < 3:
                    dir += 1
                else:
                    dir = 0
            elif instructiion == "L":
                if dir > 0:
                    dir -= 1
                else:
                    dir = 3
            elif instructiion == "G":
                if dir == 0:
                    pos[1] +=1
                elif dir == 1:
                    pos[0] += 1
                elif dir == 2:
                    pos[1] -= 1
                elif dir == 3:
                    pos[0] -= 1
        if pos == orig_pos or dir != orig_dir:
            return True
        else:
            return False


def test(instructions):
    Test = Solution()
    print(Test.isRobotBounded(instructions))

instructions = "GGLLGG"
test(instructions)

instructions = "GG"
test(instructions)

instructions = "GL"
test(instructions)

"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)
"""