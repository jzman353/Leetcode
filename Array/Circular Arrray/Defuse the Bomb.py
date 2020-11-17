"""
60%
1652. Defuse the Bomb
Easy

You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

    If k > 0, replace the ith number with the sum of the next k numbers.
    If k < 0, replace the ith number with the sum of the previous k numbers.
    If k == 0, replace the ith number with 0.

As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0.

Example 3:

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

Constraints:

    n == code.length
    1 <= n <= 100
    1 <= code[i] <= 100
    -(n - 1) <= k <= n - 1
"""

class Solution:
    def decrypt(self, code, k: int):
        length = len(code)
        code_copy = [0 for _ in range(length)]
        if k == 0:
            return code_copy
        if k > 0:
            for i in range(len(code)):
                one = (i + 1) % length
                two = (i + 1 + k) % length
                if one < two:
                    summ = 0
                    for j in range(one, two):
                        summ += code[j]
                    code_copy[i] = summ
                else:
                    summ = 0
                    for j in range(one, length):
                        summ += code[j]
                    for j in range(0, two):
                        summ += code[j]
                    code_copy[i] = summ
        else:
            for i in range(len(code)):
                one = (i)
                two = (i + k)
                if one > two:
                    summ = 0
                    for j in range(two, one):
                        summ += code[j]
                    code_copy[i] = summ
                else:
                    summ = 0
                    for j in range(two, length):
                        summ += code[j]
                    for j in range(0, one):
                        summ += code[j]
                    code_copy[i] = summ
        return code_copy

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.decrypt(input1,input2)
        print(ans)
        return ans


    assert test([5,7,1,4], 3) == [12,10,16,13]
    assert test([5, 7, 1, 4], 0) == [0,0,0,0]
    assert test([2, 4, 9, 3], -2) == [12, 5, 6, 13]

"""
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k >0:
            ans[0] = sum(code[1:k+1])
            for i in range(1,n):
                ans[i]= ans[i-1] + code[(i+k)% n] - code[i]
        if k <0:
            return self.decrypt(code[::-1], -k)[::-1]
        return ans
"""