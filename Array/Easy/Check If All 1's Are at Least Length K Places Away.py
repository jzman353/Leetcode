"""
1437. Check If All 1's Are at Least Length K Places Away
Easy

Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

Example 1:

Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:

Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true
Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true

Constraints:

1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1
"""
#100%
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = -math.inf
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - idx < k+1:
                    return False
                idx = i
        return True

"""
Approach 1: One Pass + Count
Let's first implement a pretty straightforward one-pass idea: to iterate over the array and count the number of zeros in-between the "neighbor" 1s. Each two neighbor 1s should have at least kk zeros in-between. If it's not the case, return false.

simple Fig 1. One pass: count the number of zeros in-between the "neighbour" 1s.

Implementation

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # initialize the counter of zeros to k
        # to pass the first 1 in nums
        count = k
        
        for num in nums:
            # if the current integer is 1
            if num == 1:
                # check that number of zeros in-between 1s
                # is greater than or equal to k
                if count < k:
                    return False
                # reinitialize counter
                count = 0
            # if the current integer is 0
            else:
                # increase the counter
                count += 1
                
        return True

Complexity Analysis

Time complexity: \mathcal{O}(N)O(N) to parse an array of NN elements.

Space complexity: \mathcal{O}(1)O(1) since we don't allocate any additional data structures here.


Approach 2: Bit Manipulation
This approach would be more suitable for the Facebook variation of this problem, when the input is not a binary array but an integer.

In this situation, the problem could be solved with the bitwise trick to remove trailing zeros in the binary representation:


simple Fig 2. Approach 2: use bit manipulations to work with the binary representation of the integer.

Algorithm

Convert binary array into integer x. Note that this conversion always works fine in Python where there is no limit on the value of integers. In Java, the usage of this approach is limited by the integer capacity.

Consider the base cases: return true if x == 0 or k == 0.

Remove trailing zeros in the binary representation of x. That ensures that the last bit of x is 1-bit.

While x is greater than 1:

Remove trailing 1-bit with the right shift: x >>= 1.

Remove trailing zeros one by one, and count them using counter count. The number of zeros in-between 1-bits should be greater or equal to k. Hence, return false if count < k.

We're here because all 1-bits are separated by more than k zeros. Return true.

Implementation

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # convert binary array into int
        x = 0
        for num in nums:
            x = (x << 1) | num
        
        # base case
        if x == 0 or k == 0:
            return True
        
        # remove trailing zeros
        while x & 1 == 0:
            x = x >> 1
        
        while x != 1:
            # remove trailing 1-bit
            x = x >> 1
            
            # count trailing zeros
            count = 0
            while x & 1 == 0:
                x = x >> 1
                count += 1
                
            # number of zeros in-between 1-bits
            # should be greater than or equal to k
            if count < k:
                return False
        
        return True

Complexity Analysis

Time complexity: \mathcal{O}(N)O(N) to parse an array of NN elements.

Space complexity: \mathcal{O}(1)O(1) since we don't allocate any additional data structures here.
"""