'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

Runtime: 220 ms, faster than 73.73%
'''

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_stack = []
        even_stack = []
        res = []
        parity = 0
        for i in A:
            if i % 2 == 0:
                even_stack.append(i)
            else:
                odd_stack.append(i)
            if parity == 0 and even_stack:
                res.append(even_stack.pop())
                parity = 1
            elif parity == 1 and odd_stack:
                res.append(odd_stack.pop())
                parity = 0
        while even_stack or odd_stack:
            if parity == 1:
                res.append(odd_stack.pop())
                parity = 0
            if parity == 0 and even_stack:
                res.append(even_stack.pop())
                parity = 1
        return res


'''
Runtime: 196 ms
j = 1
    for i in range(0, len(A), 2):
        if A[i] % 2:
            while A[j] %2:
                j += 2
            A[i], A[j] = A[j], A[i]
    return A
'''



