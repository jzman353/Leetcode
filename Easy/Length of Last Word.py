"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

"""

def lengthOfLastWord(s: str) -> int:
    s = s.rstrip()
    if " " not in s:
        return len(s)
    for count, letter in enumerate(reversed(s)):
        if letter == " ":
            return count

#print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord(""))
print(lengthOfLastWord("a"))
print(lengthOfLastWord("a "))

"""def lengthOfLastWord(s: str) -> int:
    s = s.rstrip()
    if " " not in s:
        return len(s)
    count = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == " ":
            return count
        else:
            count +=1"""