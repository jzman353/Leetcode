"""
28. Implement strStr()
Easy

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:

Input: haystack = "", needle = ""
Output: 0

Constraints:

    0 <= haystack.length, needle.length <= 5 * 104
    haystack and needle consist of only lower-case English characters.
"""
#20%
#Optimize this solution by checking "haystack[i:i+len(needle)] == needle" instead of using a loop
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        count = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[count]:
                count += 1
                if count == len(needle):
                    return i - count + 1
                for j in range(i+1,len(haystack)):
                    if haystack[j] == needle[count]:
                        count += 1
                        if count == len(needle):
                            return j - count + 1
                    else:
                        count = 0
                        break
        return -1

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.strStr(input1, input2)
        print(ans)
        return ans

    assert test("hello","ll") == 2
    assert test("aaaaa", "ab") == -1
    assert test("", "") == 0
    assert test("mississippi", "issip") == 4
    assert test("a", "a") == 0
    assert test("abc", "c") == 2

"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)-(len(needle)-1)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
"""