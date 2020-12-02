'''
Kadane_algorithm_applied_to_circular_array

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000

For those of you who are familiar with the Kadane's algorithm, think in terms of that. For the newbies, Kadane's algorithm is used to finding the maximum sum subarray from a given array. This problem is a twist on that idea and it is advisable to read up on that algorithm first before starting this problem. Unless you already have a great algorithm brewing up in your mind in which case, go right ahead!
What is an alternate way of representing a circular array so that it appears to be a straight array? Essentially, there are two cases of this problem that we need to take care of. Let's look at the figure below to understand those two cases: (Max subarray in the middle) or (Max subarray split across [wraps])
The first case can be handled by the good old Kadane's algorithm. However, is there a smarter way of going about handling the second case as well?

Runtime: 832 ms Beats 6.3%
Memory Usage: 18 MB
'''

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(A):
            """Find the largest sum of any contiguous subarray."""
            best_sum = float('-inf')
            current_sum = 0
            for x in A:
                current_sum = max(0, current_sum + x)
                best_sum = max(best_sum, current_sum)
            return best_sum
        
        pos=False
        max1 = float('-inf')
        for x in A:
            if x>max1:
                max1 = x
            if x>=0:
                pos = True
        if pos == False:
            return max1
        
        n = len(A) 

        # Case 1: get the maximum sum using standard kadane's algorithm 
        max_kadane = kadane(A) 

        # Case 2: Now find the maximum sum that includes corner 
        # elements. 
        max_wrap = 0
        for i in range(0,n): 
            max_wrap += A[i] 
            A[i] = -A[i] 

        # Max sum with corner elements will be: 
        # array-sum - (-max subarray sum of inverted array) 
        max_wrap = max_wrap + kadane(A) 
        
        # The maximum circular sum will be maximum of two sums 
        if max_wrap > max_kadane: 
            return max_wrap 
        else: 
            return max_kadane 

'''
Runtime: 584 ms
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        maxTotal,maxSoFar,minSoFar,minTotal,s = A[0], A[0], A[0], A[0],A[0]
        for i in range(1, len(A)):
            maxSoFar = max(A[i], maxSoFar + A[i])
            maxTotal = max(maxTotal, maxSoFar)            
            
            minSoFar = min(A[i], minSoFar + A[i])            
            minTotal = min(minTotal, minSoFar)            
            s += A[i]
        if(s == minTotal):
            return maxTotal
        
        return max(s - minTotal, maxTotal); 
'''