"""
#55%
1390. Four Divisors
Medium

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.



Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.



Constraints:

    1 <= nums.length <= 10^4
    1 <= nums[i] <= 10^5
"""

import math
class Solution:
    def sumFourDivisors(self, nums) -> int:
        d = {}
        ans = 0
        for i in nums:
            div = []
            if i in d.keys():
                ans += d[i]
                continue
            div.append(1)
            div.append(i)
            for j in range(2,math.ceil(i**(1/2))+1):
                if i%j==0:
                    if j not in div:
                        div.append(j)
                    if i // j not in div:
                        div.append(i // j)
            if len(div) == 4:
                temp = sum(div)
                ans += temp
                d[i] = temp
            else:
                d[i] = 0
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.sumFourDivisors(input1)
        print(ans)
        return ans

    assert test([21,4,7]) == 32
    assert test([21, 21]) == 64
    assert test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45