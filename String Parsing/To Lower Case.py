'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

Most languages support lowercase conversion for a string data type. However, that is certainly not the purpose of the problem. Think about how the implementation of the lowercase function call can be done easily.
Think ASCII!
Think about the different capital letters and their ASCII codes and how that relates to their lowercase counterparts. Does there seem to be any pattern there? Any mathematical relationship that we can use?

Runtime: 40 ms Beats 9.4%
Memory Usage: 13.8 MB
'''

class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


'''
Runtime: 8 ms

class Solution:
    def toLowerCase(self, str: str) -> str:
        l_str = [ord(i) for i in str]
        for j in range(len(l_str)):
            if l_str[j] > 64 and l_str[j] < 91:
                l_str[j] = l_str[j]+32
            else:
                continue
        res = [chr(val) for val in l_str]
        return ''.join(res)
'''