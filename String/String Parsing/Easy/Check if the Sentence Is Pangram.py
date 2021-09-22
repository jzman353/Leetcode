"""
1832. Check if the Sentence Is Pangram
Easy

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false


Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
#87%
import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in string.ascii_lowercase:
            if i not in sentence:
                return False
        return True

"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        numLetter = [0] * 26
        
        for char in sentence:
            numLetter[ord(char) - 97] += 1
        
        return False if 0 in numLetter else True
"""