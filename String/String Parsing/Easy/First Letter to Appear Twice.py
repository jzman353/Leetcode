"""
2351. First Letter to Appear Twice
Easy

Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.

Example 1:

Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.
Example 2:

Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters.
s has at least one repeated letter.
"""

#86%
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = defaultdict(int)
        for i in s:
            if d[i]:
                return i
            d[i] += 1

"""
Use a string instead of a dictionary to track
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l=''
        for i in range(len(s)):
            if s[i] in l:
                return s[i]
            else:
                l=l+s[i]
"""

"""
import random
import collections
import string
def test_cases():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2,100)))

results = 0
while results < 8:
    test = test_cases()
    c = collections.Counter(test)
    if c.most_common(1)[0][1] > 1:
        results += 1
        print('"'+test+'"')
"""