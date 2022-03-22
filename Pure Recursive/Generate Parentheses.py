"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8
"""
#53%
class Solution:
    def generateParenthesis(self, n: int):
        self.answer = []
        def helper(curr,left,right):
            if left > 0:
                helper(curr+"(",left-1,right)
            if right > 0 and left < right:
                if right > 0:
                    helper(curr+")",left,right-1)
            elif right == 0:
                self.answer.append(curr)
        helper("",n,n)
        return self.answer

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.generateParenthesis(input1)
        print(ans)
        return ans

    assert test(1) == ["()"]
    assert test(3) == ["((()))","(()())","(())()","()(())","()()()"]

"""
sample 16 ms submission
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return ['']
        
        stack = []
        res = []
        
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
            
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closeN)
                stack.pop()
                
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack(0, 0)
"""