#19%
"""
Random Pick With Weight (Medium)
You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.

Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.

Constraints:

    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.
"""


class Solution:
    def __init__(self, w):
        self.w = w

    def pickIndex(self) -> int:
        import random
        return random.choices(range(len(self.w)), weights = self.w)[0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

if __name__ == '__main__':
    def test(input1):
        Test = Solution(input1)
        ans = Test.pickIndex()
        print(ans)

    w = [1]
    test(w)

    w = [1,1,1,1,0]
    test(w)

# print(timeit.timeit("test([1,8,6,2,5,4,8,3,7])", setup="from __main__ import test", number=10))

"""
class Solution:
  def __init__(self, w: List[int]):
    total = sum(w)
    self.segments = []
    runningSum = 0
    for weight in w:
      runningSum += weight
      self.segments.append(runningSum / total)
  # [0.4, 0.6, 1]
  def pickIndex(self) -> int:
    rand = random.random()
    return bisect.bisect(self.segments, rand)
    # for i in range(len(self.segments)):
    #   if rand < self.segments[i]:
    #     return i - 1
"""