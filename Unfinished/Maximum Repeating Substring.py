"""
1668. Maximum Repeating Substring
Easy
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.



Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
Example 2:

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
Example 3:

Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".


Constraints:

1 <= sequence.length <= 100
1 <= word.length <= 100
sequence and word contains only lowercase English letters.
"""

import re
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        w = "("+word+")+"
        Regex = re.compile(w)
        #mo1 = Regex.search(sequence)
        mo1 = Regex.findall(sequence)
        if mo1:
            print(mo1)
            print(mo1.group())
            return mo1.group().count(word)
        else:
            return 0

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.maxRepeating(input1,input2)
        print(ans)
        return ans

    assert test("ababc", "ab") == 2
    assert test("ababc", "ba") == 1
    assert test("ababc", "ac") == 0
    assert test("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba") == 5
