"""
Code
Testcase
Testcase
Test Result

275. H-Index II
Solved
Medium
Topics
Companies
Hint
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in ascending order, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

You must write an algorithm that runs in logarithmic time.

Example 1:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,2,100]
Output: 2


Constraints:

n == citations.length
1 <= n <= 105
0 <= citations[i] <= 1000
citations is sorted in ascending order.
"""

#29%
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        counter = 0
        for i in citations:
            if i < counter+1:
                return counter
            counter += 1
        return counter

"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations)
        while l <= r:
            m = (l + r) // 2
            rank = len(citations) - bisect_left(citations, m)
            if m <= rank:
                l = m + 1
            else:
                r = m - 1
        return r
"""