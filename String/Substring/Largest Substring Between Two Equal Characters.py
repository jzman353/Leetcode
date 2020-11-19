"""
88%
1624. Largest Substring Between Two Equal Characters
Easy

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

Example 4:

Input: s = "cabbac"
Output: 4
Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".

Constraints:

    1 <= s.length <= 300
    s contains only lowercase English letters.
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        left = 0
        right = len(s)-1
        ans = -1
        while left<right:
            if ans > right +1:
                break
            if s[left] in seen.keys():
                if seen[s[left]][0] == None:
                    seen[s[left]][0] = left
                    ans = max(ans, seen[s[left]][1]-left-1)
                else:
                    seen[s[left]][0] = min(seen[s[left]][0], left)
                    if seen[s[left]][1] != None:
                        seen[s[left]][1] = max(seen[s[left]][1], left)
                    else:
                        seen[s[left]][1] = left
                    ans = max(ans, seen[s[left]][1] - seen[s[left]][0] - 1)
            else:
                seen[s[left]] = [left, None]
            if s[right] in seen.keys():
                if seen[s[right]][1] == None:
                    seen[s[right]][1] = right
                    ans = max(ans, right-seen[s[right]][0]-1)
                else:
                    seen[s[right]][1] = max(seen[s[right]][1],right)
                    if seen[s[right]][0] != None:
                        seen[s[right]][0] = min(seen[s[right]][0], right)
                    else:
                        seen[s[right]][0] = right
                    ans = max(ans, seen[s[right]][1] - seen[s[right]][0] - 1)
            else:
                seen[s[right]] = [None, right]
            left += 1
            right -= 1
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.maxLengthBetweenEqualCharacters(input1)
        print(ans)
        return ans

    assert test("aa") == 0
    assert test("abca") == 2
    assert test("cbzxy") == -1
    assert test("cabbac") == 4
    assert test("abapoiuytrewqs") == 1
    assert test("zxcvloiuytreaba") == 1
    assert test("mgntdygtxrvxjnwksqhxuxtrv") == 18
    assert test("rimkibmvpnhlgtdkazshyilqmywn") == 21
    assert test("aydsicwrfybunpqsdsnenvrfirr") == 19
    assert test("wtuklxznpebwkkuczifhbimjsckdrkulbbulvfrxcpiwxwdmorldfpktddf") == 53
    assert test("kplphjvvpjgtclucdtrucnwucnsfxpiwspnzdguknznvwgsdsnaitqwkwloubrchcmlxmhgmlcjpaosacgprwxynr") == 80

"""
The benefit of only going in one direction is major simplicity
I was able to find a condition in which the while loop should break early since I was searching from the outside in so my solution should be faster
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        ans = -1

        for i, char in enumerate(s):
            if char not in seen:
                seen[char] = i
            else:
                ans = max(ans, i - seen[char] - 1)

        return ans
"""