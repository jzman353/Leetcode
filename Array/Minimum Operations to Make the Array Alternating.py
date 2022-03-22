"""
2170. Minimum Operations to Make the Array Alternating
Medium

You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.

Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations.
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""

#33%
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        odd = defaultdict(int)
        even = defaultdict(int)

        max_even = [0, 1]
        next_max_even = [0, None]

        max_odd = [1, 0]
        next_max_odd = [0, None]

        for i in range(len(nums)):
            if i % 2 == 0:
                odd[nums[i]] += 1
                if odd[nums[i]] >= max_odd[0]:
                    if nums[i] != nums[max_odd[1]]:
                        next_max_odd = max_odd
                    max_odd = [odd[nums[i]], i]
                elif odd[nums[i]] > next_max_odd[0]:
                    next_max_odd = [odd[nums[i]], i]
            else:
                even[nums[i]] += 1
                if even[nums[i]] >= max_even[0]:
                    if nums[i] != nums[max_even[1]]:
                        next_max_even = max_even
                    max_even = [even[nums[i]], i]
                elif even[nums[i]] > next_max_even[0]:
                    next_max_even = [even[nums[i]], i]

        if nums[max_even[1]] != nums[max_odd[1]]:
            return len(nums) - (max_odd[0] + max_even[0])
        else:
            return len(nums) - max(max_odd[0] + next_max_even[0], max_even[0] + next_max_odd[0])

"""
sample 1080 ms submission
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)

        even = nums[::2]
        evencnt = Counter(even)
        evencnt[0] = 0
        odd = nums[1::2]
        oddcnt = Counter(odd)
        oddcnt[0] = 0
        
        evenKeys = sorted(evencnt, key=evencnt.get, reverse=True)
        oddKeys = sorted(oddcnt, key=oddcnt.get, reverse=True)

        if evenKeys[0] == oddKeys[0]:
            cand1 = N - evencnt[evenKeys[0]] - oddcnt[oddKeys[1]]
            cand2 = N - evencnt[evenKeys[1]] - oddcnt[oddKeys[0]]
            return min(cand1, cand2)
        else:
            return N - evencnt[evenKeys[0]] - oddcnt[oddKeys[0]]
"""
