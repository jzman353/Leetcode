#95%
"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
class Solution:

    def __init__(self, nums):
        self.nums = nums
    """
    def pick(self, target: int) -> int:
        for count, value in enumerate(self.nums):
            if value == target:
                self.nums[count] = 1
            else:
                self.nums[count] = 0
        import random
        return random.choices(range(len(self.nums)), weights=self.nums)[0]
    """
    def pick(self, target: int) -> int:
        ans = []
        for count, value in enumerate(self.nums):
            if value == target:
                ans.append(count)
        import random
        return random.choice(ans)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

if __name__ == '__main__':
    def test(input1,input2):
        Test = Solution(input1)
        ans = Test.pick(input2)
        print(ans)

    nums = [1,2,3,3,3]
    target = 3
    test(nums,target)

# print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))
