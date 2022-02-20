"""
537. Complex Number Multiplication
Medium

A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Constraints:

num1 and num2 are valid complex numbers.
"""
#93%
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        x = num1.split("+")
        x[1] = x[1][:-1]
        y = num2.split("+")
        y[1] = y[1][:-1]
        x=complex(int(x[0]),int(x[1]))
        y=complex(int(y[0]),int(y[1]))
        result = x*y
        return "{}+{}i".format(int(result.real),int(result.imag))

"""
sample 16 ms submission
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, bi = self.extractNums(num1)
        c, di = self.extractNums(num2)
        ac = a * c
        adi = a * di
        bic = bi * c
        bidi = bi * di * -1
        A = ac + bidi
        BI = adi + bic
        return "{}+{}i".format(A, BI)
    def extractNums(self, num):
        values = num.split("+")
        return int(values[0]), int(values[1][:-1])

Approach #1 Simple Solution[Accepted]
Algorithm

Multiplication of two complex numbers can be done as:

(a+ib) \times (x+iy)=ax+i^2by+i(bx+ay)=ax-by+i(bx+ay)(a+ib)×(x+iy)=ax+i 
2
 by+i(bx+ay)=ax−by+i(bx+ay)

We simply split up the real and the imaginary parts of the given complex strings based on the '+' and the 'i' symbols. We store the real parts of the two strings aa and bb as x[0]x[0] and y[0]y[0] respectively and the imaginary parts as x[1]x[1] and y[1]y[1] respectively. Then, we multiply the real and the imaginary parts as required after converting the extracted parts into integers. Then, we again form the return string in the required format and return the result.

public class Solution {

    public String complexNumberMultiply(String a, String b) {
        String x[] = a.split("\\+|i");
        String y[] = b.split("\\+|i");
        int a_real = Integer.parseInt(x[0]);
        int a_img = Integer.parseInt(x[1]);
        int b_real = Integer.parseInt(y[0]);
        int b_img = Integer.parseInt(y[1]);
        return (a_real * b_real - a_img * b_img) + "+" + (a_real * b_img + a_img * b_real) + "i";

    }
}

Complexity Analysis

Time complexity : O(1)O(1). Here splitting takes constant time as length of the string is very small (<20)(<20).

Space complexity : O(1)O(1). Constant extra space is used.
"""