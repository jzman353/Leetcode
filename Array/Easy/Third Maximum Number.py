"""
#63%
414. Third Maximum Number
Easy

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

Example 2:

Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

import math

class Solution:
    def thirdMax(self, nums) -> int:
        nums = list(set(nums))
        maxx1 = -math.inf
        maxx2 = -math.inf
        maxx3 = -math.inf
        for i in nums:
            if i > maxx1:
                maxx3 = maxx2
                maxx2 = maxx1
                maxx1 = i
            elif i > maxx2:
                maxx3 = maxx2
                maxx2 = i
            elif i > maxx3:
                maxx3 = i
        if maxx3 != -math.inf:
            return maxx3
        else:
            return maxx1

"""
class Solution:
    def thirdMax(self, nums) -> int:
        maxx1 = -math.inf
        maxx2 = -math.inf
        maxx3 = -math.inf
        for i in nums:
            if i > maxx1:
                maxx3 = maxx2
                maxx2 = maxx1
                maxx1 = i
            elif i == maxx1:
                continue
            elif i > maxx2:
                maxx3 = maxx2
                maxx2 = i
            elif i == maxx2:
                continue
            elif i > maxx3:
                maxx3 = i
        if maxx3 != -math.inf:
            return maxx3
        else:
            return maxx1
"""
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        desc_arr = list( dict.fromkeys(nums)) 
        desc_arr.sort(reverse=True)
        
        if len(desc_arr) < 3:
          return desc_arr[0]
        else:
          return desc_arr[2]
          
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = set(nums)
		
		# return global max if unique number is not enough
        if len(unique_nums) < 3:
            return max( nums )

        # use native min-heap with negation to find maximal number
        unique_nums = list(map(lambda x: -x,unique_nums))#[ -e for e in unique_nums]
        
        # build min-heap
        heapify( unique_nums )
        
        # pop 3rd maximum element
        for _ in range(3):
            value = heappop( unique_nums )
            
        return -value

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        
        if len(s)<3:
            return max(s)
        
        s.remove(max(s))
        s.remove(max(s))
        return(max(s))
"""