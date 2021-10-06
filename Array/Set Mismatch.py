"""
645. Set Mismatch
Easy

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
"""
#5%
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        ans = [0]*2
        done = False
        for i in range(len(nums)):
            if not done:
                if d[nums[i]] > 0:
                    ans[0] = nums[i]
                    done = True
                else:
                    d[nums[i]] += 1
            if i not in nums and i != 0:
                ans[1] = i
        if len(nums) not in nums:
            ans[1] = len(nums)
        return ans

"""
sample 174 ms submission
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l, s = len(nums), sum(set(nums))
        l = l * ( 1 + l ) // 2
        return [sum(nums) - s, l - s]
        
We are given that we have numbers from 1 to n and some number x is here twice and another number y is missing. Let us calculate sum of all numbers and sum of squares of all numbes and given this information we can get our answer, using math! For this we need to use couple of facts:

1 + 2 + ... + n = n*(n+1)//2. But even if you do not know this formula you can get it in O(n) time and O(1) space.
1^2 + 2^2 + ... + n^2 = n*(n+1)*(2*n+1)//6. Again if you do not know this formula, you can get it in O(n) time and O(1) space.
Now, let us consider number A = -sum(nums) + n*(n+1)//2. It is equal to y - x, because each element not equal to x and y will be canceled out. In similar way if we define B = -sum(i*i for i in nums) + n*(n+1)*(2*n+1)//6, it will be equal to y*y - x*x. So, we have system of equations now:

A = y - x
B = y*y - x*x.

Dividing one by another we have B/A = y + x, so x = (B/A - A)/2 and y = (B/A + A)/2, which we just return.

Complexity: time complexity is O(n), space complexity is only O(1).

class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        A = -sum(nums) + n*(n+1)//2
        B = -sum(i*i for i in nums) + n*(n+1)*(2*n+1)//6
        return [(B-A*A)//2//A, (B+A*A)//2//A]
"""