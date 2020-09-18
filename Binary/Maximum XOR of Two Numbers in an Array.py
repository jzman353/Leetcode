#Brute Force not enough
"""
Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""
#Time limit exceeded 28/29
class Solution:
    def __init__(self):
        self.max = 0
    def findMaximumXOR(self, nums) -> int:
        nums = list(set(nums))
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                self.max = max(self.max, nums[i] ^ nums[j])
        return self.max

Test = Solution()
print(Test.findMaximumXOR([3, 10, 5, 25, 2, 8]))

"""
# Function to return the  
# maximum xor  
def max_xor( arr , n): 
      
    maxx = 0
    mask = 0;  
  
    se = set() 
      
    for i in range(30, -1, -1): 
          
        # set the i'th bit in mask  
        # like 100000, 110000, 111000.. 
        mask |= (1 << i) 
        newMaxx = maxx | (1 << i) 
      
        for i in range(n): 
              
            # Just keep the prefix till  
            # i'th bit neglecting all  
            # the bit's after i'th bit  
            se.add(arr[i] & mask) 
  
        for prefix in se: 
              
            # find two pair in set  
            # such that a^b = newMaxx  
            # which is the highest  
            # possible bit can be obtained 
            if (newMaxx ^ prefix) in se: 
                maxx = newMaxx 
                break
                  
        # clear the set for next  
        # iteration  
        se.clear() 
    return maxx 
"""