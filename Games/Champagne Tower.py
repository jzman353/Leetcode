"""
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup (250ml) of champagne.

Then, some champagne is poured in the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)



Example 1:

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champagne to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champagne to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

Example 3:

Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000



Constraints:

    0 <= poured <= 109
    0 <= query_glass <= query_row < 100
"""
"""
#1st strategy: simulation with list
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        #if poured >= 5050:
        #    return 1
        #1000000000

        def recursive(amount, row, glass):
            if self.root[row-1][glass-1] != 1:
                if amount - (1 - self.root[row-1][glass-1]) >= 0:
                    amount -= 1 - self.root[row-1][glass-1]
                    self.root[row-1][glass-1] = 1
                else:
                    self.root[row-1][glass-1] += amount
                    amount = 0
            if row-1 == query_row and glass-1 == query_glass and self.root[query_row][query_glass] == 1:
                return 1
            if amount > 0:
                if len(self.root) < row+1:
                    self.root.append([0 for i in range(row+1)])
                recursive(amount / 2, row + 1, glass)
                recursive(amount/2, row+1, glass+1)


        self.root = [[0]]
        recursive(poured, 1, 1)
        try:
            return self.root[query_row][query_glass]
        except:
            return 0
"""
#2nd strategy: simulation with list and calculation
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        self.root = [[0]*i for i in range(1,101)]
        self.root[0][0] = poured
        for i in range(query_row):
            for j in range(i+1):
                calc = (self.root[i][j]-1)/2
                if calc > 0:
                    self.root[i+1][j] += calc
                    self.root[i + 1][j+1] += calc
        return min(1,self.root[query_row][query_glass])


if __name__ == '__main__':
    def test(input1, input2, input3):
        Test = Solution()
        ans = Test.champagneTower(input1,input2,input3)
        print(ans)
        return ans


    assert test(0, 1, 1) == 0
    assert test(1, 1, 1) == 0
    assert test(2, 1, 1) == 0.5
    assert test(100000009, 33, 17) == 1
    assert test(25, 6, 1) == .1875
    assert test(1000000000, 99, 99) == 0

