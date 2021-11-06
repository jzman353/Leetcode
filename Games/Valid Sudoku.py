"""
36. Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

#9%
class Solution:
    def box(self,board,i,j):
        if i<3:
            copy1 = copy.deepcopy(board[:3])
            if j<3:
                for k in range(len(copy1)):
                    copy1[k] = copy1[k][:3]
            elif j<6:
                for k in range(len(copy1)):
                    copy1[k] = copy1[k][3:6]
            else:
                for k in range(len(copy1)):
                    copy1[k] = copy1[k][6:]
        elif i<6:
            copy1 = copy.deepcopy(board[3:6])
            if j<3:
                for k in range(len(copy1)):
                    copy1[k] = copy1[k][:3]
            elif j<6:
                for k in range(len(copy1)):
                    copy1[k] = copy1[k][3:6]
            else:
                for k in range(len(copy1)):
                    copy1[k] = copy1[k][6:]
        else:
            copy1 = copy.deepcopy(board[6:])
            if j<3:
                for k in range(len(copy1)):
                    copy1[k] = copy1[k][:3]
            elif j<6:
                for k in range(len(copy1)):
                    copy1[k] = copy1[k][3:6]
            else:
                for k in range(len(copy1)):
                    copy1[k] = copy1[k][6:]
        return list(chain.from_iterable(copy1))
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                #if board[i][j] not in "123456789.":
                #    return False
                if board[i][j] != '.' and (board[i].count(board[i][j])>1 or list(zip(*board))[j].count(board[i][j])>1 or self.box(board,i,j).count(board[i][j])>1):
                    return False
        return True

"""
sample 68 ms submission
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        mMat = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    k = (i // 3) * 3 + (j // 3)
                    
                    if cur not in rows[i]: rows[i].add(cur)
                    else: return False
                
                    if cur not in cols[j]: cols[j].add(cur)
                    else: return False
                
                    if cur not in mMat[k]: mMat[k].add(cur)
                    else: return False
                
        return True  
"""