"""
#46/83 Time Limit Exceeded
Numbers At Most N Given Digit Set

Given an array of digits, you can write numbers using each digits[i] as many times as we want.  For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.



Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation:
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.

Example 3:

Input: digits = ["7"], n = 8
Output: 1



Constraints:

    1 <= digits.length <= 9
    digits[i].length == 1
    digits[i] is a digit from '1' to '9'.
    All the values in digits are unique.
    1 <= n <= 109
"""
import itertools
import string
class Solution:
    def atMostNGivenDigitSet(self, digits, n: int) -> int:
        def product(*args, repeat=1):
            # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
            # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
            pools = [tuple(pool) for pool in args] * repeat
            result = [[]]
            for pool in pools:
                result = [x + [y] for x in result for y in pool]
            for prod in result:
                yield tuple(prod)
        digits.sort()
        exit = False
        p_list = []
        for d in range(1,len(str(n))+1):
            p = product(digits,repeat = d)
            for i in p:
                temp = ""
                for j in i:
                    if j in string.digits:
                        temp = temp + str(j)
                if int(temp) not in p_list and int(temp) <= n:
                    p_list.append(int(temp))
                elif int(temp) > n:
                    exit = True
                    break
            if exit:
                break
        #print(p_list)
        return len(p_list)

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.atMostNGivenDigitSet(input1,input2)
        print(ans)
        return ans

    assert test(["1","3","5","7"], 100) == 20
    assert test(["1","4","9"], 1000000000) == 29523
    assert test(["1","2","3","4","5","6","7","8","9"], 91243) == 59979


"""
Dynamic Programming + Counting
class Solution:
    def atMostNGivenDigitSet(self, D, N):
        S = str(N)
        K = len(S) #Used to find max number of digits we could possibly need
        dp = [0] * K + [1] 
        # dp[i] = total number of valid integers if N was "N[i:]"

        for i in xrange(K-1, -1, -1):
            # Compute dp[i]

            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K-i-1)
                elif d == S[i]: #If the digit is equal to the same place in N, add the possibilities in the next digits
                    dp[i] += dp[i+1]
                #Ignore if the digit is higher than the same place in N because those are accounted for in dp[i] += len(D) ** (K-i-1)

        return dp[0] + sum(len(D) ** i for i in xrange(1, K))
"""