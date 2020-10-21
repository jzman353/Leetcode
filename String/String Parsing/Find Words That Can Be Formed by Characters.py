"""
13%
1160. Find Words That Can Be Formed by Characters
Easy

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.



Note:

    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    All strings contain lowercase English letters only.
"""
import collections
class Solution:
    def countCharacters(self, words, chars: str) -> int:
        summ = 0
        for i in words:
            c = collections.Counter(chars)
            cc = collections.Counter(i)
            c.subtract(cc)
            if c.most_common()[:-1-1:-1][0][1] >= 0:
                summ += len(i)
        return summ

"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        pre_compiled_counter = Counter(chars)
        output = 0 
        for word in words : 
            if Counter(word) - pre_compiled_counter == Counter() :
                output = output + len(word)
        return output
"""