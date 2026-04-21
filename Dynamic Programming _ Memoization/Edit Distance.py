"""
72. Edit Distance
Medium

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
#100%
"""
from collections import defaultdict
import collections

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        return dp[len(word1)][len(word2)]


"""
Think about it this way — you're comparing word1[i] and word2[j] at each step. There are only two cases:
Case 1: characters match (word1[i] == word2[j])

No operation needed, so dp[i][j] = ?

Case 2: characters don't match

You have 3 choices, each costing 1 operation:

Replace: you've now solved dp[i-1][j-1] + 1
Delete from word1: you've now solved dp[i-1][j] + 1
Insert into word1: you've now solved dp[i][j-1] + 1


Take the minimum of the 3
"""


if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.minDistance(input1,input2)
        print(ans)
        return ans


    # Empty / Null inputs
    # Why: Empty string to empty string requires 0 operations.
    assert test("", "") == 0, "Test 1 failed: both empty"

    # Why: Converting empty string to word requires len(word2) insertions.
    assert test("", "abc") == 3, "Test 2 failed: empty to word"

    # Why: Converting word to empty string requires len(word1) deletions.
    assert test("abc", "") == 3, "Test 3 failed: word to empty"

    # Single character
    # Why: Same single char requires 0 operations.
    assert test("a", "a") == 0, "Test 4 failed: same single char"

    # Why: Different single chars requires 1 replace.
    assert test("a", "b") == 1, "Test 5 failed: different single char"

    # Why: Single char to empty requires 1 delete.
    assert test("a", "") == 1, "Test 6 failed: single char to empty"

    # Already equal
    # Why: Identical strings require 0 operations.
    assert test("horse", "horse") == 0, "Test 7 failed: identical strings"

    # Examples from problem
    assert test("horse", "ros") == 3, "Test 8 failed: horse -> ros"
    assert test("intention", "execution") == 5, "Test 9 failed: intention -> execution"

    # One is substring of other
    # Why: Tests pure insertion/deletion with no replacements needed.
    assert test("abc", "abcd") == 1, "Test 10 failed: one insertion"
    assert test("abcd", "abc") == 1, "Test 11 failed: one deletion"

    # Completely different strings
    # Why: No common characters means all replacements + insertions/deletions.
    assert test("abc", "xyz") == 3, "Test 12 failed: completely different same length"

    # Reverse of each other
    # Why: Common failure point for DP solutions that track direction.
    assert test("ab", "ba") == 2, "Test 13 failed: reverse of each other"
    assert test("abc", "cba") == 2, "Test 14 failed: reverse 3 chars"

    # All identical characters
    # Why: Tests solutions that might confuse duplicate character positions.
    assert test("aaa", "aa") == 1, "Test 15 failed: all same char different length"
    assert test("aaaa", "aa") == 2, "Test 16 failed: all same char, 2 deletes"

    # Large length difference
    # Why: When lengths differ greatly, answer should equal the length difference if one is a substring.
    assert test("a", "aaaa") == 3, "Test 17 failed: large length difference"

    # Off by one boundary
    # Why: Single operation needed — catches solutions that are off by one.
    assert test("abc", "bc") == 1, "Test 18 failed: delete first char"
    assert test("abc", "ac") == 1, "Test 19 failed: delete middle char"
    assert test("abc", "ab") == 1, "Test 20 failed: delete last char"
    assert test("abc", "xabc") == 1, "Test 21 failed: insert at front"
    assert test("abc", "axbc") == 1, "Test 22 failed: insert in middle"

    # Common prefix/suffix
    # Why: Solutions should not be tripped up by matching characters at boundaries.
    assert test("abcdef", "abcxyz") == 3, "Test 23 failed: common prefix"
    assert test("xyzabc", "defabc") == 3, "Test 24 failed: common suffix"

    # Replace vs insert+delete tradeoff
    # Why: 1 replace should be cheaper than 1 insert + 1 delete (2 ops).
    assert test("ab", "ac") == 1, "Test 25 failed: replace cheaper than insert+delete"

    # Idempotency
    # Why: Solution should not mutate inputs.
    assert test("horse", "ros") == 3
    assert test("horse", "ros") == 3, "Test 26 failed: idempotency"

    # Return type
    # Why: Must return int not float or string.
    assert isinstance(test("a", "b"), int), "Test 27 failed: return type should be int"

    # Maximum constraint length stress
    # Why: Tests O(n*m) DP handles upper bounds without TLE.
    assert test("a" * 500, "b" * 500) == 500, "Test 28 failed: max length all different"
    assert test("a" * 500, "a" * 500) == 0, "Test 29 failed: max length identical"
    assert test("a" * 500, "") == 500, "Test 30 failed: max length to empty"

    print("All tests passed!")
