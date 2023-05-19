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

class Solution:
    def countPalindromes(self, s: str) -> int:
        ans = 0
        length = len(s)
        for i in range(length):
            left = s[:i]
            right = s[i+1:][::-1]
            print(i, s[i])
            print("left: "+str(left))
            print("right: "+str(right))
            print("ans: "+str(ans))
            for j in range(10):
                try:
                    idxl1 = left.index(str(j))
                    idxr1 = right.index(str(j))
                except:
                    continue
                for k in range(10):
                    try:
                        idxl2 = left[idxl1+1:].index(str(k))
                        idxr2 = right[idxr1+1:].index(str(k))
                        ans += 1
                        ans = ans % (10**9 +7)
                    except:
                        continue
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.countPalindromes(input1)
        print(ans)
        return ans

    assert test("103301") == 2
    assert test("0000000") == 21
    assert test("9999900000") == 2