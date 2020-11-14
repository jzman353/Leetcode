"""
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]

"""
return sorted(l)[-k]
"""

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        from random import randint
        
        # basic idea: three-way quick sort
        # average time complexity: O(n)
        
        def quickSelect(nums, low_bound, high_bound, k):
            
            # should never happen
            if low_bound >= high_bound:
                return None
            
            rand_idx = randint(low_bound, high_bound - 1)
            pivot = nums[rand_idx]
            
            less_ptr, equal_ptr = low_bound, low_bound
            for curr_ptr in range(low_bound, high_bound):
                if nums[curr_ptr] < pivot:
                    temp = nums[curr_ptr]
                    nums[curr_ptr] = nums[equal_ptr]
                    nums[equal_ptr] = nums[less_ptr]
                    nums[less_ptr] = temp
                    less_ptr += 1
                    equal_ptr += 1
                elif nums[curr_ptr] == pivot:
                    temp = nums[curr_ptr]
                    nums[curr_ptr] = nums[equal_ptr]
                    nums[equal_ptr] = temp
                    equal_ptr += 1
                else: # nums[curr_ptr] > pivot
                    pass
                    # nothing need to be done
            
            if k < less_ptr:
                return quickSelect(nums, low_bound, less_ptr, k)
            elif k >= equal_ptr:
                return quickSelect(nums, equal_ptr, high_bound, k)
            else:
                return nums[less_ptr]
            
        return quickSelect(nums, 0, len(nums), len(nums) - k)   
"""