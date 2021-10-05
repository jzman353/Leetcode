"""
917. Reverse Only Letters
Easy

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
"""
#82%
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = list(s)
        head = len(l)-1
        tail = 0
        while tail < head:
            if l[tail] not in string.ascii_letters:
                tail += 1
            if l[head] not in string.ascii_letters:
                head -= 1
            if l[tail] in string.ascii_letters and l[head] in string.ascii_letters:
                temp = l[tail]
                l[tail] = l[head]
                l[head] = temp
                tail += 1
                head -= 1
        return "".join(l)
"""
#12%
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = list(s)
        letters = []
        indexes = []
        for i,val in enumerate(l):
            if val in string.ascii_letters:
                letters.append(val)
                indexes.append(i)
        indexes.reverse()
        for i, val in enumerate(indexes):
            l[val] = letters[i]
        return "".join(l)
        
Approach 1: Stack of Letters
Intuition and Algorithm

Collect the letters of S separately into a stack, so that popping the stack reverses the letters. (Alternatively, we could have collected the letters into an array and reversed the array.)

Then, when writing the characters of S, any time we need a letter, we use the one we have prepared instead.

class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

Complexity Analysis

Time Complexity: O(N)O(N), where NN is the length of S.

Space Complexity: O(N)O(N).


Approach 2: Reverse Pointer
Intuition

Write the characters of S one by one. When we encounter a letter, we want to write the next letter that occurs if we iterated through the string backwards.

So we do just that: keep track of a pointer j that iterates through the string backwards. When we need to write a letter, we use it.

class Solution(object):
    def reverseOnlyLetters(self, S):
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        
        return "".join(ans)

Complexity Analysis

Time Complexity: O(N)O(N), where NN is the length of S.

Space Complexity: O(N)O(N).

sample 12 ms submission
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ldx = 0
        rdx = len(s)-1
        slen = rdx
        lets = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        arr = list(s)
        while ldx < rdx:
            while s[ldx] not in lets and ldx+1 < rdx:
                ldx += 1
            while s[rdx] not in lets and rdx-1 > ldx:
                rdx -= 1
            if s[ldx] in lets and s[rdx] in lets:
                arr[ldx], arr[rdx] = arr[rdx], arr[ldx]
            ldx += 1
            rdx -= 1
        return ''.join(arr)
"""