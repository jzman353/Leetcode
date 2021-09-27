"""
1018. Binary Prefix Divisible By 5
Easy

You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Example 1:

Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: nums = [1,1,1]
Output: [false,false,false]
Example 3:

Input: nums = [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]
Example 4:

Input: nums = [1,1,1,0,1]
Output: [false,false,false,false,false]

Constraints:

1 <= nums.length <= 105
nums[i] is 0 or 1.

"""

#70
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        if nums[0] == 0:
            ans = [True]
        else:
            ans = [False]
        calc = nums[0]
        for i in range(1,len(nums)):
            calc = (calc*2)+nums[i]
            ans.append(calc%5==0)
        return ans

"""
#TLE
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        for i in range(len(nums)):
            ans.append((int(''.join(map(str,nums[:i+1])),2))%5==0)
        return ans
"""

"""
Math explination of best solution
https://math.stackexchange.com/questions/4027896/pattern-for-all-the-binary-chains-divisible-by-5#:~:text=If%20the%20number%20goes%20to%20five%20or%20above,binary%20number%201111101000%202%20%3D%201000%2C%20you%20go%3A

sample 96 ms submission
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        summ = 0
        answers = []
        for num in nums:
            summ = summ * 2 + num
            if summ % 5 == 0:
                answers.append(True)
            else:
                answers.append(False)
                summ = summ % 5
        return answers
        
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result=0
        ans=[]
        for i in range (0,len(nums)):
            result=result*2+nums[i]
            if result % 5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
"""