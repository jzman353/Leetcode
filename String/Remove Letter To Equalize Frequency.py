"""
2423. Remove Letter To Equalize Frequency
Easy

You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.

Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.

Constraints:

2 <= word.length <= 100
word consists of lowercase English letters only.
"""

#94%
class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        cm = [i[1] for i in c.items()]
        s = sorted(list(set(cm)))
        return (len(s) == 2 and abs(s[1]-s[0] == 1) and cm.count(s[1]) == 1) or (len(s) == 2 and s[0] == 1 and cm.count(s[0]) == 1) or (len(s) == 1 and s[0] == 1) or len(set(word)) == 1

"""
This solution is the same as mine but only sorts as a last resort
from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        unique = {}
        for val in counter.values():
            unique[val] = unique.get(val, 0) + 1

        if len(unique) > 2:
            return False

        if len(unique) == 1:
            if 1 in unique or 1 in unique.values():
                return True
            else:
                return False
        
        if 1 in unique and unique[1] == 1:
            return True
 
        keys = sorted(unique.keys())
        if (keys[1] - keys[0] == 1) and (unique[keys[1]] == 1):
            return True
        return False
"""

"""
Test Cases:
"abcc"
"aazz"
"abc"
"cba"
"bac"
"abbcc"
"ddaccb"
"zz"
"""