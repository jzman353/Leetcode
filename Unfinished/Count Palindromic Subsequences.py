"""
2484. Count Palindromic Subsequences
Hard

Given a string of digits s, return the number of palindromic subsequences of s having length 5. Since the answer may be very large, return it modulo 109 + 7.

Note:

A string is palindromic if it reads the same forward and backward.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:

Input: s = "103301"
Output: 2
Explanation:
There are 6 possible subsequences of length 5: "10330","10331","10301","10301","13301","03301".
Two of them (both equal to "10301") are palindromic.
Example 2:

Input: s = "0000000"
Output: 21
Explanation: All 21 subsequences are "00000", which is palindromic.
Example 3:

Input: s = "9999900000"
Output: 2
Explanation: The only two palindromic subsequences are "99999" and "00000".

Constraints:

1 <= s.length <= 104
s consists of digits.
"""

import bisect
import collections
import string

#TLE between 10**@ and 10**3
"""
The algorithm could be more efficient if we retained the number of possible palindromic subsequences for each i so that 
it does not have to be recalculated for every i
"""
class Solution:
    def countPalindromes(self, s: str) -> int:
        ans = 0

        d = collections.defaultdict(list)

        for i, digit in enumerate(s):
            d[digit].append(i)

        for i in range(2, len(s) - 2):
            for j in range(10):
                idx = bisect.bisect_left(d[str(j)], i)
                stackjl = d[str(j)][:idx]
                if str(j) == s[i]:
                    idx += 1
                stackjr = d[str(j)][idx:]

                for k in range(10):
                    idx = bisect.bisect_left(d[str(k)], i)
                    stackkl = d[str(k)][:idx]
                    if str(k) == s[i]:
                        idx += 1
                    stackkr = d[str(k)][idx:]

                    left = 0
                    tempjl = stackjl[:]
                    while tempjl:
                        jl = tempjl.pop()
                        idx = bisect.bisect_left(stackkl, jl)
                        if j == k:
                            idx += 1
                        kl = len(stackkl) - idx
                        left += kl

                    right = 0
                    tempjr = stackjr[:]
                    while tempjr:
                        jr = tempjr.pop()
                        kr = bisect.bisect_left(stackkr, jr)
                        right += kr
                    ans += left * right
        return ans

import random
def testCases():
    #print('"'+"".join(random.choices(string.digits, k=random.randint(1, 10 ** 1)))+'"')
    #print('"'+"".join(random.choices(string.digits, k=random.randint(1, 10 ** 2)))+'"')
    #TLE @ level 3
    print('"'+"".join(random.choices(string.digits, k=random.randint(10 ** 2, 10 ** 3)))+'"')
    #print('"'+"".join(random.choices(string.digits, k=random.randint(1, 10 ** 4)))+'"')

for i in range(8):
    testCases()

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.countPalindromes(input1)
        print(ans)
        return ans

    assert test("103301") == 2
    assert test("0000000") == 21
    assert test("9999900000") == 2

"""
    def countPalindromes(self, s: str) -> int:
        #re.finditer is not finding all of the matches

        import re
        s = "0000000"
        ans = 0

        for i in range(2,len(s)-2):
            left = s[:i]
            right = s[i+1:][::-1]
            for j in range(10):
                for k in range(10):
                    matches = re.finditer(r'(?=([{}][0-9]*[{}]))'.format(j,k), left)
                    resl = [match.group(1) for match in matches]
                    matches = re.finditer(r'(?=([{}][0-9]*[{}]))'.format(j, k), right)
                    resr = [match.group(1) for match in matches]
                    ans += len(resl)*len(resr)
                    #results = [match.group(1) for match in matches]
                    if j == 0 and k == 0:
                        print(i,j,k,ans)
                        print(resl,resr)

        print(ans)
"""