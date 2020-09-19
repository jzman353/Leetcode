'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
   Hide Hint #1  
You should make use of what you have produced already.
   Hide Hint #2  
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
   Hide Hint #3  
Or does the odd/even status of the number help you in calculating the number of 1s?
'''

def countBits(num: int):
        count_ones = 0
        if num % 2 == 1:
            count_ones += 1
        x = 1
        while 2**x <= num:
            x *= 2
        x /= 2
        if x == 0.5:
            output = [count_ones]
        elif x == 1:  # num is 2 or higher
            count_ones += 1  # MSB
        else:
            count_ones += 1  # MSB
            for i in range(int(x), 1, -1):
                if x % i == 1:
                    count_ones += 1

        return count_ones

'''
print(countBits(0))
print(countBits(1))
print(countBits(2))
print(countBits(3))
print(countBits(4))
print(countBits(5))
'''
print(countBits(6))




