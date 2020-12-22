"""
1014. Best Sightseeing Pair
Medium

Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

Note:

    2 <= A.length <= 50000
    1 <= A[i] <= 1000
"""
"""
#O(n^2) #Time Limit Exceeded
class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        ans = 0
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                ans = max(A[i]+A[j]+i-j,ans)
        return ans
"""

#Didn't find this one by myself 67%
class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        # Kadane's algorithm
        maxsofar = A[0]
        result = 0

        for i in range(1, len(A)):
            result = max(result, maxsofar + A[i] - i)
            maxsofar = max(maxsofar, A[i] + i)

        return result
"""
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        i = 0
        for j in range(1,len(A)):
            res = max(res,A[i]+A[j]+i-j)
            if j-i>A[i]-A[j]:
                i = j
        return res

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # consider B[i] = A[i] + i, C[i] = A[i] -j
        # Find the max of B[i] + C[j]
        B = [A[i] + i for i in range(len(A))]
        C = [A[i] - i for i in range(len(A))]
		
        p, q = 0, 1
        max_score = float('-inf')
        # for each q = 1, 2,..., len(A) - 1
        # update the max of B[0], ...., B[j-1]: B[p]
        # calculate B[q] + C[q]
        while q < len(B):
            if B[q-1] > B[p]:
                p = q - 1 
            max_score = max(max_score, B[p] + C[q])
            q += 1
        return max_score
"""