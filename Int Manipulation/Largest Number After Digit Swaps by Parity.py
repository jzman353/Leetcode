"""
2231. Largest Number After Digit Swaps by Parity
Easy

You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.

Constraints:

1 <= num <= 109
"""

#16%
class Solution:
    def largestInteger(self, num: int) -> int:
        s_num = str(num)
        evens = []
        even_idx = set()
        odds = []
        for i, val in enumerate(s_num):
            if int(val) % 2 == 0:
                evens.append(val)
                even_idx.add(i)
            else:
                odds.append(val)
        evens.sort()
        odds.sort()
        answer = ''
        for i in range(len(s_num)):
            if i in even_idx:
                answer += evens.pop()
            else:
                answer += odds.pop()
        return int(answer)

"""
sample 16 ms submission
class Solution:
    def largestInteger(self, num: int) -> int:
        num = [char for char in str(num)]
        ret = []
        
        even, odd = [], []
        for char in num:
            if int(char) & 1:
                odd.append(char)
            else:
                even.append(char)
        
        even.sort(reverse = True)
        odd.sort(reverse = True)
        
        for char in num:
            if int(char) & 1:
                ret.append(odd.pop(0))
            else:
                ret.append(even.pop(0))
        
        return "".join(ret)
"""