"""
0%
Find the Smallest Divisor Given a Threshold
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.



Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4


Constraints:

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
"""

#Time Limit Exceeded when we iterated by 1
import math

class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:

        def try1():
            self.sum2 = 0
            for i in nums:
                self.sum2 += math.ceil(i/self.estimate)

        self.estimate = 1
        self.remember = 1
        try1()
        self.sum_old = self.sum2
        while self.sum2>threshold:
            self.remember = self.estimate
            self.estimate += 100000
            try1()
        self.sum2 = self.sum_old
        self.estimate = self.remember
        while self.sum2>threshold:
            self.remember = self.estimate
            self.estimate += 10000
            try1()
        self.sum2 = self.sum_old
        self.estimate = self.remember
        while self.sum2>threshold:
            self.remember = self.estimate
            self.estimate += 1000
            try1()
        self.sum2 = self.sum_old
        self.estimate = self.remember
        while self.sum2>threshold:
            self.remember = self.estimate
            self.estimate += 100
            try1()
        self.sum2 = self.sum_old
        self.estimate = self.remember
        while self.sum2>threshold:
            self.remember = self.estimate
            self.estimate += 10
            try1()
        self.sum2 = self.sum_old
        self.estimate = self.remember
        while self.sum2>threshold:
            self.remember = self.estimate
            self.estimate += 5
            try1()
        self.sum2 = self.sum_old
        self.estimate = self.remember
        while self.sum2>threshold:
            self.remember = self.estimate
            self.estimate += 2
            try1()
        self.sum2 = self.sum_old
        self.estimate = self.remember
        while self.sum2>threshold:
            self.remember = self.estimate
            self.estimate += 1
            try1()
        return self.estimate

if __name__ == '__main__':
    def test(input1, input2):
        Test = Solution()
        ans = Test.smallestDivisor(input1,input2)
        print(ans)
        return ans

    assert test([1,2,5,9], 6) == 5
    assert test([2,3,5,7,11], 11) == 3
    assert test([19], 5) == 4

"""
from numpy import array, ceil, sum
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums=array(nums)
        left=0
        right=max(nums)
        while(left<right):
            mid=left+((right-left)//2)
            if sum(ceil(nums/mid))>threshold:
                left=mid+1
            else:
                right=mid
        return left
"""