'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.

Similar Questions
Perfect Number Easy

For each number in the range, check whether it is self dividing by converting that number to a character array (or string in Python), then checking that each digit is nonzero and divides the original number.

Runtime: 68 ms Beats 30%
Memory Usage: 14 MB
'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        Numbers=[]
        Result=[]
        for i in range(left,right+1):
            #print(i)
            for k,d in enumerate(str(i)):
                #print("d: "+d)
                Numbers.append(int(d))
                #print("Numbers: "+str(Numbers))
                #print(i%Numbers[len(Numbers)-1])
                if Numbers[len(Numbers)-1]==0 or i%Numbers[len(Numbers)-1]!=0:
                    break
                #print(k)
                #print("length"+str(int(len(str(i)))))
                #print(int(k) == int(len(str(i))))
                if int(k)+1 == len(str(i)):
                    Result.append(i)
                #print("Result: "+str(Result))
            Numbers=[]
        return Result







