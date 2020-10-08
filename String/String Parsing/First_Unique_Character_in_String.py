'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

Runtime: 104 ms Beats 64%
Memory Usage: 14 MB
'''

def firstUniqChar(s: str) -> int:
    i=0
    s1 = list(s)
    if len(s)==0:
        return -1
    if len(s)==1:
        return 0
    while i<=len(s)-1:
        print(s[i])
        print(s[i+1:])
        print(s1)
        if not s1:
            return -1
        elif s[i] in s[i+1:]:
            s1 = list(filter((s[i]).__ne__, s1))
            i+=1
        elif s[i] in s1:
            return i
        else:
            i+=1
    return -1

#s = "aadadaad"
#s = "aaadd"
s="dddccdbba"
print(firstUniqChar(s))

'''
Runtime: 44ms
class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = [s.index(i) for i in set(s) if s.count(i)==1]
        return min(res) if res else -1

Runtime: 92ms
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for key, value in dic.items():
            if value == 1:
                return s.index(key)
        return -1
'''


