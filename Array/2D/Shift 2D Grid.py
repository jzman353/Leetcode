"""
1260. Shift 2D Grid
Easy

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

    Element at grid[i][j] moves to grid[i][j + 1].
    Element at grid[i][n - 1] moves to grid[i + 1][0].
    Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying shift operation k times.



Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:

Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m <= 50
    1 <= n <= 50
    -1000 <= grid[i][j] <= 1000
    0 <= k <= 100
"""
#78%
class Solution:
    def shiftGrid(self, grid, k: int):
        n = len(grid)
        m = len(grid[0])
        #Don't rotate the entire grid
        if k >= m*n:
            k = k % (m*n)
        # Rotate rows first
        if k > m:
            for i in range(k//m):
                grid.insert(0,grid[-1])
                grid.pop()
                k -= m
        #Rotate columns second
        temp = []
        for i in range(k):
            temp.append(grid[-1].pop())
        temp_next = []
        for i in range(n):
            for j in range(len(temp)):
                grid[i].insert(0,temp[j])
                temp_next.append(grid[i].pop())
            temp = temp_next
            temp_next = []
        grid[-1].extend(temp[::-1])
        return grid

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.shiftGrid(input1,input2)
        print(ans)
        return ans

    assert test([[1,2,3],[4,5,6],[7,8,9]], 1) == [[9,1,2],[3,4,5],[6,7,8]]
    assert test([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4) == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    assert test([[1,2,3],[4,5,6],[7,8,9]], 9) == [[1,2,3],[4,5,6],[7,8,9]]
    assert test([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10) == [[9,1,2],[3,4,5],[6,7,8]]
    assert test([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 100) == [[9,10,11,12],[1,2,3,4],[5,6,7,8]]
    assert test([[1],[2],[3],[4],[7],[6],[5]], 23) == [[6], [5], [1], [2], [3], [4], [7]]
    assert test([[-353,853,839,122,-337],[819,356,116,0,791],[-516,-502,-681,-427,-314],[-386,-400,597,740,836],[129,598,40,-875,-968],[495,-604,79,414,-104],[237,121,211,4,677],[-712,351,-947,-203,361]], 7) == [[4,677,-712,351,-947],[-203,361,-353,853,839],[122,-337,819,356,116],[0,791,-516,-502,-681],[-427,-314,-386,-400,597],[740,836,129,598,40],[-875,-968,495,-604,79],[414,-104,237,121,211]]



