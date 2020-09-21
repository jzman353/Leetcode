#74%
"""
Minimum Cost to Move Chips to The Same Position (Easy)

We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

    position[i] + 2 or position[i] - 2 with cost = 0.
    position[i] + 1 or position[i] - 1 with cost = 1.

Return the minimum cost needed to move all the chips to the same position.
"""


class Solution:
    def minCostToMoveChips(self, position) -> int:
        odd_num = even_num = 0
        for i in position:
            if i % 2 == 0:
                even_num += 1
            else:
                odd_num += 1
        return min(even_num,odd_num)

if __name__ == '__main__':
    def test(input):
        Test = Solution()
        ans = Test.minCostToMoveChips(input)
        print(ans)

    position = [1,2,3]  #1 1
    test(position)
    position = [2,2,2,3,3] #2 2
    test(position)

    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))

""" This solution doesn't have if statements
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # n = len(position)
        # return n//2
        ans1 = 0
        ans2 = 0
        for num in position:
            ans1 += abs(num%2-1)
            ans2 += num%2
        return min(ans1, ans2)
"""