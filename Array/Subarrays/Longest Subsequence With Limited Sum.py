"""
2389. Longest Subsequence With Limited Sum
Easy

You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
Example 2:

Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.

Constraints:

n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 106
"""

#9%
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        l = sorted(nums)
        ans = []
        for i in queries:
            temp = l.copy()
            s = sum(temp)
            while s > i:
                try:
                    s -= temp.pop()
                except:
                    break
            ans.append(len(temp))
        return ans

"""
Sample 93 ms submission

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] 
            
        answer = []
        for query in queries:
            answer.append(bisect.bisect_right(nums, query))
            
        return answer
"""

import random
def test_cases():
    n = random.randint(1, 1000)
    m = random.randint(1, 1000)
    nums = random.choices(list(range(1000000)),k=n)
    queries = random.choices(list(range(1000000)),k=m)
    print(nums)
    print(queries)

for i in range(8):
    test_cases()