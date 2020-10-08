'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

You may assume that both strings contain only lowercase letters.

Runtime: 56 ms Beats 60%
Memory Usage: 14.3 MB
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mList = list(magazine)
        try:
            for i in ransomNote:
                mList.remove(i)
        except:
            return False
        return True

'''
Runtime: 16ms
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteLetters = set(list(ransomNote))
        for l in noteLetters:
            if magazine.count(l) < ransomNote.count(l):
                return False
        
        return True
        
Runtime: 24ms
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,"",1)
            else: return False
        
        return True
'''