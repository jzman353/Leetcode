"""
93%
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in strs:
            if len(i) == 0:
                return ""
        ans = min((word for word in strs if word), key=len)
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if j>len(ans)-1:
                    break
                if strs[i][j] != ans[j]:
                    ans = ans[:j]
                    break
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.longestCommonPrefix(input1)
        print(ans)
        return ans

    assert test(["flower","flow","flight"]) == 'fl'
    assert test(["dog","racecar","car"]) == ''
    assert test(["", ""]) == ""

"""
#Unzips the list and compares each letter to all other letters in all other words until one doesn't match and then breaks
#group will look like ['f','f','f'] for the first example
#res will look like ['f','l'] for the first example
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for group in zip(*strs):
            if len(set(group)) > 1: break
            res.append(group[0])
        return "".join(res)
"""