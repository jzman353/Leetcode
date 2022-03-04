"""
935. Knight Dialer
Medium

The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

Example 1:

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
Example 2:

Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
Example 3:

Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.

Constraints:

1 <= n <= 5000

**************SEE Knight_Dialer.JPG****************
"""
#80%
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        d_odd = {}
        d_even = {}
        d_odd[0] = 1
        d_odd[46] = 2
        d_odd[28] = 2
        d_odd[1379] = 4

        def update(dict1,dict2):
            self.answer = 0
            dict1[0] = dict2[46]
            dict1[1379] = dict2[46]*2+dict2[28]*2
            dict1[46] = dict2[1379]+dict2[0]*2
            dict1[28] = dict2[1379]

            for i in [0,1379,46,28]:
                self.answer += dict1[i]

        while n > 1:
            if not d_even:
                update(d_even,d_odd)
                d_odd = defaultdict(int)
            else:
                update(d_odd,d_even)
                d_even = defaultdict(int)
            n -= 1

        return self.answer%(10**9+7)
"""
#80%
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        d_odd = defaultdict(int)
        d_even = defaultdict(int)
        for i in [4,0,6]:
            d_odd[i] += 1
        for i in [3,8,1]:
            d_odd[i] += 2

        def update(dict1,dict2):
            self.answer = 0
            dict1[0] = dict2[4]+dict2[6]
            dict1[1] = dict2[6]*2+dict2[8]
            dict1[3] = dict2[4]*2+dict2[8]
            dict1[4] = dict2[3]+dict2[0]
            dict1[6] = dict2[1]+dict2[0]
            dict1[8] = dict2[1]+dict2[3]

            for i in [0,1,3,4,6,8]:
                self.answer += dict1[i]

        while n > 1:
            if not d_even:
                update(d_even,d_odd)
                d_odd = defaultdict(int)
            else:
                update(d_odd,d_even)
                d_even = defaultdict(int)
            n -= 1

        return self.answer%(10**9+7)
"""
"""
#70%
from collections import defaultdict

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        d_odd = defaultdict(int)
        d_even = defaultdict(int)
        for i in [0,1,2,3,4,6,7,8,9]:
            d_odd[i] += 1

        def update(dict1,dict2):
            self.answer = 0
            dict1[0] = dict2[4]+dict2[6]
            dict1[1] = dict2[6]+dict2[8]
            dict1[2] = dict2[7]+dict2[9]
            dict1[3] = dict2[4]+dict2[8]
            dict1[4] = dict2[3]+dict2[9]+dict2[0]
            dict1[6] = dict2[1]+dict2[7]+dict2[0]
            dict1[7] = dict2[2]+dict2[6]
            dict1[8] = dict2[1]+dict2[3]
            dict1[9] = dict2[4]+dict2[2]

            for i in [0,1,2,3,4,6,7,8,9]:
                self.answer += dict1[i]

        while n > 1:
            if not d_even:
                update(d_even,d_odd)
                d_odd = defaultdict(int)
            else:
                update(d_odd,d_even)
                d_even = defaultdict(int)
            n -= 1

        return self.answer%(10**9+7)
"""
"""
sample 53 ms submission
N = 10 ** 9 + 7


@cache
def distinct(n):
    if n == 1:
        return [1, 2, 4, 2]
    A, B, C, D = distinct(n - 1)
    return B, (2 * A + C) % N, (2 * B + 2 * D) % N, C


class Solution:
    def knightDialer(self, n: int) -> int:
        return (sum(distinct(n)) + (n == 1)) % N
"""
if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.knightDialer(input1)
        print(ans)
        return ans

    assert test(1) == 10
    assert test(2) == 20
    assert test(3) == 46
    assert test(4) == 104
    assert test(5) == 240
    assert test(6) == 544
    assert test(7) == 1256
    assert test(8) == 2848
    assert test(9) == 6576
    assert test(10) == 14912