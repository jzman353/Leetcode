"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

Example 4:

Input: candidates = [1], target = 1
Output: [[1]]

Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]



Constraints:

    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    All elements of candidates are distinct.
    1 <= target <= 500
"""


class Solution:
    def combinationSum(self, candidates, target: int):
        candidates = sorted(candidates)
        import bisect
        count = bisect.bisect_right(candidates,target)
        for i in range(len(candidates)-count):
            candidates.pop()
        if not candidates:
            return candidates
        print(candidates)

"""
class Solution:
    def combinationSum(self, candidates, target):
        def BackTr(target, curr_sol, k):  
            if target == 0:
                self.sol.append(curr_sol)

            if target < 0 or k >= len(candidates):
                return

            for i in range(k, len(candidates)):
                BackTr(target - candidates[i], curr_sol + [candidates[i]], i)
        
        self.sol = []
        BackTr(target, [], 0)   
        return self.sol
"""

def test(input1,input2):
    Test = Solution()
    print(Test.combinationSum(input1,input2))

candidates = [1,4]
target = 2
test(candidates,target) #[[1,1]]

candidates = [1,4]
target = 4
test(candidates,target) #[[1,1,1,1] [4]]

candidates = [2,3,6,7]
target = 7
test(candidates,target) #[[2,2,3],[7]]

candidates = [2,3,6,7,8,9]
target = 7
test(candidates,target) #[[2,2,3],[7]]

candidates = [2,3,5]
target = 8
test(candidates,target) #[[2,2,2,2],[2,3,3],[3,5]]

candidates = [2]
target = 1
test(candidates,target) #[]

candidates = [1]
target = 1
test(candidates,target) #[[1]]

candidates = [1]
target = 2
test(candidates,target) #[[1,1]]
