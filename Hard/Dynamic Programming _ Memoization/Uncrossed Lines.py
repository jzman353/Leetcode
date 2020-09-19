"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.



Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2


Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000

Think dynamic programming. Given an oracle dp(i,j) that tells us how many lines A[i:], B[j:] [the sequence A[i], A[i+1], ... and B[j], B[j+1], ...] are uncrossed, can we write this as a recursion?
"""

'''
# Gave up
def maxUncrossedLines(A, B) -> int:
    res = 0
    off_limits = []
    for count1, i in enumerate(A):
        for count2, j in enumerate(B):
            if i == j and count1 not in off_limits and count2 not in off_limits:
                res += 1
                if count1 not in off_limits:
                    off_limits.append(count1)
                if count2 not in off_limits:
                    off_limits.append(count2)
                if count2 - count1 > 0:
                    for k in range(count1, count2 + 1):
                        if k not in off_limits:
                            off_limits.append(k)
                elif count1 - count2 > 0:
                    for k in range(count2, count1 + 1):
                        if k not in off_limits:
                            off_limits.append(k)
                print(i)
                print(count1)
                print(count2)
                print()
    return res
'''


#A = [1, 4, 2]
#B = [1, 2, 4]  # Expected: 2

#A = [2,5,1,2,5]
#B = [10,5,2,1,5,2] # Expected: 3

A = [1,3,7,1,7,5]
B = [1,9,2,5,1] # Expected: 2
#print("answer: " + str(maxUncrossedLines(A, B)))

'''
def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
		from functools import lru_cache
		@lru_cache(None)
		def helper(i, j):
			if i>=len(A) or j>=len(B):
				return 0
			
			at = None
			for ind in range(j, len(B)):
				if B[ind]==A[i]:
					at = ind
					break
		
			ans = 0
			if at!=None:
				ans = max(ans, 1+helper(i+1, at+1))
			ans = max(ans, helper(i+1, j))
			return ans
		
		return helper(0, 0)
'''
#class Solution: Runtime: 228 ms Beats 70%
def maxUncrossedLines(A, B) -> int:
    dp = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if(A[i - 1] == B[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(A)][len(B)]
'''
class Solution:
	def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
		
		A = [ -1 ] + A
		B = [ -1 ] + B
		
		dp_table = {}
		
		def helper( idx_a, idx_b ):
			
			if (idx_a, idx_b) in dp_table:
				return dp_table[(idx_a, idx_b)]
			
			
			if idx_a == 0 or idx_b == 0:
				# Any list compared to empty list give no uncrossed line
				return 0
			
			elif A[idx_a] == B[idx_b]:
				
				dp_table[(idx_a, idx_b)] = helper(idx_a-1, idx_b-1) + 1
				return dp_table[(idx_a, idx_b)]
			else:
				dp_table[(idx_a, idx_b)] = max( helper(idx_a-1, idx_b), helper(idx_a, idx_b-1))
				return dp_table[(idx_a, idx_b)]
		
		# --------------------------------------------
		return helper( len(A)-1, len(B)-1 )

from collections import defaultdict
import bisect
class Solution:
	def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
		dct=defaultdict(list)
		for i in range(len(A)):dct[A[i]].append(i)
		lst=[]
		for i in B:
			if i in dct:
				lst+=dct[i][::-1]
		# find the longest increasing subsequence  of lst
		d=[-1]
		for n in lst:
			if n>d[-1]:
				d.append(n)
			else:
				ind=bisect.bisect_left(d,n)
				d[ind]=n
		return len(d)-1

68 ms
class Solution:
	def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
		s = set(A) & set(B)
		A = [a for a in A if a in s]
		B = [b for b in B if b in s]
		m, n = len(A), len(B)
		if m < n:
			A, B, m, n = B, A, n, m
			
		dp = [0]*(m+1)                      # dp[i] in loop j: check up to A[i], B[j] 
		for j in range(n):                  # B[0]..B[j]
			new_dp = dp[:]
			for i in range(m):              # A[0]..A[i]
				if A[i] == B[j]:
					new_dp[i+1] = dp[i] + 1 # add a new line
				else:
					new_dp[i+1] = max(dp[i+1], new_dp[i])   # choose the best strategy
			dp = new_dp
			
		return dp[-1]
'''
print("answer: " + str(maxUncrossedLines(A, B)))
