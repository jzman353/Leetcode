"""
67%
1275. Find Winner on a Tic Tac Toe Game
Easy

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

    Players take turns placing characters into empty squares (" ").
    The first player A always places "X" characters, while the second player B always places "O" characters.
    "X" and "O" characters are always placed into empty squares, never on filled ones.
    The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.

Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
"   "    "   "    "   "    "   "    "   "    "O  "

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"

Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "

Constraints:

    1 <= moves.length <= 9
    moves[i].length == 2
    0 <= moves[i][j] <= 2
    There are no repeated elements on moves.
    moves follow the rules of tic tac toe.
"""

import collections
class Solution:
    def tictactoe(self, moves) -> str:
        move = "A"
        d = collections.deque(moves)
        board = [[0 for i in range(3)] for j in range(3)]

        def checkWin():
            # Rows
            for i in board:
                if i == ["A", "A", "A"]:
                    return "A"
                if i == ["B", "B", "B"]:
                    return "B"
            # Cols
            for i in range(len(board)):
                col = [sub[i] for sub in board]
                if col == ["A", "A", "A"]:
                    return "A"
                if col == ["B", "B", "B"]:
                    return "B"
            # Diagonals
            if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
                if board[1][1] == "A":
                    return "A"
                if board[1][1] == "B":
                    return "B"

        while d:
            x, y = d.popleft()
            board[x][y] = move
            ans = checkWin()
            if ans:
                return ans
            if move == "A":
                move = "B"
            else:
                move = "A"

        if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
            return "Draw"
        else:
            return "Pending"

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.tictactoe(input1)
        print(ans)
        return ans

    assert test([[0,0],[2,0],[1,1],[2,1],[2,2]]) == "A"
    assert test([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]) == "B"
    assert test([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]) == "Draw"
    assert test([[0,0],[1,1]]) == "Pending"
