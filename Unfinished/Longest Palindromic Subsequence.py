"""
516. Longest Palindromic Subsequence
Medium

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""
import collections
import string
from itertools import chain


#TLE ["a","b","c"] 10-100 chars
#

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def check_palindrome(string1):
            return string1 == string1[::-1]

        def helper(left, right, res):
            min_length = min(len(left), len(right))
            if res + 2*min_length <= self.maxx:
                return

            for i in range(min_length):
                if left[i] == right[i]:
                    res += 2
                    self.maxx = max(self.maxx, res)
                else:
                    helper(left[i + 1:], right[i:], res)
                    helper(left[i:], right[i + 1:], res)

        c = collections.Counter(s)
        self.maxx = c.most_common(1)[0][1]

        left_flipped = list(range(len(s) // 2))[::-1]
        right = list(range(len(s) // 2, len(s)))
        order = list(chain.from_iterable(zip(left_flipped, right)))
        if len(s) % 2 != 0:
            order.append(right[-1])

        for i in order:
            res = 1
            left = s[:i]
            right = s[i + 1:]
            left = [x for x in left if x in right]
            right = [x for x in right if x in left][::-1]
            helper(left, right, res)
            if i != len(s) - 1 and s[i] == s[i + 1]:
                res = 2
                self.maxx = max(self.maxx, 2)
                left = s[:i]
                right = s[i + 2:]
                left = [x for x in left if x in right]
                right = [x for x in right if x in left][::-1]
                helper(left, right, res)

        return self.maxx

import random
def testCases():
    #print('"' + "".join(random.choices(["a","b","c"], k=random.randint(1, 10))) + '"')
    #print('"' + "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 10))) + '"')
    print('"' + "".join(random.choices(["a","b","c"], k=random.randint(10, 100))) + '"')
    #print('"' + "".join(random.choices(string.ascii_lowercase, k=random.randint(10, 100))) + '"')
    #print('"'+"".join(random.choices(string.ascii_lowercase,k=random.randint(100,1000)))+'"')

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.longestPalindromeSubseq(input1)
        print(ans)
        return ans

    assert test("bbbab") == 4
    assert test("cbbd") == 2
    assert test("cbbbcbcacc") == 6

    for i in range(8):
        testCases()

"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def check_palindrome(string1):
            return string1 == string1[::-1]

        def helper(left, right, res):
            #print(self.seen)
            if (tuple(left), tuple(right)) not in self.seen.keys() or (tuple(left), tuple(right)) in self.seen.keys() and res > self.seen[(tuple(left), tuple(right))]:
                self.seen[(tuple(left), tuple(right))] = res
            else:
                return
            min_length = min(len(left), len(right))
            if res + 2*min_length <= self.maxx:
                return

            for i in range(min_length):
                if left[i] == right[i]:
                    res += 2
                    self.maxx = max(self.maxx, res)
                else:
                    helper(left[i + 1:], right[i:], res)
                    helper(left[i:], right[i + 1:], res)

        c = Counter(s)
        self.maxx = c.most_common(1)[0][1]
        self.seen = {}

        left_flipped = list(range(len(s)//2))[::-1]
        right = list(range(len(s)//2,len(s)))
        order = list(chain.from_iterable(zip(left_flipped, right)))
        if len(s) % 2 != 0:
            order.append(right[-1])

        count = 0
        while count < len(order):
            i = order[count]
            res = 1
            while i != len(s) - 1 and s[i] == s[i + 1]:
                res += 1
                count += 1
                self.maxx = max(self.maxx, res)
            left = s[:i]
            right = s[i + 2:]
            left = [x for x in left if x in right]
            right = [x for x in right if x in left][::-1]
            helper(left, right, res)
            count += 1

        return self.maxx
"""