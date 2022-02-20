"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
#98%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        e = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        self.ans = []
        def helper(digits,val):
            if len(digits) != 0:
                for i in e[digits[0]]:
                    temp = copy.deepcopy(val)
                    temp+=i
                    helper(digits[1:],temp)
            else:
                self.ans.append(val)
        helper(digits,"")
        return self.ans

"""
class Solution:
    def letterCombinations(self, digits: str):
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']
                }
        self.answer = []
        def rPhone(current_str, num):
            if not num:
                self.answer.append(current_str)
            else:
                for i in phone[num[0]]:
                    rPhone(current_str+i, num[1:])

        rPhone("", list(digits))
        return self.answer
"""

"""
sample 8 ms submission
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phn_dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        ans = []
        if len(digits) == 0:
            return []
        def dfs(digits, res, start):
            if start >= len(digits):
                ans.append(''.join(res))
                return
            for char in phn_dict[digits[start]]:
                res.append(char)
                dfs(digits, res, start + 1)
                res.pop()
            return
        
        dfs(digits, [], 0)
        return ans   
"""