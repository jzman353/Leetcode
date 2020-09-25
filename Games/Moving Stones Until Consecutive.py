#30%
"""
1033. Moving Stones Until Consecutive
Easy

Three stones are on a number line at positions a, b, and c.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints.  Formally, let's say the stones are currently at positions x, y, z with x < y < z.  You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]



Example 1:

Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

Example 2:

Input: a = 4, b = 3, c = 2
Output: [0,0]
Explanation: We cannot make any moves.

Example 3:

Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.



Note:

    1 <= a <= 100
    1 <= b <= 100
    1 <= c <= 100
    a != b, b != c, c != a
"""

class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        s = sorted([a,b,c])
        maxx = s[2]
        mid = s[1]
        minn = s[0]
        min_moves = 0
        max_moves = 0
        if mid-minn == 2 or maxx-mid == 2:
            min_test = True
        else:
            min_test = False
        if minn+1!=mid:
            max_moves += mid-minn-1
            min_moves += 1
        if maxx-1!=mid:
            max_moves += maxx-mid-1
            min_moves += 1
        if min_test:
            min_moves = 1
        return [min_moves,max_moves]

if __name__ == '__main__':
    def test(input1, input2,input3):
        Test = Solution()
        print(Test.numMovesStones(input1, input2,input3))

    a,b,c = 1,2,5
    test(a,b,c)
    a, b, c = 4,3,2
    test(a, b, c)
    a, b, c = 3,5,1
    test(a, b, c)

"""
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        
        # sort the elements
        a,b,c = sorted([a,b,c])
    
        # finding left and right gaps
        left = b-a-1
        right = c-b-1
        
        if left == 0 and right == 0:
            return [0,0]
        
        if left == 0 or right == 0:
            return [1, max(right, left)]
        
        if left == 1 or right == 1:
            return [1, left+right]
        
        return [2, left+right]
"""