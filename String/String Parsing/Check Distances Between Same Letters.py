"""
2399. Check Distances Between Same Letters
Easy

You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.

Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.

Return true if s is a well-spaced string, otherwise return false.

Example 1:

Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: true
Explanation:
- 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
- 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
- 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
Return true because s is a well-spaced string.
Example 2:

Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: false
Explanation:
- 'a' appears at indices 0 and 1 so there are zero letters between them.
Because distance[0] = 1, s is not a well-spaced string.

Constraints:

2 <= s.length <= 52
s consists only of lowercase English letters.
Each letter appears in s exactly twice.
distance.length == 26
0 <= distance[i] <= 50
"""
import string

"""
#36%
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = defaultdict(list)
        for i, letter in enumerate(s):
            l = ord(letter)-97
            d[l].append(i)
            if len(d[l]) == 2:
                d[l] = d[l][1]-d[l][0]-1

        for i in d.keys():
            if d[i]!=distance[i]:
                return False
        return True

Sample 30 ms submission

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = len(s := list(s))
        for i, ch in enumerate(s):
            if ch and ((m := i + distance[ord(ch)-97] + 1) >= n or s[m] != ch):
                return False
            s[m] = 0

        return True
"""

import random
import collections
def test_cases():
    n = random.randint(1, 26)
    letters = random.sample(string.ascii_lowercase,k=n)*2
    test = "".join(random.sample(letters,k=n*2))
    print('"'+test+'"')
    d = collections.defaultdict(list)
    for i, letter in enumerate(test):
        d[ord(letter) - 97].append(i)

    for i in d.keys():
        d[i] = d[i][1] - d[i][0] - 1

    distance = [0 for i in range(26)]

    for i in range(26):
        if i in d.keys():
            distance[i] = d[i]

    print(distance)

for i in range(8):
    test_cases()