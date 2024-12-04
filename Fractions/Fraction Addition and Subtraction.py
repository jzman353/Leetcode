"""
592. Fraction Addition and Subtraction
Solved
Medium
Topics
Companies
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"

Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""

#100%

import fractions
class Solution:
    def fractionAddition(self, expression: str) -> str:
        l = expression.split('+')
        for i in range(len(l)):
            if '-' in l[i]:
                l[i] = l[i].split('-')
                for j in range(len(l[i])):
                    l[i][j] = l[i][j].split('/')
                    if j == 0 and l[i][0] == ['']:
                        l[i][0] = 0
                    elif j == 0 and l[i][0] != ['']:
                        l[i][j] = fractions.Fraction(numerator=int(l[i][j][0]), denominator=int(l[i][j][1]))
                    elif j == 1 and l[i][0] == ['']:
                        l[i][j] = fractions.Fraction(numerator=-int(l[i][j][0]), denominator=int(l[i][j][1]))
                    else:
                        l[i][j] = fractions.Fraction(numerator=-int(l[i][j][0]), denominator=int(l[i][j][1]))
                l[i] = sum(l[i])
            else:
                l[i] = l[i].split('/')
                l[i] = fractions.Fraction(numerator=int(l[i][0]), denominator=int(l[i][1]))
        res = 0
        for i in l:
            res += i
        if res.denominator == 1:
            res = str(res)+"/1"
        return str(res)

"""
class Solution:
    def fractionAddition(self, expression: str) -> str:
        arr = list(map(int, re.findall(r'[+-]?\d+', expression)))
        x = 0
        y = 1        
        for i in range(0, len(arr), 2):
            u, v = arr[i], arr[i + 1]
            x = x * v + u * y
            y *= v        
        c = gcd(x, y)
        return f"{x // c}/{y // c}"

Approach 2 - Parsing with Regular Expressions
Intuition
Note: We understand that most people are not familiar with the intricacies of regular expressions. We include this approach for the sake of article completeness, but we recognize most interviewers will not expect you to know the exact regex patterns needed without additional help.

In the first approach, we manually parsed the expression string, which can be tedious and error-prone. A more efficient and reliable method is to use regular expressions (regex) to tokenize the string. Most languages provide utility functions that will tokenize a string based on a given delimiter expression written in regex. For example, if we are given a string 3a5a10, and we provide a as our delimiter, then the string will be separated into 3, 5, and 10. For this approach, we will come up with a regex expression to match the delimiters needed to split expression.

Regular Expression Breakdown
We would like to break down expression into segments representing individual numbers (either numerator or denominator) along with their corresponding signs. We observe that each fraction is separated by a / character, so let's start by simply using / as our delimiter expression. The breakdown for expression using this regex is shown below:

Tokenizing with first regex expression

We notice that this isn't a sufficient regex expression to match our desired delimiters, as 2 + 1 should ideally be two separate tokens: 2 and +1. To address this, we can add in a regex "lookahead" expression that will create a new token if the next character is a + or a -, and will add the character to the new token. This lookahead expression can be expressed as (?=[-+]). Here, the (?=) portion indicates looking ahead at the next character, and the [-+] argument indicates that the lookahead should be done for either the - character or + character.

Combining these two expressions with the logical OR operator (|), the resulting regex pattern becomes: /|(?=[-+]). With this, we can properly split expression using /, +, and - as delimiters. The final breakdown is shown below:

Tokenizing with second regex expression

This pattern allows us to tokenize the string into manageable parts, making it easier to iterate through each fraction and apply the arithmetic operations as in Approach 1.

Algorithm
Define helper function FindGCD(a, b) to find the greatest common divisor:
If a == 0 return b
Return FindGCD(b % a, a)
Separate expression into tokens by using the regex /|(?=[-+]) as the delimiter. Store the tokens into array nums
Initialize our running result fraction with numerator num = 0 and denominator denom = 0
Initialize i = 0 to iterate through nums
While i < nums.length:
Get the numerator and denominator of next fraction: currNum = nums[i] and currDenom=nums[i+1]
Perform fraction addition/subtraction:
num is updated to num * currDenom + currNum * denom
denom is updated to denom * currDenom
Update iterator: i += 2
Call FindGCD(num, denom) and store result in gcd.
Reduce the result fraction by dividing num and denom by gcd
Return num + "/" + denom to return the resulting fraction in string format

import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1

        # separate expression into signed numbers
        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))

        for i in range(0, len(nums), 2):
            curr_num = int(nums[i])
            curr_denom = int(nums[i + 1])

            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        gcd = abs(self._find_gcd(num, denom))

        num //= gcd
        denom //= gcd

        return str(num) + "/" + str(denom)

    def _find_gcd(self, a: int, b: int) -> int:
        if a == 0:
            return b
        return self._find_gcd(b % a, a)
"""