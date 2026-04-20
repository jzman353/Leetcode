"""
279. Perfect Squares
Medium

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:

1 <= n <= 104
"""
"""
#Without Dynamic Programming
import bisect

class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961,1024,1089,1156,1225,1296,1369,1444,1521,1600,1681,1764,1849,1936,2025,2116,2209,2304,2401,2500,2601,2704,2809,2916,3025,3136,3249,3364,3481,3600,3721,3844,3969,4096,4225,4356,4489,4624,4761,4900,5041,5184,5329,5476,5625,5776,5929,6084,6241,6400,6561,6724,6889,7056,7225,7396,7569,7744,7921,8100,8281,8464,8649,8836,9025,9216,9409,9604,9801,10000]

        self.min_count = n
        def helper(curr, count, perfect_squares):
            if count < self.min_count:
                if curr == 0:
                    self.min_count = count
                    return
                reduced_perfect_squares = perfect_squares[:bisect.bisect_right(perfect_squares, curr)]
                for i in reduced_perfect_squares[::-1]:
                    helper(curr-i, count+1, reduced_perfect_squares)

        helper(n, 0, perfect_squares)
        return self.min_count
"""

import math
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [i*i for i in range(1, int(n**0.5)+1)]

        dp = [0,1]
        for i in range(2, n+1):
            minn = float('inf')
            for square in perfect_squares:
                if square > i:
                    break
                minn = min(minn, dp[i-square]+1)
            dp.append(minn)
        return dp[-1]

"""
Lagrange's four-square theorem — a pure math approach. It states any number can be expressed as at most 4 perfect squares, so the answer is always 1, 2, 3, or 4. You can check each case mathematically in O(√n) and skip DP entirely. This is the fastest possible solution but requires knowing the theorem.
Answer is 1: n itself is a perfect square.
Answer is 4: Legendre's three-square theorem states any number of the form 4^a(8b+7) requires exactly 4 squares. That's why the code divides out all factors of 4 first, then checks if remainder is 7 mod 8.
Answer is 2: Try every i up to √n and check if n - i² is also a perfect square. If so, n = i² + j².
Answer is 3: If none of the above, it must be 3 by elimination — the theorem guarantees 4 is the maximum ever needed.
The cleverness is in the ordering — it rules out 1, 4, and 2 in O(√n), and 3 requires no check at all. Your DP solution is O(n√n), so this is significantly faster, but you'd never be expected to know this theorem in an interview!

class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(x: int) -> bool:
            r = int(x ** 0.5)
            return r * r == x

        
        if is_square(n):
            return 1

        
        while n % 4 == 0:
            n //= 4

        
        if n % 8 == 7:
            return 4

        
        i = 1
        while i * i <= n:
            if is_square(n - i * i):
                return 2
            i += 1

        
        return 3
"""

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.numSquares(input1)
        print(ans)
        return ans

    assert test(1) == 1    # 1 = 1
    assert test(2) == 2    # 2 = 1+1
    assert test(3) == 3    # 3 = 1+1+1
    assert test(4) == 1    # 4 = 4
    assert test(12) == 3   # 12 = 4+4+4
    assert test(13) == 2   # 13 = 4+9
    assert test(9) == 1    # perfect square itself
    assert test(11) == 3   # 11 = 9+1+1
    assert test(100) == 1  # 100 = 10^2
    assert test(99) == 3   # 99 = 81+9+9
    print("All tests passed!")