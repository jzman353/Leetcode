"""
844. Backspace String Compare
Easy

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ = []
        t_ = []
        for i in s:
            if i == "#":
                if s_:
                    s_.pop()
            else:
                s_.append(i)
        for i in t:
            if i == "#":
                if t_:
                    t_.pop()
            else:
                t_.append(i)
        print(s_,t_)
        return s_ == t_

"""
Approach #1: Build String [Accepted]
Intuition

Let's individually build the result of each string (build(S) and build(T)), then compare if they are equal.

Algorithm

To build the result of a string build(S), we'll use a stack based approach, simulating the result of each keystroke.

class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)

Complexity Analysis

Time Complexity: O(M + N)O(M+N), where M, NM,N are the lengths of S and T respectively.

Space Complexity: O(M + N)O(M+N).

Approach #2: Two Pointer [Accepted]
Intuition

When writing a character, it may or may not be part of the final string depending on how many backspace keystrokes occur in the future.

If instead we iterate through the string in reverse, then we will know how many backspace characters we have seen, and therefore whether the result includes our character.

Algorithm

Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped. If a character isn't skipped, it is part of the final answer.

See the comments in the code for more details.

class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))

Complexity Analysis

Time Complexity: O(M + N)O(M+N), where M, NM,N are the lengths of S and T respectively.

Space Complexity: O(1)O(1).
"""