'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

Runtime: 380 ms Beats 0%
Memory Usage: 14.6 MB
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        final=len(A)
        i=0
        temp=0
        new=A
        if(final==1):
            return new
        while i<final:
            temp=new[i]
            #print(temp)
            if new[i]%2==0:
                del new[i]
                new=[temp]+new
                i+=1
            else:
                del new[i]
                new.append(temp)
                final-=1
            #print(new)
        return new
            
'''
Runtime: 60 ms
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:      
        if (len(A) == 1):
            return A
        e=[]
        o=[]
        for i in A:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        if (len(evenList) == 0):
            return oddList
        return (e+o)
'''