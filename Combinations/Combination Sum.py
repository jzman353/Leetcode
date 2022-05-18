"""
39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

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

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""
#14%
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(candidates,target,curr=[]):
            summ = sum(curr)
            c = []
            for i in range(len(candidates)):
                if target-summ-candidates[i]>=0 and (not curr or candidates[i]>=curr[-1]):
                    c.append(candidates[i])
            for i in range(len(c)):
                #print(curr,c)
                if target-summ-c[i]>0:
                    helper(candidates,target,curr+[c[i]])
                elif target-summ-c[i]==0:
                    ans.append(curr+[c[i]])
        helper(candidates, target)
        return ans

"""
sample 36 ms submission
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSum_sorted(candidates, target)
        
    def combinationSum_sorted(self, candidates, target):
        res=[]
        if target in candidates:
            res.append([target])
        
        for i in range(len(candidates)):
            v = candidates[i]
            if v > target//2:
                break
            else:
                res_next = self.combinationSum_sorted(candidates[i:], target-v)
                for res1 in res_next:
                    res.append([v] + res1)
        return res

sample 40 ms submission
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates=sorted(candidates)
        
        def dfs(target,stack):
            if target == 0:
                res.append(stack)
                return
            for i in candidates:
                if i > target:
                    break
                if stack and i < stack[-1]:
                    continue
                else:
                    dfs(target-i,stack+[i])
        dfs(target,[])
        return res
"""