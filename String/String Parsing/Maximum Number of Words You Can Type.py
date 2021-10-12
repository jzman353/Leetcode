"""
1935. Maximum Number of Words You Can Type
Easy

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

Example 1:

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.
Example 2:

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
Example 3:

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.

Constraints:

1 <= text.length <= 104
0 <= brokenLetters.length <= 26
text consists of words separated by a single space without any leading or trailing spaces.
Each word only consists of lowercase English letters.
brokenLetters consists of distinct lowercase English letters.
"""
#45%
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t = text.split()
        answer = len(t)
        for i in t:
            for j in list(brokenLetters):
                if j in i:
                    answer -= 1
                    break
        return answer

"""
#This solution looks the same as mine
sample 16 ms submission
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t = set(brokenLetters)
        count = 0

        for word in text.split():
            for char in word:
                if char in t:
                    count += 1
                    break

        return len(text.split()) - count
"""