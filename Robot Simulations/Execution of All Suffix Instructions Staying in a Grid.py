"""
2120. Execution of All Suffix Instructions Staying in a Grid
Medium

There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).

You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).

The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:

The next instruction will move the robot off the grid.
There are no more instructions left to execute.
Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.

Example 1:

Input: n = 3, startPos = [0,1], s = "RRDDLU"
Output: [1,5,4,3,1,0]
Explanation: Starting from startPos and beginning execution from the ith instruction:
- 0th: "RRDDLU". Only one instruction "R" can be executed before it moves off the grid.
- 1st:  "RDDLU". All five instructions can be executed while it stays in the grid and ends at (1, 1).
- 2nd:   "DDLU". All four instructions can be executed while it stays in the grid and ends at (1, 0).
- 3rd:    "DLU". All three instructions can be executed while it stays in the grid and ends at (0, 0).
- 4th:     "LU". Only one instruction "L" can be executed before it moves off the grid.
- 5th:      "U". If moving up, it would move off the grid.
Example 2:

Input: n = 2, startPos = [1,1], s = "LURD"
Output: [4,1,0,0]
Explanation:
- 0th: "LURD".
- 1st:  "URD".
- 2nd:   "RD".
- 3rd:    "D".
Example 3:

Input: n = 1, startPos = [0,0], s = "LRUD"
Output: [0,0,0,0]
Explanation: No matter which instruction the robot begins execution from, it would move off the grid.

Constraints:

m == s.length
1 <= n, m <= 500
startPos.length == 2
0 <= startrow, startcol < n
s consists of 'L', 'R', 'U', and 'D'.
"""
#62.49%
import copy

class Solution:
    def executeInstructions(self, n: int, startPos, s: str):
        ans = []
        for j in range(len(s)):
            temp = 0
            pos = copy.deepcopy(startPos)
            for i in s[j:]:
                if i == 'R':
                    if pos[1] + 1 > n-1:
                        ans.append(temp)
                        break
                    else:
                        temp += 1
                        pos[1] += 1
                elif i == 'L':
                    if pos[1] - 1 < 0:
                        ans.append(temp)
                        break
                    else:
                        temp += 1
                        pos[1] -= 1
                elif i == 'U':
                    if pos[0] - 1 < 0:
                        ans.append(temp)
                        break
                    else:
                        temp += 1
                        pos[0] -= 1
                elif i == 'D':
                    if pos[0] + 1 > n-1:
                        ans.append(temp)
                        break
                    else:
                        temp += 1
                        pos[0] += 1
            else:
                ans.append(temp)
        return ans

if __name__ == '__main__':
    def test(input1, input2, input3):
        Test = Solution()
        ans = Test.executeInstructions(input1, input2, input3)
        print(ans)
        return ans

    assert test(3, [0, 1], "RRDDLU") == [1,5,4,3,1,0]

"""
sample 78 ms submission
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        direc = {'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
        upmost = startPos[0] + 1
        downmost = n - startPos[0]
        leftmost = startPos[1] + 1
        rightmost = n - startPos[1]
        curr_row,curr_col = 0,0    
        next_row,next_col = {0:m}, {0:m}
        ans = []
        
        for i in range(m-1,-1,-1):
            curr_row -= direc[s[i]][0]
            curr_col -= direc[s[i]][1]
            maxstep = m-i
            if curr_row - upmost in next_row:  
                maxstep = min(maxstep,  next_row[curr_row - upmost] - i - 1 )
            if curr_row + downmost in next_row:  
                maxstep = min(maxstep,  next_row[curr_row + downmost] - i - 1 )
            if curr_col - leftmost in next_col:  
                maxstep = min(maxstep,  next_col[curr_col - leftmost] - i - 1 )
            if curr_col + rightmost in next_col: 
                maxstep = min(maxstep,  next_col[curr_col + rightmost] - i - 1 )
            next_row[curr_row] = i
            next_col[curr_col] = i
            ans.append(maxstep)
            
        return ans[::-1]
"""