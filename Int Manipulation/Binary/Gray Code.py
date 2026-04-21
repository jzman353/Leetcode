"""
89. Gray Code
Medium

An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit
Example 2:

Input: n = 1
Output: [0,1]

Constraints:

1 <= n <= 16
100%
"""


class Solution:
    def grayCode(self, n: int) -> list[int]:
        ans = [0]

        for i in range(1, n + 1):
            for j in range(len(ans) - 1, -1, -1):
                ans.append(ans[j] | (1 << (i - 1)))

        return list(ans)


"""
class Solution:
    def grayCode(self, n: int) -> list[int]:
        ans = [0, 1]

        def adjust_leading_zeros(s, digits):
            return '0'*(digits-1-len(s))+s

        for i in range(2, n + 1):
            reversed_ans = ans[::-1]
            for j in reversed_ans:
                ans.append(int('1' + adjust_leading_zeros(str(bin(j))[2:], i),2))

        return list(ans)
"""


if __name__ == '__main__':
    def is_valid_gray_code(result, n):
        # correct length
        if len(result) != 2 ** n:
            return False, "wrong length"
        # all values in range [0, 2^n - 1]
        if not all(0 <= x <= 2 ** n - 1 for x in result):
            return False, "value out of range"
        # no duplicates
        if len(set(result)) != len(result):
            return False, "duplicate values"
        # first element is 0
        if result[0] != 0:
            return False, "first element not 0"

        # adjacent pairs differ by exactly one bit
        def one_bit_diff(a, b):
            return (a ^ b) & ((a ^ b) - 1) == 0 and a != b

        for i in range(len(result) - 1):
            if not one_bit_diff(result[i], result[i + 1]):
                return False, f"adjacent pair ({result[i]},{result[i + 1]}) differ by more than one bit"
        # first and last differ by exactly one bit
        if not one_bit_diff(result[0], result[-1]):
            return False, "first and last don't differ by one bit"
        return True, "ok"


    def test(n):
        result = Solution().grayCode(n)
        valid, msg = is_valid_gray_code(result, n)
        assert valid, f"n={n} failed: {msg}, got {result}"
        return result


    # n=1: only 2 elements [0,1]
    test(1)

    # n=2: 4 elements, example from problem
    test(2)

    # n=3: 8 elements
    test(3)

    # n=4: 16 elements
    test(4)

    # n=5: 32 elements
    test(5)

    # all powers of 2 up to n=16
    for n in range(1, 17):
        test(n)

    # return type check
    assert isinstance(test(1), list), "should return a list"
    assert isinstance(test(1)[0], int), "elements should be ints"

    # idempotency
    assert is_valid_gray_code(test(3), 3)[0] == True
    assert is_valid_gray_code(test(3), 3)[0] == True

    print("All tests passed!")