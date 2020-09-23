"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
#20%
class Solution:
    def majorityElement(self, nums):
        third = len(nums)/3
        ans = []
        import collections
        c = collections.Counter(nums)
        for i, count in c.most_common(2):
            if count > third:
                ans.append(i)
        return ans

"""    
#11%
class Solution:
    def majorityElement(self, nums):
        third = len(nums)/3
        dict1 = {}
        ans = []
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
            if dict1[i] > third and i not in ans:
                ans.append(i)
        return ans
"""
if __name__ == '__main__':
    def test(input):
        Test = Solution()
        ans = Test.majorityElement(input)
        print(ans)


    nums = [3,2,3]
    test(nums) #[3]

    nums = [1,1,1,3,3,2,2,2]
    test(nums) #[1,2]

# print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))