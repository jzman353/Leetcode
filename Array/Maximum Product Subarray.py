#78%
"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

#Runtime: 60 ms
#Memory Usage: 14 MB

import math

def maxProduct(nums) -> int:
    zeros = nums.count(0)
    if zeros > 0:
        maxprod = max(0,nums[0], nums[len(nums) - 1])
    else:
        maxprod = max(nums[0], nums[len(nums) - 1])
    subarray = [[] for i in range(zeros+1)]
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count+=1
        else:
            subarray[zero_count].append(nums[i])
            maxprod = max(maxprod, nums[i])
    for i in subarray:
        if not i:
            continue
        prod = math.prod(i)
        maxprod = max(maxprod, prod)
        if prod > 0:
            pass
        else:
            first = 0
            last = len(nums)-1
            first_check = False
            first_test = False
            last_test = False
            for count2,j in enumerate(i):
                if j<0 and first_check == False:
                    first = count2
                    first_check = True
                    if count2 != 0:
                        first_test = True
                elif j<0:
                    last = count2
                    if count2 != len(i)-1:
                        last_test = True
            if first_test == True:
                maxprod = max(maxprod, math.prod(i[:first]))
            if len(i[first:])>1:
                maxprod = max(maxprod, math.prod(i[first + 1:]))
            if last_test == True:
                maxprod = max(maxprod, math.prod(i[last+1:]), math.prod(i[:last+1]))
            if last_test == True or first_test == True:
                maxprod = max(maxprod, math.prod(i[:last]))
    return maxprod



#print(maxProduct([2,3,-2,4])) #1 6
#print(maxProduct([-2,0,-1])) #2 0
#print(maxProduct([-2,3,-4])) #91/187 24
#print(maxProduct([-2])) #163/187 -2
#print(maxProduct([0])) #163/187 0
#print(maxProduct([2,-5,-2,-4,3])) #168/187 24
print(maxProduct([3,-2,-3,3,-1,0,1])) #181/187 54

'''
def maxProduct(self, nums: List[int]) -> int:
        max_num = min_num = 1
        max_product = float('-inf')
        for num in nums:
            num1 = max_num * num
            num2 = min_num * num
            max_num = max(num, num1, num2)
            min_num = min(num, num1, num2)
            max_product = max(max_product, max_num)
        return max_product
'''