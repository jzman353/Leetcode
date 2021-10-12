"""
884. Uncommon Words from Two Sentences
Easy

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
"""
#88%
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + " " + s2
        c = Counter(s.split())
        answer = []
        for i in c:
            if c[i] == 1:
                answer.append(i)

        return answer

#22%
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1s = Counter(s1.split())
        s2s = Counter(s2.split())
        answer = []
        for i in s1s:
            if s1s[i] > 1:
                if i in s2s.keys():
                    del s2s[i]
            elif i not in s2s.keys():
                answer.append(i)
            else:
                del s2s[i]

        for i in s2s:
            if s2s[i] == 1:
                answer.append(i)

        return answer