"""
57%
1370. Increasing Decreasing String
Easy

Given a string s. You should re-order the string using the following algorithm:

    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.



Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Example 3:

Input: s = "leetcode"
Output: "cdelotee"

Example 4:

Input: s = "ggggggg"
Output: "ggggggg"

Example 5:

Input: s = "spo"
Output: "ops"



Constraints:

    1 <= s.length <= 500
    s contains only lower-case English letters.

Accepted
25,856
Submissions
33,931
"""

class Solution:
    def sortString(self, s: str) -> str:
        import collections
        c = collections.Counter(''.join(sorted(s)))
        a = ''
        while c.most_common()[0][1]>0:
            stack = []
            for i in c.keys():
                if c[i] > 0:
                    a = a+i[0]
                    c[i] -= 1
                if c[i] > 0:
                    stack.append(i)
            while stack:
                j = stack.pop()
                if j in c.keys() and c[j]>0:
                    a = a+j[0]
                    c[j] -= 1
        return a

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.sortString(input1)
        print(ans)
        return ans


    input1 = "aaaabbbbcccc"
    assert test(input1) == "abccbaabccba"

    input1 = "rat"
    assert test(input1) == "art"

    input1 = "leetcode"
    assert test(input1) == "cdelotee"

    input1 = "ggggggg"
    assert test(input1) == "ggggggg"

    input1 = "spo"
    assert test(input1) == "ops"