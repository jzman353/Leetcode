#18%
"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        import collections
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        sc.subtract(tc)
        for key,value in sc.items():
            if value != 0:
                return key

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        return Test.findTheDifference(s,t)

    s = "abcd"
    t = "abcde"
    print(test(s,t))
    s = "abcde"
    t = "abcd"
    print(test(s, t))
    s = "abcd"
    t = "abecd"
    print(test(s, t))
    s = "abcd"
    t = "eabcd"
    print(test(s, t))
    s = "abcd"
    t = "abcda"
    print(test(s, t))