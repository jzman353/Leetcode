"""
2094. Finding 3-Digit Even Numbers
Easy

You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.

Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array.
Notice that there are no odd integers or integers with leading zeros.
Example 2:

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits.
In this example, the digit 8 is used twice each time in 288, 828, and 882.
Example 3:

Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.

Constraints:

3 <= digits.length <= 100
0 <= digits[i] <= 9
"""
#67%
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        l_evens = list(i for i in digits if i%2==0)
        s_evens = set(l_evens)
        self.answer = []
        self.seen = set()
        def helper(digits,len_evens,curr=''):
            for i in range(len(digits)):
                if len(curr) == 2:
                    if digits[i] in s_evens and curr+str(digits[i]) not in self.seen:
                        self.seen.add(curr+str(digits[i]))
                        self.answer.append(int(curr+str(digits[i])))
                elif len(curr) == 1 and curr+str(digits[i]) not in self.seen:
                    if digits[i] in s_evens:
                        if len_evens > 1:
                            self.seen.add(curr+str(digits[i]))
                            helper(digits[:i]+digits[i+1:],len_evens-1,curr=curr+str(digits[i]))
                    else:
                        self.seen.add(curr+str(digits[i]))
                        helper(digits[:i]+digits[i+1:],len_evens,curr=curr+str(digits[i]))
                elif curr+str(digits[i]) not in self.seen:
                    if digits[i] in s_evens:
                        if len_evens > 1 and digits[i] != 0:
                            self.seen.add(curr+str(digits[i]))
                            helper(digits[:i]+digits[i+1:],len_evens-1,curr=curr+str(digits[i]))
                    else:
                        self.seen.add(curr+str(digits[i]))
                        helper(digits[:i]+digits[i+1:],len_evens,curr=curr+str(digits[i]))

        helper(digits,len(l_evens))
        return list(self.answer)

"""
sample 48 ms submission
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans,cnt = [], Counter(digits)
        
        for i in range(1,10):
            for j in range(0,10):
                for k in range(0,10,2):
                    if cnt[i] > 0 and cnt[j] > (i==j) and cnt[k] > (k==j) + (k==i):
                        ans.append(i*100 + j*10 + k*1)
        return ans
"""