"""
260. Single Number III
Medium

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""
#42%
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums).most_common()[::-1]
        return [c[0][0],c[1][0]]
"""
#15%
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i in nums:
            if i in d[1]:
                del d[1][bisect.bisect_left(d[1], i)]
            else:
                bisect.insort_left(d[1], i)
        return [d[1][0],d[1][1]]
"""
"""
Apparently it is faster to go through the dictionary a second time rather than delete values from it
sample 50 ms submission
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=[]
        for i in d:
            if d[i]==1:
                ans.append(i)
        return ans 
"""