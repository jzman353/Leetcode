"""
503. Next Greater Element II
Solved
Medium
Topics
Companies
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
#5%
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        for i in range(len(nums)):
            for j in list(range(i+1, len(nums)))+list(range(0, i)):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break
        return ans

#6%
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        stack = []
        curr_stack = []
        remove = []
        first_run = True
        while first_run or stack:
            if not first_run:
                if stack == curr_stack:
                    break
                curr_stack = copy.deepcopy(stack)
            if first_run:
                for i in range(len(nums)):
                    stack.append(i)
                    for j in stack:
                        if nums[i] > nums[j]:
                            ans[j] = nums[i]
                            remove.append(j)
                    stack = [k for k in stack if k not in remove]
                    remove = []
            else:
                for i in range(max(stack)):
                    if not stack:
                        break
                    for j in stack:
                        if nums[i] > nums[j]:
                            ans[j] = nums[i]
                            remove.append(j)
                    stack = [k for k in stack if k not in remove]
                    remove = []
            if first_run:
                first_run = False
        return ans
"""
Notes about the template :
1) We initialize an empty stack at the beginning.
2) The stack contains the index of items in the array, not the items themselves
3) There is an outer for loop and inner while loop.
4) At the beginning of the program, the stack is empty, so we don't enter the while loop at first.
5) The earliest we can enter the while loop body is during the second iteration of for loop. That's when there is at least an item in the stack.
6) At the end of the while loop, the index of the current element is pushed into the stack
7) The OPERATOR inside the while loop condition decides what type of monotonic stack are we creating.
8) The OPERATOR could be any of the four - >, >=, <, <=

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nextGreater = [-1] * len(nums)
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                top = stack.pop()
                nextGreater[top] = nums[i]
            stack.append(i)
        # First loop - stack has indices, if we find next greater element for any index we save the 
        # result in nextGreater so at the end the indices remaining - are the ones for whom we havent found 
        # next greater.
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                top = stack.pop()
                nextGreater[top] = nums[i]

        return nextGreater
"""