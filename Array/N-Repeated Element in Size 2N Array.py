'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even

Runtime: 252 ms Beats 21%
Memory Usage: 15.2 MB
'''

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        new_list=[]
        for i in A:
            if i not in set(new_list):
                new_list.append(i)
            else:
                return i
#O(N) time and O(N) space

'''
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for k in range(1, 3):
            for i in range(len(A) - k):
                if A[i] == A[i + k]:
                    return A[i]
        return A[0]

#O(N) time and O(1) space
'''