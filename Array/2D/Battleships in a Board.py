"""
419. Battleships in a Board
Medium

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:

Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.


Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
"""
#5%
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        self.seen = []
        answer = 0

        def lookDown(pos):
            if pos[0] + 1 < len(board):
                self.seen.append([pos[0] + 1, pos[1]])
                if board[pos[0] + 1][pos[1]] == "X":
                    lookDown([pos[0] + 1, pos[1]])

        def lookRight(pos):
            if pos[1] + 1 < len(board[0]):
                self.seen.append([pos[0], pos[1] + 1])
                if board[pos[0]][pos[1] + 1] == "X":
                    lookRight([pos[0], pos[1] + 1])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if [i, j] not in self.seen:
                    self.seen.append([i, j])
                    if board[i][j] == "X":
                        answer += 1
                        lookDown([i, j])
                        lookRight([i, j])

        return answer

"""
sample 57 ms submission
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def isHead(i, j):
            #return True/False
            if board[i][j] == 'X' and  \
                (i == 0 or board[i - 1][j] != 'X') and \
                (j == 0 or board[i][j-1] != 'X'):
                return True
            
            return False
        
        R = len(board)
        C = len(board[0])
        bCount = 0
        for i in range(R):
            for j in range(C):
                if isHead(i, j):
                    bCount += 1
                    
        return bCount
"""