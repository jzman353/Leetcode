"""
150. Evaluate Reverse Polish Notation
Medium

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

58%
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        first_time = False

        def calc(num1, num2, operator):
            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            elif operator == "/":
                return int(num1 / num2)

        for token in tokens:
            if token in ["+","-","*","/"]:
                num2 = stack.pop()
                num1 = stack.pop()
                ans = calc(num1, num2, token)
                stack.append(ans)
            else:
                stack.append(int(token))

        return ans

if __name__ == '__main__':
    def test(tokens):
        ans = Solution().evalRPN(tokens)
        print(ans)
        return(ans)

    assert test(["2","1","+","3","*"]) == 9          # example 1: ((2+1)*3)
    assert test(["4","13","5","/","+"]) == 6          # example 2: (4+(13/5))
    assert test(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22  # example 3
    assert test(["3"]) == 3                           # single number
    assert test(["2","3","+"]) == 5                   # simple add
    assert test(["5","3","-"]) == 2                   # simple subtract
    assert test(["3","4","*"]) == 12                  # simple multiply
    assert test(["7","2","/"]) == 3                   # simple divide
    assert test(["-7","2","/"]) == -3                 # negative truncates toward zero
    assert test(["7","-2","/"]) == -3                 # negative truncates toward zero
    assert test(["-7","-2","/"]) == 3                 # two negatives
    assert test(["2", "3", "4", "+", "*"]) == 14  # 2*(3+4)
    assert test(["3", "4", "2", "+", "*", "5", "+"]) == 23  # 3*(4+2)+5
    assert test(["1", "2", "+", "3", "*", "4", "-"]) == 5  # ((1+2)*3)-4
    assert test(["5", "1", "2", "+", "4", "*", "+", "3", "-"]) == 14  # 5+((1+2)*4)-3
    assert test(["2", "3", "+", "4", "5", "+", "*"]) == 45  # (2+3)*(4+5)
    assert test(["4", "2", "/", "5", "*"]) == 10  # (4/2)*5
    assert test(["3", "4", "+", "2", "*", "7", "/"]) == 2  # ((3+4)*2)/7
    assert test(["8", "3", "2", "+", "/"]) == 1  # 8/(3+2) - tests number waiting on stack
    assert test(["1", "2", "3", "+", "+"]) == 6  # 1+(2+3) - tests number waiting on stack

    print("All tests passed!")

"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for curr in tokens:
            if curr=="+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            elif curr=="-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)    
            elif curr=="*":
                num1 = stack.pop()    
                num2 = stack.pop()
                stack.append(num2*num1)
            elif curr=="/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))    
            else:
                stack.append(int(curr))    
        return stack.pop()        
"""