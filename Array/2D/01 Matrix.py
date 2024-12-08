"""
542. 01 Matrix
Attempted
Medium
Topics
Companies
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
#TLE
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ones = set()
        zeros = set()
        y_len = len(mat)
        x_len = len(mat[0])
        for m in range(y_len):
            for n in range(x_len):
                if mat[m][n] == 1:
                    ones.add((n,m))
                elif mat[m][n] == 0:
                    zeros.add((n,m))
        res = [[0 for i in range(x_len)] for j in range(y_len)]
        #optimize later with a spiral pattern until a 0 is found
        for i in ones:
            min_distance = math.inf
            for j in zeros:
                y_distance = abs(j[0]-i[0])
                x_distance = abs(j[1]-i[1])
                min_distance = min(min_distance, x_distance+y_distance)
            res[i[1]][i[0]] = min_distance
        return res

# Chat gpt helped
#54%
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        res = [[float("inf") for i in range(cols)] for j in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            y, x = queue.popleft()
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols and res[ny][nx] > res[y][x] + 1:
                    res[ny][nx] = res[y][x] + 1
                    queue.append((ny, nx))

        return res

"""
Explanation
Initialization:

Start by creating a result matrix res filled with float('inf').
Add all 0 cells to a queue because their distances are already known.
BFS Traversal:

For each cell in the queue, explore its neighbors in four directions.
If a neighbor cell's current distance is greater than the distance of the current cell + 1, update the neighbor's distance and add it to the queue.
Propagation:

BFS ensures that the shortest distance is calculated in increasing order.
Complexity
Time Complexity: 
O(m⋅n), where m and n are the dimensions of the matrix. Each cell is processed once.
Space Complexity: 
O(m⋅n) for the result matrix and queue.
This approach avoids unnecessary recalculations and is efficient for large matrices.

there is a specific reason we use popleft() instead of pop() when implementing Breadth-First Search (BFS) with a deque.

Key Difference:
popleft() removes an element from the front of the deque (queue behavior).
pop() removes an element from the end of the deque (stack behavior).
Why popleft() for BFS?
BFS explores nodes layer by layer, ensuring that all nodes at a given distance are processed before moving to nodes at the next distance. This behavior requires a queue, where:

The earliest-added (oldest) elements are processed first (FIFO: First-In-First-Out).
Using popleft() ensures the order of processing aligns with the BFS logic.
If you use pop() instead, the deque behaves like a stack (LIFO: Last-In-First-Out), which is how Depth-First Search (DFS) works. This would fundamentally change the traversal order, breaking BFS's layer-by-layer exploration.

Efficiency of popleft() in deque
The deque is optimized for O(1) popleft() operations, making it a natural fit for BFS.
If you were to use a list and emulate popleft() by removing the first element (list.pop(0)), it would have O(n) complexity because it shifts all subsequent elements, leading to performance degradation.
TL;DR
We use popleft() to maintain BFS's correct traversal order and ensure efficiency with O(1) deque operations.
"""

"""
Another good solution:
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        self.m = len(mat)
        self.n = len(mat[0])
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.result = [[0 for col in range(self.n)] for row in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == 1:
                    self.result[i][j] = self.dfsHelper(mat, i, j)

        return self.result


    def dfsHelper(self, mat: list[list[int]], i: int, j: int):
        if i > 0 and mat[i-1][j] == 0: return 1 # top
        if i < self.m -1 and mat[i+1][j] == 0: return 1  # down
        if j > 0 and mat[i][j-1] == 0: return 1  # left
        if j < self.n -1 and mat[i][j+1] == 0: return 1  # right

        top = 9999; left = 9999; bottom = 9999; right = 9999

        if i > 0 and self.result[i-1][j] != 0:
            top = self.result[i-1][j]

        if j > 0 and self.result[i][j-1] != 0:
            left = self.result[i][j-1]

        if j < self.n -1:
            if self.result[i][j+1] == 0:
                self.result[i][j+1] = self.dfsHelper(mat, i, j+1)
            right = self.result[i][j+1]

        if i < self.m - 1:
            if self.result[i+1][j] == 0:
                self.result[i+1][j] = self.dfsHelper(mat, i+1, j)
            bottom = self.result[i+1][j]

        return 1 + min(top, min(left, min(bottom, right)))
"""