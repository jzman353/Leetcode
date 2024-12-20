"""
999. Available Captures for Rook
Easy

On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.

Example 1:

Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.
Example 2:


Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: The bishops are blocking the rook from attacking any of the pawns.
Example 3:

Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: The rook is attacking the pawns at positions b5, d6, and f5.

Constraints:

board.length == 8
board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
"""
#23%
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        #Find rook
        rook_pos = []
        for i in range(8):
            if rook_pos:
                break
            for j in range(8):
                if board[i][j] == "R":
                    rook_pos = [i,j]
                    break
        answer = 0
        #Look up
        i = rook_pos[0]-1
        j = rook_pos[1]
        while i >= 0:
            if board[i][j] == "p":
                answer += 1
                break
            elif board[i][j] == "B":
                break
            i -= 1
        #Look down
        i = rook_pos[0]+1
        while i < 8:
            if board[i][j] == "p":
                answer += 1
                break
            elif board[i][j] == "B":
                break
            i += 1
        #Look right
        i = rook_pos[0]
        j = rook_pos[1]+1
        while j < 8:
            if board[i][j] == "p":
                answer += 1
                break
            elif board[i][j] == "B":
                break
            j += 1
        #Look left
        j = rook_pos[1]-1
        while j >= 0:
            if board[i][j] == "p":
                answer += 1
                break
            elif board[i][j] == "B":
                break
            j -= 1
        return answer

"""
#This solution is similar to mine but I like that it uses less code for the up/down/left/right checks
#They could break the for loops in the first section when the Rook is found
sample 16 ms submission
class Solution:
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x0, y0 = i, j
        res = 0
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x, y = x0 + dx, y0 + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p': res += 1
                if board[x][y] != '.': break
                x, y = x + dx, y + dy
        return res
"""