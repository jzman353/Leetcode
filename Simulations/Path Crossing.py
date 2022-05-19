"""
1496. Path Crossing
Easy

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

Example 1:

Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""
#73%
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        been = [[0,0]]
        pos = [0,0]
        for i in path:
            if i == 'N':
                pos = [pos[0],pos[1]+1]
            elif i == 'S':
                pos = [pos[0],pos[1]-1]
            elif i == 'E':
                pos = [pos[0]+1,pos[1]]
            else:
                pos = [pos[0]-1,pos[1]]
            if pos in been:
                return True
            been.append(pos)
        return False
"""
#73%
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        been = set()
        been.add((0,0))
        pos = (0,0)
        for i in path:
            if i == 'N':
                pos = (pos[0],pos[1]+1)
            elif i == 'S':
                pos = (pos[0],pos[1]-1)
            elif i == 'E':
                pos = (pos[0]+1,pos[1])
            else:
                pos = (pos[0]-1,pos[1])
            if pos in been:
                return True
            been.add(pos)
        return False
"""
"""
#This solution relies on the fact that there is an upward bound of the path length
sample 16 ms submission
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set([0])
        x = y = 0
        for s in path:
            if s == 'N':
                y += 1
            elif s == 'S':
                y -= 1
            elif s == 'E':
                x += 1
            else:
                x -= 1
            
            if x * 10001 + y in seen:
                return True
            seen.add(x * 10001 + y)
        return False;
"""