#Solved brute force but not good enough

'''Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''

import math
import collections

def repeatedSubstringPattern(s: str) -> bool:
    substring = []
    for i in range(math.ceil(len(s)/2)):
        copy = list(s)
        substring.append(s[i])
        copy = copy[i + 1:]
        while copy:
            if copy[:i+1]==substring:
                copy = copy[i+1:]
                if copy == copy[i+1:]:
                    return True
            else:
                break
    return False

'''
print(repeatedSubstringPattern("abab")) #True
print(repeatedSubstringPattern("aba")) #False
print(repeatedSubstringPattern("abcabcabcabc")) #True
'''
print(repeatedSubstringPattern("abaababaab")) #True
#Passes 74/120 tests Time Limit Exceeded
"""
1)
for i in range(1,int(len(s)/2)+1):
    if set(s.split(s[0:i])) == {''}:
        return True 
    return False

2)    
for i in range(1, len(s)//2+1):
    if N % i == 0 and s[:i]* (N//i) == s:
        return True
return False
"""

