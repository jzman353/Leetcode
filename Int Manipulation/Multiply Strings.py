"""
43. Multiply Strings
Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

#100%
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))

"""
Solution
Overview
We are given two non-negative integers that are represented as strings and asked to return the product of the two integers, also in the form of a string. There are a few subtle challenges and edge cases that we must consider to solve this problem. So, before determining how to multiply two numbers in string format, let's first consider a simpler variation of the problem: adding two numbers in string format.
We can add two numbers represented as strings by adding digits from the given numbers in each place. The sum of two digits must be between 0 and 18. The ones place is added to the result while the tens place is carried and summed with the next pair of digits. When summing two numbers, the carried digit will always be zero or one. This process can be repeated for each digit, as shown below.

image

Why does learning how to add two integers represented as strings help us solve this problem? As we will soon see, addition is a subproblem of multiplication. Thus we will need to be able to solve the problem of adding two numbers as strings before we can solve the problem of multiplying two numbers as strings.

If this type of problem is new to you and you would like to practice by solving similar problems, we have provided the list below:

66. Plus One
67. Add Binary
415. Add Strings
989. Add to Array-Form of Integer
Approach 1: Elementary Math
Intuition

Our goal is to multiply two integer numbers that are represented as strings. However, we are not allowed to use a built-in BigInteger library or convert the inputs to integers directly. So how can we multiply the two input strings? We can try to break the problem down into manageable chunks, as is done in elementary mathematics. Thus, we will focus on one digit at a time, just like in the addition example, except here we will be multiplying both numbers digit by digit.

Now, let's recall the process for multiplying two numbers.
We take the ones place digit of the second number, then multiply it with all digits of the first number consequently going backward, and write the result. We need to remember about carry as well. Note that for multiplication, carry may be any digit between 0 and 8.

image


Then we take the tens place digit of the second number and multiply it with all digits of the first number. Since we used the tens place digit, we will multiply this result by 10. Then we write this result below the previous result, signifying that we will add it to the previous result later.

image


Then we continue the same way with hundreds place digit, then with thousands place digit of the second number, and so on, until we have visited every digit in the second number.

image


As is evident from the above diagram, this process is equivalent to multiplying each digit of the second number by the entire first number and appending zeros at the end of each intermediate result based on the place in the second number that the digit came from. Then we add all the results together to get the final product of the first and second numbers.

image


Let's look at an example. Consider 123 * 456123∗456, it can be written as,

\implies (123 * (6 + 50 + 400))⟹(123∗(6+50+400))
\implies (123 * 6) + (123 * 50) + (123 * 400)⟹(123∗6)+(123∗50)+(123∗400)
\implies (123 * 6) + (123 * 5 * 10) + (123 * 4 * 100)⟹(123∗6)+(123∗5∗10)+(123∗4∗100)

\implies \Sigma \space ( firstNumber * j^{th} \space digit \space of \space secondNumber * 10^{(index \space j \space of \space digit \space counting \space from \space the \space end)} )⟹Σ (firstNumber∗j 
th
  digit of secondNumber∗10 
(index j of digit counting from the end)
 )

The results of the multiplication of each digit of the second number with the first number can be stored in an array of strings, and then we can add all these strings to get the final product.

Algorithm

Multiplication of both numbers starts from the ones place digit (the right-most digit), so we should start our multiplication from index num2.size() - 1 and go to index 0. Alternatively, we can reverse both inputs and iterate from index 0 to index num2.size() - 1.

For each digit in num2 that we multiply by num1 we will get a new intermediate result. This intermediate result (currentResult) will be stored in a list, string, or StringBuilder, depending on the language of choice. To calculate each intermediate result, we will start by inserting the appropriate number of zeros according to the current digit's place in the second number (i.e. if it is the hundreds place, we append 2 zeros). Then we will perform the multiplication step as demonstrated in the above diagrams. During this step, we will insert the lower place digits into the currentResult before the higher place digits. Because we are pushing the lower place digits first and always appending to the end, our result will be in reverse order, so once the multiplication and addition steps are complete, we will need to reverse answer before returning.

Let's walk through the steps one by one:

Reverse both numbers.
For each digit in secondNumber:
Keep a carry variable, initially equal to 0.
Initialize currentResult array beginning with the appropriate number of zeros according to the place of the secondNumber digit.
For each digit in firstNumber:
Multiply the secondNumber's digit and the firstNumber's digit and add carry to the multiplication.
Take the remainder of multiplication with 10 to get the last digit.
Append the last digit to the currentResult.
Divide multiplication by 10 to get the new value for carry.
Append the remaining value for carry (if any) to the currentResult.
Push the currentResult into the results array.
Compute the cumulative sum over all the obtained arrays using the ans as an answer.
Reverse ans and return it.
Current
1 / 12
Implementation

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": 
            return "0"
        
        # Reverse both numbers.
        first_number = num1[::-1]
        second_number = num2[::-1]
        
        # For each digit in second_number, multipy the digit by first_number and then
        # store the multiplication result (reversed) in the results array.
        results = []
        for index, digit in enumerate(second_number):
            results.append(self.multiply_one_digit(digit, index, first_number))
        
        # Add all of the results together to get our final answer (in reverse order)
        answer = self.sum_results(results)

        # Reverse answer and join the digits to get the final answer.
        return ''.join(str(digit) for digit in reversed(answer))

    def multiply_one_digit(self, digit2: str, num_zeros: int, first_number: List[str]) -> List[int]:
        """Multiplies first_number by a digit from second_number (digit2)."""
        # Insert zeros at the beginning of the current result based on the current digit's place.
        current_result = [0] * num_zeros
        carry = 0

        # Multiply each digit in first_number with the current digit of the second_number.
        for digit1 in first_number:
            multiplication = int(digit1) * int(digit2) + carry
            # Set carry equal to the tens place digit of multiplication.
            carry = multiplication // 10
            # Append last digit to the current result.
            current_result.append(multiplication % 10)

        if carry != 0:
            current_result.append(carry)
        return current_result
    
    def sum_results(self, results: List[List[int]]) -> List[int]:
        # Initialize answer as a number from results.
        answer = results.pop()

        # Add each result to answer one at a time.
        for result in results:
            new_answer = []
            carry = 0

            # Sum each digit from answer and result. Note: zip_longest is the
            # same as zip, except that it pads the shorter list with fillvalue.
            for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
                # Add current digit from both numbers.
                curr_sum = digit1 + digit2 + carry
                # Set carry equal to the tens place digit of curr_sum.
                carry = curr_sum // 10
                # Append the ones place digit of curr_sum to the new answer.
                new_answer.append(curr_sum % 10)

            if carry != 0:
                new_answer.append(carry)

            # Update answer to new_answer which equals answer + result
            answer = new_answer

        return answer

Complexity Analysis

Here NN and MM are the number of digits in num1 and num2 respectively.

Time complexity: O(M^2 + M \cdot N)O(M 
2
 +M⋅N).

During multiplication, we perform NN operations for each of the MM digits of the second number; this requires O(M \cdot N)O(M⋅N) time. Then we add each of the MM multiplication results (of length O(N + M)O(N+M)) to the answer string; this requires O(M \cdot (M + N))O(M⋅(M+N)) time.

When we multiply a number with one digit, the result's maximum length can be at most one more than the number's length (We can see that when we multiply the max integer of d digits, i.e., 9...99 with 9) and there can be at most (M-1) zeroes initially appended to the result. Hence, each result is of order O(N + M)O(N+M).

Summing the results requires iterating over the length of the current answer for each result. Since the length of two numbers multiplied together cannot be longer than the sum of the lengths of the two numbers, iterating over each digit in the answer will take O(M + N)O(M+N) time and we will do so M - 1M−1 times (for all but one of the MM results). So this step takes O(M \cdot (M + N))O(M⋅(M+N)) time.

Finally, reversing the answer will require O(M + N)O(M+N) time. Taking all steps into consideration, the total time complexity is O(M^2 + M \cdot N)O(M 
2
 +M⋅N).

Space complexity: O(M^2 + M \cdot N)O(M 
2
 +M⋅N).

We store each result of multiplication for each digit of num2 with num1 in the results array. Each multiplication result can have at most N + MN+M length, and there will be MM such results. Thus the space complexity is O(M \cdot (M + N))O(M⋅(M+N)).


Approach 2: Elementary math using less intermediate space
Intuition

Notice that we are storing the multiplication result for every digit in num2. If we know the maximum size of the answer array ahead of time, we can add each multiplication result directly to the final answer. Thus, we can avoid using the extra space required by the results array.

First, let's determine what the maximum size of the answer array would be.

Try a few test cases on your own, multiply two numbers, count how many digits are in the result, and compare that to the number of digits in each number. Notice that whenever two numbers with the number of digits NN and MM are multiplied, the result never exceeds (N+M)(N+M) digits.

We could readily accept that num1.length + num2.length ≥ (num1 · num2).length without rigorous proof. However, it never hurts to verify a relationship that was derived from observation before accepting it as a fact. Don't worry, you will not be expected to provide a proof like this during the interview, hence you can skip it if you want.

The proof that the length of the product of two numbers is always less than or equal to the sum of lengths of the two numbers is as follows: (click to show/hide)

So an answer string of size N + MN+M is guaranteed to be large enough to hold our final result. Let's create one and initialize all of its values as zero. Instead of storing all results of multiplication of each digit of num2num2 with num1num1 like we did in Approach 1, we can directly add the current result to the answer string.

Algorithm

Reverse both numbers.
Initialize ans array with (N+M)(N+M) zeros.
For each digit in secondNumber:
Keep a carry variable, initially equal to 0.
Initialize an array (currentResult) that begins with some zeros based on the place of the digit in secondNumber.
For each digit of firstNumber:
Multiply secondNumber's digit and firstNumber's digit and add previous carry to the multiplication.
Take the remainder of multiplication with 10 to get the last digit.
Append the last digit to currentResult array.
Divide the multiplication by 10 to obtain the new value for carry.
After iterating over each digit in the first number, if carry is not zero, append carry to the currentResult.
Add currentResult to the ans.
If the last digit in ans is zero, before reversing ans, we must pop the zero from ans. Otherwise, there would be a leading zero in the final answer.
Reverse ans and return it.
Current
1 / 11
Implementation

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": 
            return "0"
        
        # Reverse both numbers.
        first_number = num1[::-1]
        second_number = num2[::-1]
        
        # To store the multiplication result of each digit of secondNumber with firstNumber.
        N = len(first_number) + len(second_number)
        answer = [0] * N

        # Multiply each digit in second_number by the first_number
        # and add each result to answer
        for index, digit in enumerate(second_number):
            answer = self.addStrings(self.multiplyOneDigit(first_number, digit, index), answer)

        # Pop excess zero from the end of answer (if any).
        if answer[-1] == 0:
            answer.pop()

        # Ans is in the reversed order.
        # Reverse it to get the final answer.
        answer.reverse()
        return ''.join(str(digit) for digit in answer)
    
    def multiplyOneDigit(self, first_number: str, digit2: str, num_zeros: int):
        # Insert 0s at the beginning based on the current digit's place.
        currentResult = [0] * num_zeros
        carry = 0

        # Multiply firstNumber with the current digit of secondNumber.
        for digit1 in first_number:
            multiplication = int(digit1) * int(digit2) + carry
            # Set carry equal to the tens place digit of multiplication.
            carry = multiplication // 10
            # Append the ones place digit of multiplication to the current result.
            currentResult.append(multiplication % 10)

        if carry != 0:
            currentResult.append(carry)
        return currentResult
    
    def addStrings(self, result: list, answer: list) -> list:
        carry = 0
        i = 0
        new_answer = []
        for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
            # Add current digits of both numbers.
            curr_sum = digit1 + digit2 + carry
            carry = curr_sum // 10
            # Append last digit of curr_sum to the answer.
            new_answer.append(curr_sum % 10)
            i += 1

        return new_answer

Complexity Analysis

Here NN and MM are the number of elements in num 1 and num 2 strings.
"""