"""
2023. Number of Pairs of Strings With Concatenation Equal to Target
Medium

Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

Example 1:

Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"
Example 2:

Input: nums = ["123","4","12","34"], target = "1234"
Output: 2
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"
Example 3:

Input: nums = ["1","1","1"], target = "11"
Output: 6
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"

Constraints:

2 <= nums.length <= 100
1 <= nums[i].length <= 100
2 <= target.length <= 100
nums[i] and target consist of digits.
nums[i] and target do not have leading zeros.
"""
#6%
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        self.answer = 0
        nums.sort()
        #print(nums)
        def helper(remaining_target, used_inxs=[]):
            if not remaining_target:
                if len(used_inxs) == 2:
                    self.answer += 1
                return
            if len(used_inxs) == 2:
                return
            inx = bisect.bisect_left(nums,remaining_target[0])
            while inx < len(nums) and nums[inx][0] == remaining_target[0]:
                #print(inx, nums[inx], remaining_target, nums[inx] == remaining_target[:len(nums[inx])], inx not in used_inxs, remaining_target[len(nums[inx]):])
                if inx not in used_inxs and nums[inx] == remaining_target[:len(nums[inx])]:
                    helper(remaining_target[len(nums[inx]):],used_inxs+[inx])
                inx += 1
        helper(target)
        return self.answer

"""
sample 32 ms submission
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        freq = collections.Counter(nums)
        # print(freq)

        for e in freq:
            # print(target[:len(e)], target[len(e):] )
            if target[:len(e)] == e:
                suffix = target[len(e):]
                ans += freq[e] * freq[suffix]
                if e == suffix:
                    ans -= freq[suffix]

        return ans
"""