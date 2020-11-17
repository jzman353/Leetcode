"""
87% but practically 100%
1646. Get Maximum in Generated Array
Easy

You are given an integer n. An array nums of length n + 1 is generated in the following way:

    nums[0] = 0
    nums[1] = 1
    nums[2 * i] = nums[i] when 2 <= 2 * i <= n
    nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

Return the maximum integer in the array nums.

Example 1:

Input: n = 7
Output: 3
Explanation: According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.

Example 2:

Input: n = 2
Output: 1
Explanation: According to the given rules, the maximum between nums[0], nums[1], and nums[2] is 1.

Example 3:

Input: n = 3
Output: 2
Explanation: According to the given rules, the maximum between nums[0], nums[1], nums[2], and nums[3] is 2.

Constraints:

    0 <= n <= 100
"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        ans = [0,1]
        for i in range(2,n+1):
            if i%2==0:
                ans.append(ans[i//2])
            else:
                ans.append(ans[i//2]+ans[i//2+1])
        return max(ans)

"""
#This approach makes the incorrect assumption that the highest value will always be in the highest two numbers. 
#I assumed that the highest odd value would be the highest result but that is incorrect.
import copy

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        needed = [n, n - 1]
        generated = {0: 0, 1: 1}
        orig = copy.deepcopy(n)

        # print(generated)
        def generate(n1):
            while n1 > 1:
                if n1 % 2 == 1:  # odd
                    n1 = n1 // 2
                    if n1 not in generated.keys() and n1 not in needed:
                        needed.append(n1)
                    if n1 + 1 not in generated.keys() and n1+1 not in needed:
                        needed.append(n1 + 1)
                        generate(n1+1)
                else:
                    n1 = n1 // 2
                    if n1 not in generated.keys() and n1 not in needed:
                        needed.append(n1)
            # print(needed)

        # print(orig)
        generate(orig)
        # print(orig-1)
        generate(orig - 1)

        needed.sort()
        for i in needed:
            if i % 2 == 0:  # even
                generated[i] = generated[i // 2]
            else:
                generated[i] = generated[i // 2] + generated[i // 2 + 1]

        # print(generated)
        return max(generated[n], generated[n - 1])
"""

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.getMaximumGenerated(input1)
        print(ans)
        return ans

    assert test(7) == 3
    assert test(0) == 0
    assert test(1) == 1
    assert test(8) == 3
    assert test(9) == 4
    assert test(15) == 5