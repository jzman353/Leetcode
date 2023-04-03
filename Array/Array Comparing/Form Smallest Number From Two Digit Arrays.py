"""
2605. Form Smallest Number From Two Digit Arrays
Easy

Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.

Example 1:

Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
Example 2:

Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.

Constraints:

1 <= nums1.length, nums2.length <= 9
1 <= nums1[i], nums2[i] <= 9
All digits in each array are unique.
"""

#100%
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s = sorted(set(nums1)&set(nums2))
        if s:
            return s[0]
        else:
            minn1, minn2 = math.inf, math.inf
            for i in nums1:
                minn1 = min(minn1, i)
            for i in nums2:
                minn2 = min(minn2, i)
            if minn1 <= minn2:
                return int(str(minn1)+str(minn2))
            else:
                return int(str(minn2)+str(minn1))

"""
def list_with_n_digits_with_random_numbers_between_1_and_9(n):
    return random.sample(range(1, 10), n)

#make length of list between 1 and 7 and print 16 results
for i in [random.randint(1, 7) for i in range(16)]:
    print(list_with_n_digits_with_random_numbers_between_1_and_9(i))
"""