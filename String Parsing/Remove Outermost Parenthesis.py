'''
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string

Can you find the primitive decomposition? The number of ( and ) characters must be equal.

Runtime: 52 ms, faster than 18.47%
'''

#class Solution:
def removeOuterParentheses(S: str) -> str:
    left = 0
    right = 0
    stack = []
    new_stack = None
    for count, char in enumerate(S):
        if char == '(':
            if not new_stack:
                stack.append(count)
                new_stack = 1
            left += 1
        elif char == ')':
            right +=1
        if left == right != 0:
            new_stack = None
            stack.append(count)
    for count, i in enumerate(stack):
        S = S[:i-count] + S[i+1-count:]
    return S

#Input: "(()())(())"
#Output: "()()()"
#S = "(()())(())"

#Input: "(()())(())(()(()))"
#Output: "()()()()(())"
#S = "(()())(())(()(()))"

#Input: "()()"
#Output: ""
#S = "()()"


removeOuterParentheses(S)

'''
Runtime: 16 ms
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        out=''
        o=0
        c=0
        for i in S:
            if i=='(':
                if o!=c:
                    out+=i
                o+=1
                
            else:
                c+=1
                if o!=c:
                    out+=i
        return out
'''



