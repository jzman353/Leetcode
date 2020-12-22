"""
413. Arithmetic Slices
Medium

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
#39%
class Solution:
    def sumsum(self, n):
        res = 0
        for i in range(1, n + 1):
            res += i
        return res

    def numberOfArithmeticSlices(self, A) -> int:
        if not A or len(A) == 1:
            return 0
        diff = A[1] - A[0]
        count = 0
        ans = 0
        for i in range(1, len(A) - 1):
            if A[i + 1] - A[i] == diff:
                count += 1
            else:
                if count >= 1:
                    ans += self.sumsum(count)
                count = 0
                diff = A[i + 1] - A[i]
        if count >= 1:
            ans += self.sumsum(count)
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.numberOfArithmeticSlices(input1)
        print(ans)
        return ans

    assert test([1, 2, 3, 4]) == 3
    assert test([]) == 0
    assert test([1]) == 0
    assert test([1,2,3]) == 1

"""
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        
        dp_list = [0] * (len(A)-1)
        j = 1
        for i in range(1,len(A)-1):
            if (A[i] - A[i-1]) == (A[i+1]-A[i]):
                dp_list[i] = (dp_list[i-1]+j)
                j+= 1
            else:
                dp_list[i] = dp_list[i-1]
                j = 1
        print(dp_list)
        return dp_list[-1]
"""