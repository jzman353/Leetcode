"""
59. Spiral Matrix II
Medium

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 20
"""
#14%
class Solution:
    def generateMatrix(self, n: int):
        mat = [[0 for i in range(n)] for j in range(n)]
        counter = 1
        pos = [0,0]
        left = 0
        right = n-1
        top = 0
        bot = n-1
        while left <= right and bot >= top:
            #GoRight
            while pos[1] < right:
                mat[pos[0]][pos[1]] = counter
                pos[1] += 1
                counter += 1
            top += 1
            #GoDown
            if left <= right and bot >= top:
                while pos[0] < bot:
                    mat[pos[0]][pos[1]] = counter
                    pos[0] += 1
                    counter += 1
                right -= 1
            #GoLeft
            if left <= right and bot >= top:
                while pos[1] > left:
                    mat[pos[0]][pos[1]] = counter
                    pos[1] -= 1
                    counter += 1
                bot -= 1
            #GoUp
            if left <= right and bot >= top:
                while pos[0] > top:
                    mat[pos[0]][pos[1]] = counter
                    pos[0] -= 1
                    counter += 1
                left += 1
        mat[pos[0]][pos[1]] = counter
        return mat

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.generateMatrix(input1)
        print(ans)
        return ans

    assert test(3) == [[1,2,3],[8,9,4],[7,6,5]]
    assert test(1) == [[1]]

"""
sample 12 ms submission
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr=[[0 for _ in range(n)] for i in range(n)]
        l,r=0,n-1
        u,d=0,n-1
        c=0
        while l<=r or u<=d:
            for i in range(l,r+1):
                c+=1
                arr[u][i]=c
            u+=1
            for i in range(u,d+1):
                c+=1
                arr[i][r]=c
            r-=1
            for i in range(r,l-1,-1):
                c+=1
                arr[d][i]=c
            d-=1
            for i in range(d,u-1,-1):
                c+=1
                arr[i][l]=c
            l+=1
        return arr
"""