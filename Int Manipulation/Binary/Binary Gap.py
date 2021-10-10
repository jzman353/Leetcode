"""
868. Binary Gap
Easy

Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

Example 1:

Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
Example 2:

Input: n = 5
Output: 2
Explanation: 5 in binary is "101".
Example 3:

Input: n = 6
Output: 1
Explanation: 6 in binary is "110".
Example 4:

Input: n = 8
Output: 0
Explanation: 8 in binary is "1000".
There aren't any adjacent pairs of 1's in the binary representation of 8, so we return 0.
Example 5:

Input: n = 1
Output: 0

Constraints:

1 <= n <= 109
"""
#89%
class Solution:
    def binaryGap(self, n: int) -> int:
        b = str(bin(n))[2:]
        ans = 0
        prev = -1
        for i in range(len(b)):
            if b[i] == "1":
                if prev != -1:
                    ans = max(ans,i-prev)
                prev = i
        return ans

"""
sample 16 ms submission
class Solution:
    def binaryGap(self, n: int) -> int:
        c, previous, d = 0, -1, 0
        while n > 0:
            r = n % 2
            if r == 1:
                if previous != -1:
                    d = max(d, c - previous)
                previous = c
            n = n // 2
            c += 1
        return d

Approach 1: Store Indexes
Intuition

Since we wanted to inspect the distance between consecutive 1s in the binary representation of N, let's write down the index of each 1 in that binary representation. For example, if N = 22 = 0b10110, then we'll write A = [1, 2, 4]. This makes it easier to proceed, as now we have a problem about adjacent values in an array.

Algorithm

Let's make a list A of indices i such that N has the ith bit set.

With this array A, finding the maximum distance between consecutive 1s is much easier: it's the maximum distance between adjacent values of this array.

class Solution(object):
    def binaryGap(self, N):
        A = [i for i in xrange(32) if (N >> i) & 1]
        if len(A) < 2: return 0
        return max(A[i+1] - A[i] for i in xrange(len(A) - 1))

Complexity Analysis

Time Complexity: O(\log N)O(logN). Note that \log NlogN is the number of digits in the binary representation of NN.

Space Complexity: O(\log N)O(logN), the space used by A.


Approach 2: One Pass
Intuition

In Approach 1, we created an array A of indices i for which N had the ith bit set.

Since we only care about consecutive values of this array A, we don't need to store the whole array. We only need to remember the last value seen.

Algorithm

We'll store last, the last value added to the virtual array A. If N has the ith bit set, a candidate answer is i - last, and then the new last value added to A would be last = i.

class Solution(object):
    def binaryGap(self, N):
        last = None
        ans = 0
        for i in xrange(32):
            if (N >> i) & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
        return ans

Complexity Analysis

Time Complexity: O(\log N)O(logN). Note that \log NlogN is the number of digits in the binary representation of NN.

Space Complexity: O(1)O(1).
"""