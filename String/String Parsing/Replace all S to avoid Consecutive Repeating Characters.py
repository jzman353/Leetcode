"""
1576. Replace All ?'s to Avoid Consecutive Repeating Characters
Easy

Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.



Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".

Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".

Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"

Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"



Constraints:

    1 <= s.length <= 100
    s contains only lower case English letters and '?'.
"""

class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) == 1:
            if s[0] == "?":
                return "a"
        for i in range(len(s)):
            # print(s)
            if s[i] == "?":
                if i == 0:
                    if s[i + 1] != "?" and s[i + 1] != "a":
                        s = "a" + s[1:]
                    elif s[i + 1] != "?" and s[i + 1] == "a":
                        s = "b" + s[1:]
                    elif s[i + 1] == "?":
                        s = "a" + s[1:]
                elif i == len(s) - 1:
                    if s[i - 1] == "a":
                        temp = "b"
                    else:
                        temp = "a"
                    s = s[:len(s) - 1] + temp
                else:
                    if s[i + 1] == "?":
                        if s[i - 1] == "a":
                            temp = "b"
                        else:
                            temp = "a"
                        s = s[:i] + temp + s[i + 1:]
                    else:
                        if s[i - 1] != "a" and s[i + 1] != "a":
                            temp = "a"
                        elif s[i - 1] != "b" and s[i + 1] != "b":
                            temp = "b"
                        elif s[i - 1] != "c" and s[i + 1] != "c":
                            temp = "c"
                        s = s[:i] + temp + s[i + 1:]
        return s

"""
class Solution:
    def modifyString(self, s: str) -> str:
        N = len(s)
        if not N:
            return s
        if N == 1:
            return s if s[0] != '?' else 'a'
        ans = s[0] if s[0] != '?' else ('a' if s[1] != 'a' else 'b')
        for i in range(1, N-1):
            if s[i] != '?':
                ans += s[i]
            elif ans[-1] != 'a' and s[i+1] != 'a':
                ans += 'a'
            elif ans[-1] != 'b' and s[i+1] != 'b':
                ans += 'b'
            else: # {ans[-1], s[i+1]} == {'a','b'}
                ans += 'c'            
        ans += s[-1] if s[-1] != '?' else ('a' if ans[-1] != 'a' else 'b')
        return ans
"""