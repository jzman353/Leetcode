#23%
"""
Repeated Substring Pattern (Easy)
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

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


"""

import timeit
import math

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)//2+1
        for i in range(1,length):
            test = s[:i]*math.ceil(len(s)/(i))
            if s == test:
                return True
        return False

if __name__ == '__main__':
    def test(input):
        Test = Solution()
        ans = Test.repeatedSubstringPattern(input)
        print(ans)

    s = "abab"  # 1 True
    test(s)
    s = "aba"  # 2 False
    test(s)
    s = "abcabcabcabc"  # 3 True
    test(s)
    s = "ababab"  # 102 True
    test(s)

    #print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))

    """
    class Solution:
        def repeatedSubstringPattern(self, s: str) -> bool:
            return s in (2 * s)[1 : -1]
    """
