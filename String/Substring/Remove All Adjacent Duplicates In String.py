"""
1047. Remove All Adjacent Duplicates In String
Easy

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.



Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".



Note:

    1 <= S.length <= 20000
    S consists only of English lowercase letters.
"""

#Time Limit Exceeded
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        while 1:
            count = 0
            if len(S) == 0 or len(S) == 1:
                return S
            for i in range(len(S)-1):
                if S[i] == S[i+1]:
                    if i+2<len(S):
                        S = S[:i]+S[i+2:]
                    else:
                        S = S[:i]
                    break
                else:
                    count += 1
                if count == len(S)-1:
                    return S
"""

#Second try: #20%
#instead of a while loop and a for loop, use one while loop and move the index backward when an item is deleted
class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        while i < len(S)-1:
            if len(S) == 0 or len(S) == 1:
                return S
            if S[i] == S[i + 1]:
                if i + 2 < len(S):
                    S = S[:i] + S[i + 2:]
                    if i != 0:
                        i -= 1
                else:
                    S = S[:i]
            else:
                i += 1
        return S

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.removeDuplicates(input1)
        print(ans)
        return ans

    assert test("abbaca") == "ca"
    assert test("aaaaaaaa") == ""
    assert test("aaaaaaaaa") == "a"

"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        dup = {ch * 2 for ch in ascii_lowercase}
        prevLength = -1
        currentLength = 0
        while True:
            currentLength = len(S)
            for key in dup:
                S = S.replace(key, "")
            if currentLength == prevLength:
                break
            prevLength = currentLength

        return S
"""