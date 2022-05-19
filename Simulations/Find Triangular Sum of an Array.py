"""
2221. Find Triangular Sum of an Array
Medium

You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.

Example 1:

Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.
Example 2:

Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 9
"""
#29%
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            nums2 = []
            for i in range(len(nums)-1):
                nums2.append((nums[i]+nums[i+1])%10)
            if len(nums2)==1:
                return nums2[0]
            #print(nums2)
            nums = []
            for i in range(len(nums2)-1):
                nums.append((nums2[i]+nums2[i+1])%10)
            #print(nums)
        return nums[0]

"""
We can determine the multiplier for each number, how often it goes into the final result.

Consider how often each entry in the triangle gets into the final digit (modulo 10). Let's build a triangle of these frequencies. The final digit is the result, so it gets into itself once:

. . . . .
 . . . .
  . . .
   . .
    1
The two digits above it each get into the bottom digit once:

. . . . .
 . . . .
  . . .
   1 1
    1
The middle digit gets into both of those 1s, and thereby gets into the final digit twice. The border digits still only get into it once:

. . . . .
 . . . .
  1 2 1
   1 1
    1
The digit above 1 2 gets into the 1 and thereby into the final digit once, and it gets into the 2 and thereby into the final digit two more times. Three times overall:

. . . . .
 . 3 . .
  1 2 1
   1 1
    1
With the same argument, the full usage-frequency triangle is:

1 4 6 4 1
 1 3 3 1
  1 2 1
   1 1
    1
It's simply Pascal's triangle upside down.

We can now use the top row frequencies with the input row:

frequencies: 1 4 6 4 1
input row:   1 2 3 4 5 (the problem's first example input)
final digit: (1*1 + 4*2 + 6*3 + 4*4 + 1*5) % 10
           = (1 + 8 + 18 + 16 + 5) % 10
           = (1 + 8 + 8 + 6 + 5) % 10
           = 28 % 10
           = 8
So the top row of frequencies is all we really need. It's the binomial coefficients mCk, where m = n-1 and 0 ≤ k ≤ m. Which we can compute with the multiplicative formula:

      m * (m-1) * ... * (m-k+1) 
mCk = -------------------------
      1  *  2  *  ...  *  k
The next one, mC(k+1), is computed from mCk as mCk * (m-k) / (k+1). So we can compute the whole top row of frequencies from left to right with m multiplications and divisions.

Implementation of that:

def triangularSum(self, nums: List[int]) -> int:
    result = 0
    m = len(nums) - 1
    mCk = 1
    for k, num in enumerate(nums):
        result = (result + mCk * num) % 10
        mCk *= m - k
        mCk //= k + 1
    return result
The above has the issue that the binomial coefficients grow larger than O(1), so the above solution isn't O(n) time O(1) space yet. But the following optimized version is, as it keeps a small representation of the binomial coefficient. Even in Python, it can solve an input of a million digits in less than a second. Also, note that it doesn't modify the input, unlike other O(1) space solutions that overwrite it.

Ideally we'd just compute the binomial coefficient mCk modulo 10, as that's all we need. But while addition, subtraction and multiplication play well under modulo, division doesn't. Instead of dividing by k+1, we can multiply by its inverse modulo 10, but only if that inverse exists. Which it only does if k+1 is coprime to 10. So only if k+1 doesn't have factor 2 or 5. Most numbers do have those factors, so I extract those factors out of mCk and store the exponents of 2 and 5 separately:

mCk ≡ mck * 2exp2 * 5exp5 (modulo 10)

So instead of mCk, I keep track of mck (kept modulo 10), exp2 and exp5, and compute mCk % 10 from them. For example if both exp2 and exp5 are positive, that means the full mCk is a multiple of both 2 and 5 and thus a multiple of 10. Which means modulo 10 it's 0, so the current num doesn't even play a role for the final result, so I skip it. Otherwise the multiplier is mck potentially multiplied by a factor depending on whether exp2 and exp5 are positive or 0. Powers of 2 are 2, 4, 8, 16, 32, 64, etc, modulo 10 they're 2, 4, 8, 6, 2, 4, etc, cycling through 2, 4, 8, 6. Powers of 5 are 5, 25, 125, 625, etc, modulo 10 that's always 5.

def triangularSum(self, nums: List[int]) -> int:
    result = 0
    m = len(nums) - 1
    mck, exp2, exp5 = 1, 0, 0
    inv = (0, 1, 0, 7, 0, 0, 0, 3, 0, 9)
    for k, num in enumerate(nums):
        if not (exp2 and exp5):
            mCk_ = mck * (6, 2, 4, 8)[exp2 % 4] if exp2 else 5 * mck if exp5 else mck
            result = (result + mCk_ * num) % 10
        if k == m:
            return result

        # mCk *= m - k
        mul = m - k
        while not mul % 2:
            mul //= 2
            exp2 += 1
        while not mul % 5:
            mul //= 5
            exp5 += 1
        mck = mck * mul % 10

        # mCk //= k + 1
        div = k + 1
        while not div % 2:
            div //= 2
            exp2 -= 1
        while not div % 5:
            div //= 5
            exp5 -= 1
        mck = mck * inv[div % 10] % 10
"""