"""
1930. Unique Length-3 Palindromic Subsequences
Medium

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
"""
import string
from collections import defaultdict, Counter

#57%
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cr = Counter(s)
        possible2 = [i for i in cr.keys() if cr[i] > 1]

        l = defaultdict(set)
        for i in range(len(s)):
            l[s[i]].update(possible2)

        d = defaultdict(set)
        cr[s[0]] -= 1
        cl = Counter(s[0])
        for i in range(1, len(s) - 1):
            cr[s[i]] -= 1
            remove = set()
            for j in l[s[i]]:
                if cl[j] and cr[j]:
                    d[s[i]].add(j)
                    remove.add(j)
            for j in remove:
                l[s[i]].remove(j)
            cl[s[i]] += 1

        ans = 0
        for i in d.keys():
            ans += len(d[i])
        return ans


import random
def test_cases():
    #print('"' + "".join(random.choices(["a","b","c"], k=random.randint(3, 10 ** 1))) + '"')
    #print('"' + "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 10 ** 2))) + '"')
    #print('"' + "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 10 ** 3))) + '"')
    #print('"' + "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 10 ** 4))) + '"')
    print('"' + "".join(random.choices(string.ascii_lowercase, k=random.randint(3, 10 ** 5))) + '"')

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.countPalindromicSubsequence(input1)
        print(ans)
        return ans

    assert test("caaacaba") == 4

    for i in range(8):
        test_cases()

"""
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = defaultdict(set)
        for i in range(len(s)):
            left = set(s[:i])
            right = set(s[i+1:])
            both = left & right
            for j in both:
                d[s[i]].add(j)
        ans = 0
        for i in d.keys():
            ans += len(d[i])
        return ans

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #possibilities = itertools.product(string.ascii_lowercase, repeat=2)
        #print(len(list(possibilities)))
        #676
        
        c = Counter(s)
        #possible1 = [c[i] for i in c.keys() if c[i] > 0]
        possible2 = [c[i] for i in c.keys() if c[i] > 1]

        l = defaultdict(set)
        for i in range(len(s)):
            l[s[i]].update(possible2)
        
        d = defaultdict(set)
        for i in range(1,len(s)-1):
            left = set(s[:i])
            right = set(s[i+1:])
            both = left & right & l[s[i]]
            for j in both:
                d[s[i]].add(j)
                
        ans = 0
        for i in d.keys():
            ans += len(d[i])
        return ans
"""