#91%
#Runtime: 24 ms
#Memory Usage: 13.7 MB

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""

def wordPattern(pattern: str, str: str) -> bool:
    pattern_dict = {}
    str_disected = str.split(" ")
    if len(pattern) != len(str_disected):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in pattern_dict:
            if str_disected[i] not in pattern_dict.values():
                pattern_dict[pattern[i]] = str_disected[i]
            else:
                return False
        elif pattern_dict[pattern[i]] != str_disected[i]:
            return False
    return True
"""
def wordPattern(pattern: str, str: str) -> bool:
    pattern_dict = {}
    str_disected = str.split(" ")
    if len(pattern) != len(str_disected):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in pattern_dict:
            pattern_dict[pattern[i]] = str_disected[i]
        elif pattern_dict[pattern[i]] != str_disected[i]:
            return False
    duplication_check = []
    for i in pattern_dict:
        if pattern_dict[i] not in duplication_check:
            duplication_check.append(pattern_dict[i])
        else:
            return False
    return True
"""
print(wordPattern("abba","dog cat cat dog"))#1 True
print(wordPattern("abba","dog cat cat fish"))#2 False
print(wordPattern("aaaa","dog cat cat dog"))#3 False
print(wordPattern("abba","dog dog dog dog"))#4 False
print(wordPattern("aaa","aa aa aa aa"))#19 False