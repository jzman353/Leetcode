"""
79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

#38%
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.answer = False

        def helper(board, word, pos, used, curr=word[0], word_inx=1):
            if self.answer:
                return
            if curr == word:
                self.answer = True
                return
            for i in [[pos[0], pos[1] - 1], [pos[0], pos[1] + 1], [pos[0] + 1, pos[1]], [pos[0] - 1, pos[1]]]:
                # print(1,i,len(word),word_inx,curr,word)
                if i[0] >= 0 and i[0] < self.m and i[1] >= 0 and i[1] < self.n:
                    # print(2,i,board[i[0]][i[1]],word,word[word_inx])
                    if i not in used and board[i[0]][i[1]] == word[word_inx]:
                        # print(3,board,word,i,used+[i],curr+board[i[0]][i[1]])
                        helper(board, word, i, [i] + used, curr + board[i[0]][i[1]], word_inx + 1)

        self.m = len(board)
        self.n = len(board[0])

        starting_positions = []
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    starting_positions.append([i, j])
        if len(word) == 1 and starting_positions:
            return True
        for i in starting_positions:
            helper(board, word, i, [i])
            if self.answer:
                return True
        return False

"""
sample 26 ms submission
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        CELL = len(board[0])
        path = set()
        def dfs(x, y, i):
            if i == len(word):
                return True

            if (x,y) in path: return False
            # if board[x][y] == "#": return False
            
            # within matrix
            if x < 0 or y < 0 or x >= ROW or y >= CELL:
                return False
            
            # if current board letter does not match current word letter
            if board[x][y] != word[i]:
                return False
            
            path.add((x,y))
            #temp = board[x][y]
            #board[x][y] = "#"
            
            res = dfs( x+1, y, i+1 ) or dfs( x-1, y, i+1 ) or dfs(x, y-1,  i+1) or dfs(x, y+1, i+1)
            
            #board[x][y] = temp
            path.remove((x,y))
            
            return res

        # Create hash table and store  letter = freq of appearance
        hm_board = {}
        for i in range(ROW):
            for j in range(CELL):
                # get returns value of board[i][j] if exist, otherwise second parm ie 0 will be used.
                hm_board[board[i][j]] = hm_board.get(board[i][j], 0) + 1
        # print(hm_board)


        # construct hashtable from word letter letter = freq of appearance
        hm_word = collections.Counter(word)

        # compare board letter freqs to word letter freqs
        # if board does not have enough letter to makeup the word.. exit.
        for char, freq in hm_word.items():
            # print(char, "=>" , hm_board.get(char, 0), freq)
            if hm_board.get(char, 0) < freq:
                return False


        # check the freqs of the first letter of the world to last
        # if less, reverse word
        # print(hm_word[word[0]], hm_word[word[-1]], word[::-1])
        if hm_word[word[0]] > hm_word[word[-1]]:
            word = word[::-1]

        for x in range(ROW):
            for y in range(CELL):
                if dfs(x, y, 0):
                    return True

        return False
"""