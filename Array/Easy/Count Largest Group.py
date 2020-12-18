"""
1399. Count Largest Group
Easy

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

Return how many groups have the largest size.

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Example 3:

Input: n = 15
Output: 6

Example 4:

Input: n = 24
Output: 5

Constraints:
    1 <= n <= 10^4
"""
#45%
import collections
class Solution:
    def countLargestGroup(self, n: int) -> int:
        c = collections.Counter()
        summ = 0
        for i in range(1,n+1):
            for j in str(i):
                summ += int(j)
            c[summ] += 1
            summ = 0
        maxx = c.most_common(1)[0][1]
        count = 0
        for i in c.most_common():
            if i[1] == maxx:
                count += 1
            else:
                return count
        return count

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.countLargestGroup(input1)
        print(ans)
        return ans

    assert test(13) == 4
    assert test(2) == 2
    assert test(15) == 6
    assert test(24) == 5