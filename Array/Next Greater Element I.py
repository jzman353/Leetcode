"""
496. Next Greater Element I
Easy

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.

Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""
#18%
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i,val in enumerate(nums2):
            for j in range(i+1,len(nums2)):
                if nums2[j] > val:
                    d[val] = nums2[j]
                    break
            if val not in d.keys():
                d[val] = -1
        ans = []
        for i in nums1:
            ans.append(d[i])
        return ans

"""
sample 28 ms submission
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dctNextGreater = defaultdict(lambda: -1)        # Defaultdict where all values are initially set to -1
        mono_stack = []                                 # Stack will contain all numbers that haven't found the nextGreaterElement
        for x in nums2:                                 # Iterate over nums2
            while mono_stack and x > mono_stack[-1]:    # If there is a stack, check if x is greater than the most recently added item. Note that if there is more than one item in the stack, it will have to be in reverse sorted order because otherwise the higher number would delete the lower number from the stack before the higher number was added to the stack.
                dctNextGreater[mono_stack.pop()] = x    # Pop the lowest number in the stack and set x as the nextGreaterElement, then check the while loop for the next lowest number in the stack
            mono_stack.append(x)                        # Always append new numbers to the stack so they can be compared to other numbers later on
        
        return [dctNextGreater[x] for x in nums1]
"""