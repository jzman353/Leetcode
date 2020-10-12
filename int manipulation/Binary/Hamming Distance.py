"""
78%
461. Hamming Distance
Easy

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

Accepted
366,634
Submissions
502,536
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = str(bin(x))
        b = str(bin(y))
        a = a[2:]
        b = b[2:]
        while len(a) < len(b):
            a="0"+a
        while len(b) < len(a):
            b="0"+b
        ans = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                ans += 1
        return ans