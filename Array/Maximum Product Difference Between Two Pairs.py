"""
1913. Maximum Product Difference Between Two Pairs
Easy

The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
Example 2:

Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.

Constraints:

4 <= nums.length <= 104
1 <= nums[i] <= 104
"""
#45%
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_four = sorted(nums[:4])
        highest = first_four[3]
        second_highest = first_four[2]
        second_lowest = first_four[1]
        lowest = first_four[0]
        for i in range(4,len(nums)):
            if nums[i] > highest:
                second_highest = highest
                highest = nums[i]
            elif nums[i] == highest:
                second_highest = highest
            elif nums[i] > second_highest:
                second_highest = nums[i]
            elif nums[i] < lowest:
                second_lowest = lowest
                lowest = nums[i]
            elif nums[i] == lowest:
                second_lowest = lowest
            elif nums[i] < second_lowest:
                second_lowest = nums[i]
        return (highest*second_highest) - (lowest*second_lowest)
"""
I honestly don't see how this is faster unless you're only looking at small datasets. Mine only has one pass through 
and a full sort seems inefficient in comparison even if mine has a max of 6 if statements per pass. I suppose 6*n is 
smaller than log(n) in this case. 10000*6 = 60000 while 10000*log10(10000)=40000. Sorting like this stops being 
efficient once n exceeds around 14k-15k
sample 144 ms submission
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return ((nums[-1]*nums[-2])-(nums[0]*nums[1]))
"""