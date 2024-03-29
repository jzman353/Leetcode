"""
94%
1002. Find Common Characters
Easy

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]



Note:

    1 <= A.length <= 100
    1 <= A[i].length <= 100
    A[i][j] is a lowercase letter

Accepted
82,232
Submissions
121,295
"""

class Solution:
    def commonChars(self, A):
        import collections
        c = collections.Counter(A[0])
        for i in range(1,len(A)):
            c2 = collections.Counter(A[i])
            c = c&c2
        return list(c.elements())