"""
#98%
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".



Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.

Example 3:

Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.

Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:

Input: A = "", B = "aa"
Output: false



Constraints:

    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A and B consist of lowercase letters.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if not A or not B:
            return False
        lena = len(A)
        lenb = len(B)
        if lena < 2 or lenb < 2:
            return False
        if lena != lenb:
            return False
        if A == B:
            import collections
            c = collections.Counter(A)
            if c.most_common(1)[0][1]>1:
                return True
            else:
                return False
        index1 = -1
        index2 = -1
        for i in range(lena):
            if A[i] != B[i] and index1 == -1:
                index1 = i
            elif A[i] != B[i] and index1 != -1:
                index2 = i
                break
        if index1 != -1 and index2 != -1:
            if index1>0:
                A2 = A[:index1]+A[index2]+A[index1+1:index2]+A[index1]+A[index2+1:]
            else:
                A2 = A[index2]+A[index1+1:index2]+A[index1]+A[index2+1:]
            if A2 == B:
                return True
            if index1>0:
                B2 = B[:index1]+B[index2]+B[index1+1:index2]+B[index1]+B[index2+1:]
            else:
                B2 = B[index2]+B[index1+1:index2]+B[index1]+B[index2+1:]
            if B2 == A:
                return True
        return False
"""
class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in itertools.izip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
"""