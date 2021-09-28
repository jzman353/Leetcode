"""
500. Keyboard Row
Easy

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).
"""
#96%
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set({'u', 't', 'r', 'y', 'i', 'p', 'w', 'o', 'e', 'q'})
        second = set({'f', 'k', 'g', 's', 'h', 'a', 'l', 'd', 'j'})
        third = set({'n', 'b', 'c', 'v', 'z', 'x', 'm'})
        ans = []
        for i in words:
            if len(set(i.lower())-first) == 0 or len(set(i.lower())-second) == 0 or len(set(i.lower())-third) == 0:
                ans.append(i)
        return ans

"""
sample 16 ms submission
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        alphaMap = {
            'Q':0, 'W':0, 'E':0, 'R':0, 'T':0, 'Y':0, 'U':0, 'I':0, 'O':0, 'P':0, 'q':0, 'w':0, 'e':0, 'r':0, 't':0, 'y':0, 'u':0, 'i':0, 'o':0, 'p':0,
            'A':1,'S':1,'D':1,'F':1,'G':1,'H':1,'J':1,'K':1,'L':1,'a':1,'s':1,'d':1,'f':1,'g':1,'h':1,'j':1,'k':1,'l':1,
            'Z':2, 'X':2, 'C':2, 'V':2, 'B':2, 'N':2, 'M':2, 'z':2, 'x':2, 'c':2, 'v':2, 'b':2, 'n':2, 'm':2, 
        }
        outputList = []
        for word in words:
            row = alphaMap[word[0]]
            multiRow = False
            for letter in word:
                if alphaMap[letter] != row:
                    multiRow = True
                    break
            if not multiRow:
                outputList.append(word)
        return outputList
"""