'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Runtime: 380 ms Beats 14%
Memory Usage: 19.9 MB
'''

def removeKdigits(num: str, k: int) -> str:
    if k == len(num):
        return '0'

    def buildLowestNumberRec(string1, k, res, final='-1'):
        if k == 0:
            res = res+string1
            return res
        
        if len(string1) <= k:
            return res

        minIndex = 0
        for i in range(k+1):
            if string1[i] < string1[minIndex]:
                minIndex = i
        
        res = res + str(string1[minIndex])
        
        new_str = string1[minIndex+1:len(string1)]

        final = buildLowestNumberRec(new_str, k-minIndex, res, final)
        if final != '-1':
            while final[0] == '0':
                if final == '0':
                    return '0'
                final = final[1:]
            return final
    
    res = ""
    res = buildLowestNumberRec(num, k, res)
    return res

#num,k = "1432219",3 # Test Case 1 Expects 1219
#num,k = "10",2 # Test Case 2 Expects 0
num,k = "10",1 # Test Case 3 Expects 0
print(removeKdigits(num, k))

'''
Runtime: 36ms
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return '0'
        stack = []
        for i in range(len(num)):
            while k > 0 and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        # if there is extra k remains, for instance: 12345 wouldn't delete anything in the previous process
        for _ in range(k):
            stack.pop()
        for i in range(len(stack)):
            if stack[i] != '0':
                return ''.join(stack[i:])
        return '0'
'''


