'''
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

 

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
Example 2:

Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
Example 3:

Input: nums = [1], index = [0]
Output: [1]
 

Constraints:

1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i

Simulate the process and fill corresponding numbers in the designated spots.

Runtime: 64 ms Beats 0%
Memory Usage: 13.8 MB
'''

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            #print(nums[i])
            #print(index[i])
            #print(len(output))
            #print()
            if index[i] == len(output):
                output.append(nums[i])
            else:
                temp = output[index[i]:]
                output[index[i]] = nums[i]
                output = output[:index[i]+1]
                output.extend(temp)
        return output

'''
Runtime: 12 ms
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        target = []
        i = 0
        while i < len(index):
            target.insert(index[i],nums[i])
            i+=1
        return target
'''

